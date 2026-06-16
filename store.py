"""
Device store (In-memory runtime registry)

Central in-memory registry for active device instances in the simulator.

In SCADA systems:
* This loosely represents the Gateway's runtime tag/device context
* Used to track active assets currently participating in the system

In this simulator:
* Stores instantiated Device objects during execution
* Acts as a shared state container between CLI and simulation loop
"""

devices = {}
