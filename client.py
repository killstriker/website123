import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(("localhost", 9999))

# Receive and decode the initial message
message = client.recv(1024).decode()

# Send user input as a response to the initial message
client.send(input(message).encode())

# Receive and decode the next message
message = client.recv(1024).decode()

# Send user input as a response to the next message
client.send(input(message).encode())

# Receive and decode the final message
print(client.recv(1024).decode())
