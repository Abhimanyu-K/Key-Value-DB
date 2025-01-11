import socket


class SocketHandler:
    def __init__(self, host='127.0.0.1', port=63632):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, command_handler):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        communication_socket, address = self.server_socket.accept()
        with communication_socket:
            print(f"communication_socket connected by {address}")
            while True:
                data = communication_socket.recv(1024).decode('utf-8')

                if not data:
                    break

                value = command_handler(data)
                print(value)
                if value:
                    communication_socket.send(
                        bytes(f"${len(str(value))}\r\n{value}\r\n", "utf-8"))
                else:
                    communication_socket.send('+OK\r\n'.encode())
