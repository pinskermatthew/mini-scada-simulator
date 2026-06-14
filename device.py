"""
Device Model (SCADA Asset Simulation)

Represents an industrial asset similar to a PLC-connected device
in a SCADA system like Ignition.

Each device:
- Has a unique ID (tag provider key equivalent)
- Has a device type (pump, tank, motor)
- Maintains a set of runtime tags (sensor values)
"""

from device_types import TEMPLATES
import copy
import random


class Device:

    # Each device instance represents a real-world industrial asset.
    # In Ignition, this would correspond to a tag structure under a device folder.
    def __init__(self, device_id, device_type="pump"):
        self.device_id = device_id
        self.device_type = device_type

        # IMPORTANT: copy so each device gets its own instance
        self.tags = copy.deepcopy(TEMPLATES.get(device_type, {}))

    def simulate(self):
        # Simulates sensor drift similar to real-time telemetry updates
        # In real systems, this data would come from PLCs via OPC UA or MQTT
        for k in self.tags:
            if isinstance(self.tags[k], (int, float)):
                self.tags[k] += random.uniform(-1, 1)
