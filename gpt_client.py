"""This code was also written by GPT after asking to connect to the server """
import socket

def start_client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 12345))
    clientsocket.send(bytes("1234", "utf-8"))
    buf = clientsocket.recv(64)
    if len(buf) > 0:
        print(buf.decode("utf-8"))

if __name__ == "__main__":
    start_client()