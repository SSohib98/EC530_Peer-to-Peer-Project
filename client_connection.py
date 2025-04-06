import socket
import threading
import sys
from datetime import datetime
import json

# Ask for username
username = input("Enter your username: ")

# Server configuration
SERVER_IP = '127.0.0.1'
PORT = 56789

# To store received messages
chat_history = []

# Receive messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Parse the message data
            message_data = json.loads(message)
            sender = message_data["sender"]
            payload = message_data["payload"]["message"]
            timestamp = message_data["timestamp"]

            # Format the received message
            formatted_message = f"{sender} ({timestamp}): {payload}"

            # Append the new message to the chat history
            chat_history.append(formatted_message)

            # Print the new message
            print_new_message(formatted_message)

        except:
            break

# Print the new message
def print_new_message(message):
    print(message)

# Start client
def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))

        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        print("Connected to chat. Type your message and press Enter to send.")
        print("Type 'exit' to leave the chat.\n")

        while True:
            message = sys.stdin.readline().strip()
            if message.lower() == "exit":
                print("Disconnecting...")
                break

            # Display the message locally (client's own message)
            timestamp = datetime.now().isoformat()
            formatted_message = f"{username} ({timestamp}): {message}"

            # Append the message to the chat history
            chat_history.append(formatted_message)

            # Print the new message
            print_new_message(formatted_message)

            # Prepare the message to send to the server
            data = {
                "type": "chat",
                "sender": username,
                "timestamp": timestamp,
                "payload": {
                    "message": message
                }
            }

            # Send the message to the server
            client_socket.send(json.dumps(data).encode('utf-8'))

        client_socket.close()

    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")

if __name__ == "__main__":
    start_client()
