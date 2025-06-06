import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[+] Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[+] Connected by {addr}")

def receive():
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                print(f"[Client]: {msg}")
        except:
            print("[!] Connection closed.")
            break

def send():
    while True:
        msg = input("")
        try:
            conn.send(msg.encode())
        except:
            print("[!] Could not send message.")
            break

recv_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

recv_thread.start()
send_thread.start()
