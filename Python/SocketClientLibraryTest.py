import socket
import sys
import threading

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    
    sock.connect((HOST, PORT))    
        # Receive data from the server and shut down
    def recvMsg():
        x = 1
        while (x==1):   
            received = str(sock.recv(1024), "utf-8")
            if not (received == ""):
                print(sock.getsockname(), ": ", received, sep="")
    def sendMsg():
        x = 1
        while (x==1):
            data = input("Me: ")
            sock.sendall(bytes(data + "\n", "utf-8"))

    recv_thread = threading.Thread(target=recvMsg)
    recv_thread.setDaemon(True)
    recv_thread.start()
    sendMsg()
print("Sent:     {}".format(data))
print("Received: {}".format(received))

