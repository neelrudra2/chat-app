# Peer-to-Peer Chat App using TCP

A real-time terminal-based chat application using Python’s socket programming and threading. This project demonstrates basic networking concepts and allows two users to communicate over a local network or localhost using TCP sockets.

## 🚀 Features

- Full-duplex communication (send and receive at the same time)
- TCP-based reliable transmission
- Console-based real-time chat
- Threaded I/O for non-blocking experience
- Works on LAN and localhost

## ⚙️ How to Run

### On the Same Machine (Localhost)

1. Open two terminals.
2. In Terminal 1, run the server:
   ```bash
   python server.py
   ```
3. In Terminal 2, run the client:
   ```bash
   python client.py
   ```
4. Enter 127.0.0.1 as the server IP when prompted.
5. Start chatting from both terminals.

## 🧠 Concepts Used

1. TCP socket programming
2. Client-server model
3. Multithreading for send/receive concurrency
4. IP addressing and port management

## 📚 Technologies

1. Python
2. Socket
3. Threading
