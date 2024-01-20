import socket

def start_client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 12345))
    clientsocket.send(bytes("1234", "utf-8"))
    
    # Receive and save the file
    with open('downloaded_file.txt', 'wb') as f:
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            f.write(data)

    print("File downloaded successfully.")

if __name__ == "__main__":
    start_client()