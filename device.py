"""
Device Model (SCADA Asset Simulation)

Represents an industrial asset similar to a PLC-connected device
in a SCADA system like Ignition.

Each device:
- Has a unique ID (tag provider key equivalent)
- Has a device type (pump, tank, motor)
- Maintains a set of runtime tags (sensor values)
"""

from device_types import TEMPLATES, ALARMS
import copy
import random
from event_store import add_event


class Device:

    # Each device instance represents a real-world industrial asset.
    # In Ignition, this would correspond to a tag structure under a device folder.
    def __init__(self, device_id, device_type="pump"):
        self.device_id = device_id
        self.device_type = device_type

        # IMPORTANT: copy so each device gets its own instance
        self.tags = copy.deepcopy(TEMPLATES.get(device_type, {}))
        self.alarm_state = {
            "level": {
                "high": False,
                "low": False
            }
        }
        self.events = []

    def simulate(self):
        # Simulates sensor drift similar to real-time telemetry updates
        # In real systems, this data would come from PLCs via OPC UA or MQTT
        for k in self.tags:
            if isinstance(self.tags[k], (int, float)):
                self.tags[k] += random.uniform(-1, 1)

        self.check_alarms()

    def check_alarms(self):
        device_alarms = ALARMS.get(self.device_type, {})

        for tag_name, rules in device_alarms.items():
            value = self.tags.get(tag_name)

            if value is None:
                continue

            # Ensure structure exists
            if tag_name not in self.alarm_state:
                self.alarm_state[tag_name] = {"high": False, "low": False}

            state = self.alarm_state[tag_name]

            # HIGH alarm
            if "high" in rules:
                is_active = value > rules["high"]
                was_active = state["high"]

                if is_active and not was_active:
                    add_event(
                        self.device_id,
                        "ALARM_ACTIVE",
                        tag_name,
                        value,
                        f"HIGH > {rules['high']}"
                    )

                if not is_active and was_active:
                    add_event(
                        self.device_id,
                        "ALARM_CLEARED",
                        tag_name,
                        value,
                        "Returned to normal"
                    )

                state["high"] = is_active

            # LOW alarm
            if "low" in rules:
                is_active = value < rules["low"]
                was_active = state["low"]

                if is_active and not was_active:
                    add_event(
                        self.device_id,
                        "ALARM_ACTIVE",
                        tag_name,
                        value,
                        f"LOW < {rules['low']}"
                    )

                if not is_active and was_active:
                    add_event(
                        self.device_id,
                        "ALARM_CLEARED",
                        tag_name,
                        value,
                        "Returned to normal"
                    )

                state["low"] = is_active
