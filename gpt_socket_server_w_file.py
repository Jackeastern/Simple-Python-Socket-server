"""This is GPT code. I asked it to allow the socket server to send a file."""

import socket

def start_server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 12345))
    serversocket.listen(5) # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if len(buf) > 0:
            print(f"Received connection from {address}")
            if buf.decode("utf-8") == "1234":
                print("Passcode accepted")
                connection.send(bytes("Hello", "utf-8"))
                
                # Send a file (Orginal was yourfile.txt| I changed it to this_test_file)
                with open('this_test_file.txt', 'rb') as f: 
                    while True:
                        data = f.read(1024)
                        if not data:
                            break
                        connection.sendall(data)
                
            else:
                print("Incorrect passcode")
                connection.send(bytes("Incorrect passcode", "utf-8"))
            connection.close()

if __name__ == "__main__":
    start_server()