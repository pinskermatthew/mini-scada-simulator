"""
Device Type Templates

Represents SCADA-style UDT (User Defined Type) equivalents.

In Ignition:
- These would correspond to UDT definitions
- Each type defines a reusable tag structure for assets
"""

# Template defines standard tag structure for this device type
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
# These are evaluated by Device.check_alarms() at runtime.
# Logic (>, <, state tracking) is handled in code; this is configuration only.
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
