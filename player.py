import pickle

# player class for server side
class SPlayer:
    def __init__(self, id, cards, addr, conn):
        self.id = id
        self.cards = cards
        self.ready = False
        self.addr = addr
        self.conn = conn
        self.count = len(cards)

    def __str__(self):
        return 'Server player with id ' + self.id

    def receiveFun(self):
        k = pickle.loads(self.conn.recv(20))
        return pickle.loads(self.conn.recv(int(k)))

    def sendFun(self, data):
        print('sending : ', data)
        data = pickle.dumps(data)
        k = f'{len(data):<10}'
        k = pickle.dumps(k)
        self.conn.send(k)
        self.conn.send(data)
        print('sent : ', pickle.loads(data))

    # def send(self, data):
    #     self.conn.send(data.encode())
    #     print("sending - " + str(data) + " to player " + str(self.id))
    #
    # def receive(self, size):
    #     received_data = self.conn.recv(size).decode()
    #     print("received - " + str(received_data) + " from player " + str(self.id))


# player class for client side
class CPlayer:
    def __init__(self, id, cards):
        self.id = id
        self.cards = cards
        self.count = len(cards)

    def __str__(self):
        return 'Client player with id ' + self.id
