# Distributed Process Communication Simulator

A beginner-friendly Python mini project that demonstrates the basic idea of **message passing** between four named processes (P1, P2, P3 and P4).

## Overview
The program defines four process inboxes, sends sample messages between them, stores each message in the receiver's inbox, and displays the received messages.

> **Scope note:** This is a local educational simulation of message passing. It does not create separate computers, operating-system processes, sockets, or real network communication.

## Objectives
- Understand the basic message-passing concept.
- Identify sender and receiver processes.
- Store messages in receiver inboxes.
- Display the communication flow.

## Technology
- Python 3
- No external libraries required

## Project structure
```text
Distributed-Process-Communication-Simulator/
├── main.py
├── README.md
├── sample_output.txt
└── Screenshots/
    └── sample_output.png
```

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Sample communication
- P1 → P2: Hello P2
- P2 → P3: Hello P3
- P3 → P4: Hello P4
- P4 → P1: Communication completed

See [`sample_output.txt`](sample_output.txt) and [`Screenshots/sample_output.png`](Screenshots/sample_output.png).

## Future improvements
- Add user input for sender, receiver and message.
- Add a graphical interface.
- Simulate message delays and delivery status.
- Extend the example to real network communication using sockets.

## Author
Add your name, department, college and academic year here before publishing.
