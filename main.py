# Distributed Process Communication Simulator
# A simple message-passing simulation using Python dictionaries and queues.

processes = {
    "P1": [],
    "P2": [],
    "P3": [],
    "P4": []
}

messages = [
    ("P1", "P2", "Hello P2"),
    ("P2", "P3", "Hello P3"),
    ("P3", "P4", "Hello P4"),
    ("P4", "P1", "Communication completed")
]

print("DISTRIBUTED PROCESS COMMUNICATION SIMULATOR")
print("-" * 45)

for sender, receiver, message in messages:
    print(f"{sender} sends a message to {receiver}: {message}")
    processes[receiver].append((sender, message))

print("\nMESSAGE RECEIVING")
print("-" * 45)

for receiver, inbox in processes.items():
    for sender, message in inbox:
        print(f"{receiver} received from {sender}: {message}")

print("\nCommunication completed successfully.")
