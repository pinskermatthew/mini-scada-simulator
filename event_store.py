from datetime import datetime

events = []


def add_event(device_id, event_type, tag, value, message):
    events.append({
        "timestamp": datetime.utcnow().isoformat(),
        "device_id": device_id,
        "type": event_type,
        "tag": tag,
        "value": value,
        "message": message
    })
