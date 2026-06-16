"""
Device type templates

Defines reusable SCADA-style device configurations, similar to
User Defined Types (UDTs).

In SCADA systems:
* UDTs define reusable tag structures for assets
* Each instance (device) inherits this structure at runtime
"""

# Template defines the default runtime tag structure for each device type.
# These simulate SCADA tag hierarchies (for example, PLC tag folders).
TEMPLATES = {
    "pump": {
        "pressure": 30.0,
        "temperature": 70.0,
        "status": "running"
    },
    "tank": {
        "level": 50.0,
        "temperature": 65.0,
        "status": "idle"
    },
    "motor": {
        "rpm": 1200,
        "temperature": 75.0,
        "status": "running"
    }
}

# Alarm thresholds per device type.
# These are evaluated by the gateway alarm engine when processing MQTT telemetry.
# Devices only publish raw values. Alarm logic is centralized in the gateway.
ALARMS = {
    "tank": {
        "level": {
            "high": 90
        }
    },
    "pump": {
        "pressure": {
            "low": 10
        }
    },
    "motor": {
        "temperature": {
            "high": 100
        }
    }
}
