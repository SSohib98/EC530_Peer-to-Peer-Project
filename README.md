# EC530_Peer-to-Peer-Project

This is a hackathon project in which I created a chat system in python that allows people to communicate with each other in real time. It uses a server and client connection.

The function and features of this system are:
- Multiple clients can message on the same server. 
- Asynchronous send/receive using threading.
- All connected users recieve/see the messages on the server in real time. 
- Users can input any username to easily display who is messaging.
- Timestamps shown to all messages.
- The SQLite database logs all chat messages.

---------------------------------------------------------------
Guide to running this P2P system:

* You will need to have python3 installed, SQLite3 (built-in with python), and any terminal access *
---
1. Setting up the Server
    - Open a terminal and navigate to your project folder by running: cd "INSERT FILE PATH HERE"
    - Run: python server_connection.py

2. Setting upthe client connection
    - Open a new terminal and navigate to the same directory.
    - Run: python client_connection.py

3. Start Messaging
    - The client terminal will display: Enter your username
    - Enter any name and being chatting!
