"""
Device model (SCADA field asset simulation)

Represents a simulated industrial asset similar to a PLC-connected device in a SCADA system.

Each device:
* Has a unique ID (used as part of MQTT topic structure)
* Has a device type (pump, tank, motor)
* Maintains a set of runtime tags (sensor values)

Devices simulate field telemetry and publish updates using MQTT to a central gateway for processing.
"""

from device_types import TEMPLATES
import copy
import random
import json
import paho.mqtt.client as mqtt
from config import MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_TOPIC_ROOT


class Device:

    # Each device instance represents a simulated industrial asset.
    # In SCADA systems, this would correspond to a PLC/RTU
    # publishing process data into the gateway.
    def __init__(self, device_id, device_type="pump"):
        self.device_id = device_id
        self.device_type = device_type

        # IMPORTANT: copy so each device gets its own instance
        self.tags = copy.deepcopy(TEMPLATES.get(device_type, {}))

        # MQTT client used to publish telemetry to the SCADA gateway
        self.mqtt = mqtt.Client()

        # Connects to shared broker (configured in config.py)
        self.mqtt.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

        # Starts background network loop for publishing messages
        # (required for async MQTT communication)
        self.mqtt.loop_start()

    def simulate(self):
        # Simulates sensor drift similar to real-world process variability
        # In production systems, this data would come from actual field sensors
        # using protocols like OPC UA or MQTT

        for k in self.tags:
            if isinstance(self.tags[k], (int, float)):
                self.tags[k] += random.uniform(-1, 1)

        # Payload represents telemetry snapshot sent to SCADA gateway
        payload = {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "tags": self.tags
        }

        # MQTT topic structure defines routing for the gateway subscription model
        topic = f"{MQTT_TOPIC_ROOT}/{self.device_id}/telemetry"

        # Publish telemetry to broker (gateway consumes this data)
        self.mqtt.publish(topic, json.dumps(payload))
