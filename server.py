import socket

class Server:

    def __init__(self, s_ip, port):
        self.s_ip = s_ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind()
        self.listen(4)

    def bind(self):
        try:
            self.socket.bind((self.s_ip, self.port))
            print('Server bind successfully')
        except:
            print("ERROR in binding")

    def listen(self, n):
        try:
            self.socket.listen(n)
            print('Server listening ...')
        except:
            print("ERROR in listening")
