"""
Mini SCADA Simulator

This project simulates a simplified SCADA gateway similar in concept to
Inductive Automation's Ignition.

In a real SCADA system:
- This process would represent the Gateway runtime
- It would manage device connections, tag values, and execution logic
"""

import threading
import time
from cli import run_cli
from store import devices


def simulation_loop():
    # Simulates a SCADA gateway runtime loop that continuously updates device data
    # at a fixed interval, similar to real-time tag updates in Ignition.
    while True:
        for device in devices.values():
            device.simulate()
        time.sleep(1)


if __name__ == "__main__":
    sim_thread = threading.Thread(target=simulation_loop, daemon=True)
    sim_thread.start()

    run_cli()
