# Mini SCADA simulator

This Python CLI tool simulates a simplified SCADA (Supervisory Control and Data Acquisition) system. It models core industrial concepts such as devices, real-time telemetry updates, alarm detection, and event logging.

The goal of this project is to better understand how SCADA systems operate at a conceptual level. For example, how gateways manage tags, evaluate alarm conditions, and generate events in response to changing process data.

* [Get started](#get-started)
* [Requirements](#requirements)
* [Commands](#commands)
* [Command examples](#command-examples)
* [About the project](#about-the-project)

## Get started

To get started, clone the repository to your computer, then run the `main.py` file.

```bash
git clone <your-repo-url>
cd mini-scada-simulator
python main.py
```

## Requirements

- Python 3.11+

> The project uses only Python standard libraries. No external dependencies are required.

## Commands

Once the simulator is running, you can interact with it using the CLI.

| Commands | Description                                                                                             |
|----------|---------------------------------------------------------------------------------------------------------|
| help     | Displays a list of all available commands and their descriptions.                                       |
| add      | Creates a new device. Requires an ID and a type (`tank`, `pump`, `motor`).                              |
| list     | Lists all active devices currently registered in the system.                                            |
| show     | Displays the current tag values for a device. Requires a device ID.                                     |
| events   | Displays recent events for a device. Requires a device ID.                                              |
| simulate | Manually updates device values for testing purposes. The simulator automatically updates device values. |
| exit     | Exits the simulator.                                                                                    |                                                                                     |

To learn more, see [usage examples](#command-examples).

## Command examples

Use the following examples to learn how to use the simulator.

### Add a device

Create a tank device with default tags and alarm configuration.

```bash
add id=tank-01 type=tank
```

### List devices

Display all currently registered devices in the system.

```bash
USER: list
```

### Show device tags

Display the current live tag values (for example: level, temperature, status).

Device tags are defined per device in `device_types.py` in the `TEMPLATES` configuration.

```bash
show id=tank-01
```

### View events

Display recent alarm and system events for the specified device.

Alarm thresholds are defined per device type in `device_types.py` in the `ALARMS` configuration. Events are only generated when a value crosses a defined threshold.

```bash
events id=tank-01
```

### Simulate

Manually trigger a single simulation for a device. This calls the device’s update logic once, updating tag values and evaluating alarms.

This is mainly used for testing and debugging. Normally, the background update process handles continuous updates automatically.


```bash
simulate id=tank-01
```

### Exit the simulator

Stop the program and exit the CLI.

```bash
exit
```

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
