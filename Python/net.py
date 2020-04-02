import socket


def Main():
    # server
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)

    # receiving request from client
    content, addr = s.accept()
    print("Connection innitiated from: ", str(addr))
    while True:
        data = str(content.recv(1024).decode('utf-8'))
        if not data:
            break
        print("From connected user: ", data)

        # processing received data @ server
        data = data.upper()
        print("sending: good day to you!", data)

        # send to client
        content.send(data.encode('utf-8'))
    content.close()


if __name__ == "__main__":
    Main()
