"""
Event store (SCADA event journal simulation)

This module simulates a lightweight SCADA event journal / historian buffer.

In SCADA systems:
* Events represent alarm transitions and system state changes
* These are typically stored in a central event journal or database
* Used for auditing, diagnostics, and historical analysis
"""

from datetime import datetime

# In-memory event buffer (simple simulation of a historian/event journal)
events = []


def add_event(device_id, event_type, tag, value, message):
    # Adds a structured event to the global event store.
    # In production SCADA systems, this would be persisted
    # to a database or historian service rather than in-memory storage.

    events.append({
        "timestamp": datetime.utcnow().isoformat(),
        "device_id": device_id,
        "type": event_type,
        "tag": tag,
        "value": value,
        "message": message
    })
