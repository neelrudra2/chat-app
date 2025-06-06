import socket
import threading

HOST = input("Enter server IP: ")
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print(f"[+] Connected to {HOST}:{PORT}")

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print(f"[Server]: {msg}")
        except:
            print("[!] Connection lost.")
            break

def send():
    while True:
        msg = input("")
        try:
            client.send(msg.encode())
        except:
            print("[!] Could not send.")
            break

recv_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

recv_thread.start()
send_thread.start()
