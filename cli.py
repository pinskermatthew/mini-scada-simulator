"""
CLI Gateway Console

This module simulates an operator interface similar to:
- Ignition Gateway scripting console
- Industrial maintenance terminal tools

Responsibilities:
- Accept user commands
- Interact with the device registry
- Trigger simulated tag updates

NOT responsible for:
- Device logic
- Data modeling
"""

from store import devices
from device import Device
from event_store import events


def run_cli():
    print("\nSCADA Gateway Console (type 'help' for commands)\n")

    while True:
        command = input("> ").strip().split()

        if not command:
            continue

        cmd = command[0]

        # -------------------
        # EXIT
        # -------------------
        if cmd in ["exit", "quit"]:
            print("Shutting down gateway...")
            break

        # -------------------
        # HELP
        # -------------------
        elif cmd == "help":
            print("""
            Commands:
              add id=<id> type=<type>     Create a device
              list                        List all devices
              show id=<id>                Show device tags
              events id=<id>              View events for a device
              simulate id=<id>            Manually update device values once
              exit                        Quit
            """)

        # -------------------
        # ADD DEVICE
        # -------------------
        elif cmd == "add":
            if len(command) < 3:
                print("Usage: add id=<id> type=<type>")
                continue

            args = {}

            for a in command[1:]:
                key, value = a.split("=")
                args[key] = value

            device_id = args.get("id")
            device_type = args.get("type", "pump")

            if device_id in devices:
                print("Device already exists")
                continue

            devices[device_id] = Device(device_id, device_type)
            print(f"Device created: {device_id} ({device_type})")

        # -------------------
        # LIST DEVICES
        # -------------------
        elif cmd == "list":
            if not devices:
                print("No devices found.")
                continue

            for d in devices.values():
                print(f"- {d.device_id}")

        # -------------------
        # SHOW DEVICE
        # -------------------
        elif cmd == "show":
            args = {}

            for a in command[1:]:
                key, value = a.split("=")
                args[key] = value

            device_id = args.get("id")

            if not device_id:
                print("Usage: show id=<device_id>")
                continue

            device = devices.get(device_id)

            if not device:
                print("Device not found")
                continue

            print(f"\nDevice: {device_id} ({device.device_type})")

            for k, v in device.tags.items():
                print(f"{k}: {v}")

        # -------------------
        # VIEW EVENTS
        # -------------------
        elif cmd == "events":
            device_id = args.get("id")

            device = devices.get(device_id)

            if not device:
                print("Device not found")
                continue

            for e in events[-20:]:
                if e["device_id"] == device_id:
                    print(e)

        # -------------------
        # SIMULATE
        # -------------------
        elif cmd == "simulate":
            args = {}

            for a in command[1:]:
                if "=" not in a:
                    print(f"Invalid argument: {a}")
                    continue

                key, value = a.split("=", 1)
                args[key] = value

            device_id = args.get("id")

            if not device_id:
                print("Usage: simulate id=<device_id>")
                continue

            device = devices.get(device_id)

            if not device:
                print("Device not found")
                continue

            # Manual override (NOT the main simulation path)
            # In real SCADA systems, this would be replaced by live OPC/MQTT updates
            device.simulate()
            print(f"Manually simulated device: {device_id}")
