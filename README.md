# Mini SCADA Simulator

This Python CLI tool simulates a simplified SCADA-style system. It models core industrial concepts such as devices, real-time telemetry updates, alarm detection, and event logging.

The goal of this project is to better understand how SCADA systems operate at a conceptual level—especially how gateways manage tags, evaluate alarm conditions, and generate events in response to changing process data.

* [Get started](#get-started)
* [Requirements](#requirements)
* [Commands](#commands)
* [About the project](#about-the-project)

## Get started

To get started, clone the repository to your computer, then run the `main.py` file.

```bash
git clone <your-repo-url>
cd mini-scada-simulator
python main.py
```

> The project uses only Python standard libraries. No external dependencies are required.

## Requirements

- Python 3.11+

## Commands

Once the simulator is running, you can interact with it using the CLI.

| Commands                | Description                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------|
| help                    | Displays a list of all available commands and their descriptions.                                            |
| add id=<id> type=<type> | Creates a new device in the system with the specified ID and type.                                           |
| list                    | Lists all active devices registered in the system.                                                           |
| show id=<id>            | Displays the tag values for the specified device.                                                            |
| events id=<id>          | Displays recent events for the specified device.                                                             |
| simulate id=<id>        | Manually updates device values for testing purposes. The main simulation loop handles updates automatically. |
| exit                    | Exits the simulator.                                                                                         |

## Features

- Device models (e.g., pumps, tanks, motors)
- Simulated sensor data updates over time
- High/low alarm evaluation logic
- Centralized event store (SCADA-style event journal)
- CLI-based interface for interacting with the system
- Real-time simulation loop (threaded execution)

## About the project

### Learning approach

This project was built as an iterative learning exercise with the assistance of a large language model (LLM).

The LLM was used as:
- A pair-programming and tutoring tool
- A way to explore SCADA concepts step-by-step
- A debugging and architecture discussion aid

All implementation decisions, understanding, and refinements were made interactively during the learning process.

### Goals

- Understand SCADA gateway architecture concepts
- Learn event-driven system design
- Implement alarm logic (HIGH / LOW conditions)
- Practice modular Python design
- Explore simulation-based system behavior

### Conceptual mapping

| Simulator component | SCADA concept                         |
|---------------------|---------------------------------------|
| Device class        | PLC / RTU / Asset                     |
| Tags                | Process variables                     |
| Simulation loop     | Telemetry updates from field devices  |
| Alarm logic         | Gateway alarm evaluation              |
| Event store         | Event journal / historian buffer      |
