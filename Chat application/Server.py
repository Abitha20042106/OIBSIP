import socket
import threading

# Server Configuration
HOST = '127.0.0.1'
PORT = 5001

def receive_messages(client_socket):
    """Handles receiving messages from the client."""
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Client: {message}")
        except:
            print("Client disconnected.")
            break

def send_messages(client_socket):
    
    while True:
        message = input("You (Server):\n ")  # Server types a message
        client_socket.send(message.encode("utf-8"))

def handle_client(client_socket):
        threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket,)).start()

def start_server():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Server is running... Waiting for client connection...")

    client_socket, addr = server.accept()
    print(f"Connected with {addr}")

    handle_client(client_socket)

if __name__ == "__main__":
    start_server()
