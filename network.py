import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "<your wifi adapter ipv4>"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = -1
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.id = self.receiveFun()
            self.id = int(self.id)
            print(self.id)
            self.sendFun('READY')
        except:
            print('error')

    def receiveFun(self):
        k = pickle.loads(self.client.recv(20))
        return pickle.loads(self.client.recv(int(k)))

    def sendFun(self, data):
        print('sending : ', data)
        data = pickle.dumps(data)
        k = f'{len(data):<10}'
        k = pickle.dumps(k)
        self.client.send(k)
        self.client.send(data)
        print('sent : ', pickle.loads(data))
