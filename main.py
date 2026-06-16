"""
Mini SCADA Simulator

This project simulates a simplified SCADA system using an MQTT-based architecture.

In a real SCADA system:
* This process represents a combination of field device simulation and operator interface
* A separate Gateway process handles telemetry ingestion, alarm evaluation, and event logging
* MQTT is used as the communication layer between devices and the gateway
"""

# Architecture mapping:
# main.py    → device simulation + CLI operator interface
# gateway.py → telemetry processing + alarm engine + event generation
# MQTT       → message transport layer

import threading
import time
from cli import run_cli
from store import devices


def simulation_loop():
    # Simulates real-time field device telemetry updates in a SCADA environment
    # at a fixed interval, similar to real-time tag updates in Ignition.
    while True:
        for device in devices.values():
            device.simulate()
        time.sleep(1)


if __name__ == "__main__":
    sim_thread = threading.Thread(target=simulation_loop, daemon=True)
    sim_thread.start()

    run_cli()
