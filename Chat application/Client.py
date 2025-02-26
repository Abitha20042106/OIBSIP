import socket
import threading

# Client Configuration
HOST = '127.0.0.1'
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Server: {message}")
        except:
            print("Disconnected from server.")
            break

def send_messages():
    while True:
        message = input("You (Client): ")  # Client types a message
        client.send(message.encode("utf-8"))

# Start threads for receiving and sending messages
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
