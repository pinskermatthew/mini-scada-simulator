"""
Device Store (In-Memory SCADA Tag Registry)

Acts like a simplified version of a SCADA Gateway tag database.

In Ignition:
- This resembles the Gateway's live tag memory
- Stores active device instances during runtime
"""

devices = {}
