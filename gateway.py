"""
SCADA gateway (MQTT telemetry processor)

This module simulates the core SCADA gateway runtime.

In a real SCADA system:
* The gateway subscribes to field device telemetry streams
* Processes incoming data in real time
* Evaluates alarm conditions centrally
* Generates events for audit/history systems
"""

import json
import paho.mqtt.client as mqtt
from device_types import ALARMS
from event_store import add_event
from config import MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_TOPIC_ROOT

alarm_state = {}


def on_connect(client, userdata, flags, rc):
    # Triggered when the gateway successfully connects to the MQTT broker.

    if rc == 0:
        print("Gateway connected to broker")

        # Subscribe to all device telemetry streams.
        client.subscribe(f"{MQTT_TOPIC_ROOT}/+/telemetry")
    else:
        print(f"Connection failed with code {rc}")


def on_subscribe(client, userdata, message_id, granted_qos):
    # Called when broker acknowledges a subscription request.
    print(f"Subscribed (message_id={message_id}, qos={granted_qos})")


def on_message(client, userdata, msg):
    # Entry point for all incoming telemetry messages.
    # The flow is to decode MQTT payload, extract device metadata and tag values,
    # then forward data to alarm evaluation engine.

    payload = json.loads(msg.payload.decode())

    device_id = payload["device_id"]
    device_type = payload["device_type"]
    tags = payload["tags"]

    print("\n--- TELEMETRY RECEIVED ---")
    print(f"Topic: {msg.topic}")
    print(f"Device: {device_id}")
    print(f"Type: {device_type}")
    print(f"Tags: {tags}")

    # Pass telemetry to alarm evaluation engine
    check_alarms(device_id, device_type, tags)


def check_alarms(device_id, device_type, tags):
    # Gateway alarm evaluation engine.

    device_alarms = ALARMS.get(device_type, {})

    # Initialize per-device state tracking
    if device_id not in alarm_state:
        alarm_state[device_id] = {}

    state = alarm_state[device_id]

    for tag_name, rules in device_alarms.items():
        value = tags.get(tag_name)

        if value is None:
            continue

        # Initialize per-tag alarm state
        if tag_name not in state:
            state[tag_name] = {
                "high": False,
                "low": False
            }

        tag_state = state[tag_name]

        # -------------------
        # HIGH ALARM
        # -------------------
        if "high" in rules:
            is_active = value > rules["high"]
            was_active = tag_state["high"]

            # Alarm transition: inactive → active
            if is_active and not was_active:
                add_event(
                    device_id,
                    "ALARM_ACTIVE",
                    tag_name,
                    value,
                    f"HIGH > {rules['high']}"
                )

            # Alarm transition: active → cleared
            if not is_active and was_active:
                add_event(
                    device_id,
                    "ALARM_CLEARED",
                    tag_name,
                    value,
                    "Returned to normal"
                )

            tag_state["high"] = is_active

        # -------------------
        # LOW ALARM
        # -------------------
        if "low" in rules:
            is_active = value < rules["low"]
            was_active = tag_state["low"]

            # Alarm transition: inactive → active
            if is_active and not was_active:
                add_event(
                    device_id,
                    "ALARM_ACTIVE",
                    tag_name,
                    value,
                    f"LOW > {rules['low']}"
                )

            # Alarm transition: active → cleared
            if not is_active and was_active:
                add_event(
                    device_id,
                    "ALARM_CLEARED",
                    tag_name,
                    value,
                    "Returned to normal"
                )

            tag_state["low"] = is_active


def main():
    # Initializes the SCADA gateway runtime.

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    # Connect to configured MQTT broker.
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

    # Start processing loop.
    client.loop_forever()


if __name__ == "__main__":
    main()
