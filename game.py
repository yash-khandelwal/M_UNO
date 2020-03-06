from logging import Logger

import server
import cards
import random
import player
import pickle
import _thread
import time


class Game:
    def __init__(self, d_ip, d_port):
        self.dealer = server.Server(d_ip, d_port)
        self.deck = [cards.Card('blue', '0', 'images/blue_0.png'), cards.Card('blue', '0', 'images/blue_0.png'),
                     cards.Card('blue', '1', 'images/blue_1.png'), cards.Card('blue', '1', 'images/blue_1.png'),
                     cards.Card('blue', '2', 'images/blue_2.png'), cards.Card('blue', '2', 'images/blue_2.png'),
                     cards.Card('blue', '3', 'images/blue_3.png'), cards.Card('blue', '3', 'images/blue_3.png'),
                     cards.Card('blue', '4', 'images/blue_4.png'), cards.Card('blue', '4', 'images/blue_4.png'),
                     cards.Card('blue', '5', 'images/blue_5.png'), cards.Card('blue', '5', 'images/blue_5.png'),
                     cards.Card('blue', '6', 'images/blue_6.png'), cards.Card('blue', '6', 'images/blue_6.png'),
                     cards.Card('blue', '7', 'images/blue_7.png'), cards.Card('blue', '7', 'images/blue_7.png'),
                     cards.Card('blue', '8', 'images/blue_8.png'), cards.Card('blue', '8', 'images/blue_8.png'),
                     cards.Card('blue', '9', 'images/blue_9.png'), cards.Card('blue', '9', 'images/blue_9.png'),
                     cards.Card('blue', '+2', 'images/blue_+2.png'), cards.Card('blue', '+2', 'images/blue_+2.png'),
                     cards.Card('blue', 'skip', 'images/blue_skip.png'),
                     cards.Card('blue', 'skip', 'images/blue_skip.png'),
                     cards.Card('blue', 'reverse', 'images/blue_reverse.png'),
                     cards.Card('blue', 'reverse', 'images/blue_reverse.png'),
                     cards.Card('green', '0', 'images/green_0.png'), cards.Card('green', '0', 'images/green_0.png'),
                     cards.Card('green', '1', 'images/green_1.png'), cards.Card('green', '1', 'images/green_1.png'),
                     cards.Card('green', '2', 'images/green_2.png'), cards.Card('green', '2', 'images/green_2.png'),
                     cards.Card('green', '3', 'images/green_3.png'), cards.Card('green', '3', 'images/green_3.png'),
                     cards.Card('green', '4', 'images/green_4.png'), cards.Card('green', '4', 'images/green_4.png'),
                     cards.Card('green', '5', 'images/green_5.png'), cards.Card('green', '5', 'images/green_5.png'),
                     cards.Card('green', '6', 'images/green_6.png'), cards.Card('green', '6', 'images/green_6.png'),
                     cards.Card('green', '7', 'images/green_7.png'), cards.Card('green', '7', 'images/green_7.png'),
                     cards.Card('green', '8', 'images/green_8.png'), cards.Card('green', '8', 'images/green_8.png'),
                     cards.Card('green', '9', 'images/green_9.png'), cards.Card('green', '9', 'images/green_9.png'),
                     cards.Card('green', '+2', 'images/green_+2.png'), cards.Card('green', '+2', 'images/green_+2.png'),
                     cards.Card('green', 'skip', 'images/green_skip.png'),
                     cards.Card('green', 'skip', 'images/green_skip.png'),
                     cards.Card('green', 'reverse', 'images/green_reverse.png'),
                     cards.Card('green', 'reverse', 'images/green_reverse.png'),
                     cards.Card('red', '0', 'images/red_0.png'), cards.Card('red', '0', 'images/red_0.png'),
                     cards.Card('red', '1', 'images/red_1.png'), cards.Card('red', '1', 'images/red_1.png'),
                     cards.Card('red', '2', 'images/red_2.png'), cards.Card('red', '2', 'images/red_2.png'),
                     cards.Card('red', '3', 'images/red_3.png'), cards.Card('red', '3', 'images/red_3.png'),
                     cards.Card('red', '4', 'images/red_4.png'), cards.Card('red', '4', 'images/red_4.png'),
                     cards.Card('red', '5', 'images/red_5.png'), cards.Card('red', '5', 'images/red_5.png'),
                     cards.Card('red', '6', 'images/red_6.png'), cards.Card('red', '6', 'images/red_6.png'),
                     cards.Card('red', '7', 'images/red_7.png'), cards.Card('red', '7', 'images/red_7.png'),
                     cards.Card('red', '8', 'images/red_8.png'), cards.Card('red', '8', 'images/red_8.png'),
                     cards.Card('red', '9', 'images/red_9.png'), cards.Card('red', '9', 'images/red_9.png'),
                     cards.Card('red', '+2', 'images/red_+2.png'), cards.Card('red', '+2', 'images/red_+2.png'),
                     cards.Card('red', 'skip', 'images/red_skip.png'), cards.Card('red', 'skip', 'images/red_skip.png'),
                     cards.Card('red', 'reverse', 'images/red_reverse.png'),
                     cards.Card('red', 'reverse', 'images/red_reverse.png'),
                     cards.Card('yellow', '0', 'images/yellow_0.png'), cards.Card('yellow', '0', 'images/yellow_0.png'),
                     cards.Card('yellow', '1', 'images/yellow_1.png'), cards.Card('yellow', '1', 'images/yellow_1.png'),
                     cards.Card('yellow', '2', 'images/yellow_2.png'), cards.Card('yellow', '2', 'images/yellow_2.png'),
                     cards.Card('yellow', '3', 'images/yellow_3.png'), cards.Card('yellow', '3', 'images/yellow_3.png'),
                     cards.Card('yellow', '4', 'images/yellow_4.png'), cards.Card('yellow', '4', 'images/yellow_4.png'),
                     cards.Card('yellow', '5', 'images/yellow_5.png'), cards.Card('yellow', '5', 'images/yellow_5.png'),
                     cards.Card('yellow', '6', 'images/yellow_6.png'), cards.Card('yellow', '6', 'images/yellow_6.png'),
                     cards.Card('yellow', '7', 'images/yellow_7.png'), cards.Card('yellow', '7', 'images/yellow_7.png'),
                     cards.Card('yellow', '8', 'images/yellow_8.png'), cards.Card('yellow', '8', 'images/yellow_8.png'),
                     cards.Card('yellow', '9', 'images/yellow_9.png'), cards.Card('yellow', '9', 'images/yellow_9.png'),
                     cards.Card('yellow', '+2', 'images/yellow_+2.png'),
                     cards.Card('yellow', '+2', 'images/yellow_+2.png'),
                     cards.Card('yellow', 'skip', 'images/yellow_skip.png'),
                     cards.Card('yellow', 'skip', 'images/yellow_skip.png'),
                     cards.Card('yellow', 'reverse', 'images/yellow_reverse.png'),
                     cards.Card('yellow', 'reverse', 'images/yellow_reverse.png'),
                     cards.Card('wild', '+4', 'images/black_+4.png'), cards.Card('wild', '+4', 'images/black_+4.png'),
                     cards.Card('wild', 'color_change', 'images/black_wildcard.png'),
                     cards.Card('wild', 'color_change', 'images/black_wildcard.png')
                     ]
        self.id = 0
        self.cards_remaining = 108
        self.counts = []
        self.players = []
        self.direction = 1
        self.top_card = cards.Card('blank', 'start', 'images/back.png')
        self.top_color = 'black'

    def shuffleDeck(self):
        """
        :do: shuffles the deck of the dealer
        :return:
        """
        random.shuffle(self.deck)

    def giveCard(self, player, n):
        """
        :do: pass the cards to the player
        :param player: SPlayer instance
        :param n: number of cards to give
        :return:
        """
        pass_cards = self.deck[0: n]
        self.deck = self.deck[n: self.cards_remaining]
        self.cards_remaining -= n
        player.sendFun(pass_cards)
        for pc in pass_cards:
            player.cards.append(pc)
        player.count += n

    def distributeCards(self):
        """
        :do: when game starts this function will return 7 cards list to pass to player class
        :return: return 7 cards list to pass to player class
        """
        pass_cards = self.deck[0: 7]
        self.deck = self.deck[7: self.cards_remaining]
        self.cards_remaining -= 7
        return pass_cards

    def create_room(self):

        """
        :do: creates room for four clients to connect to the server
        :return:
        """
        count = 0
        while count < 4:
            try:
                conn, addr = self.dealer.socket.accept()
                print(conn)
                print('Connected to:', addr)
                _thread.start_new_thread(self.client_thread, (conn, addr,))
            except:
                print('ERROR in connecting')

            count += 1

    def client_thread(self, conn, addr):

        """
        :do: its a new thread created function which called upon receiving connection request.
            - it creates new object of SPlayer and assign them different attributes
        :param conn: connection object to the client
        :param addr: address of the client
        :return:
        """
        # creating new player instance
        new_player = player.SPlayer(self.id, self.distributeCards(), addr, conn)
        # appending new player instance to the payers list at server
        self.players.append(new_player)
        self.players[-1].sendFun(str(self.id))
        # receiving the ack that client is ready
        ack = self.players[-1].receiveFun()
        if ack == 'READY':
            self.players[self.id].ready = True
        else:
            print("Connection Lost from the client with id: ", self.id)
            return
        self.players[-1].sendFun(self.players[self.id].cards)
        self.counts.append(int(7))
        print(*self.counts)
        print('Connection and communication both established with client: ', self.id)
        print(*self.players[self.id].cards)
        self.id += 1

    def validate(self, player, rec_card):

        """
        :do: validates the card thrown by player by verifying it with records and top_card
        :param player: SPlayer object
        :param rec_card: Card object
        :return:
        """
        find = False
        valid = False
        pos = -1
        for itr in range(player.count):
            # print(player.cards[itr])
            if str(player.cards[itr]) == str(rec_card):
                print("validate -> for itr -> if ==")
                find = True
                pos = itr
                break
        if self.top_card.mark == rec_card.mark or self.top_color == rec_card.color or rec_card.color == 'wild' or self.top_color == 'wild':
            print("validate -> if or")
            valid = True
        if find and valid:
            print("validate -> if and")
            player.cards.pop(pos)
            player.count -= 1
            self.top_color = rec_card.color
            return True
        else:
            print("validate -> else and")
            return False

    def countUpdate(self):
        pass

    def checkWin(self):
        winner = -1
        for itr in range(len(self.players)):
            if len(self.players[itr].cards) == 0:
                winner = itr
                break
        return winner

    def fun_card(self):
        pass

    def sendState(self, player):
        try:
            player.sendFun(self.top_card)
        except:
            print("ERROR in sending state 1 of the game")
        time.sleep(0.5)
        try:
            player.sendFun(self.counts)
            # print(len(pickle.dumps(self.counts)))
            # print(pickle.loads(pickle.dumps(self.counts)))
        except:
            print("ERROR in sending state 2 of the game")


game = Game('100.113.173.249', 5555)
game.shuffleDeck()
game.create_room()
run = True
i = 0
game.top_card = game.deck[0]
game.top_color = game.top_card.color
game.deck = game.deck[1: game.cards_remaining]
game.cards_remaining -= 1

while run:
    # time.sleep(0.1)
    print('_'*150)
    print(' '*50 , i)
    j = 0
    while j < 4:
        print("Sending state to Client: ", j)
        try:
            game.players[j].sendFun("STATE")
            print("'STATE' message sent")
            game.sendState(game.players[j])
        except:
            print("ERROR in sending message 'STATE' to player: " + str(game.players[j].id))
        # time.sleep(0.5)
        j += 1

    print("sending message to Client: ", i)
    try:
        game.players[i].sendFun('TURN_')
    except:
        print("ERROR in sending message 'TURN' to player: " + str(game.players[i].id))

    reply = ''
    try:
        reply = game.players[i].receiveFun()
        print("TURN reply received: ", reply)
    except:
        print("ERROR in RECEIVING TURN REPLY from player: " + str(game.players[i].id))

    time.sleep(1)

    if reply == 'CARD':
        rec_card = cards.Card('blank', 'start', 'images/back.png')
        try:
            rec_card = game.players[i].receiveFun()
            print("Received Card is: ", rec_card)
        except:
            print("ERROR in RECEIVING CARD OBJECT from player: " + str(game.players[i].id))
        is_valid = game.validate(game.players[i], rec_card)
        if is_valid:
            print("Valid card was received")
            game.top_card = rec_card
            game.counts[i] -= 1
            winner = game.checkWin()
            if winner != -1:
                # someone won
                for itr in range(4):
                    game.players[itr].sendFun('END__')
                    time.sleep(1)
                    if itr == winner:
                        game.players[itr].sendFun('WON__')
                    else:
                        game.players[itr].sendFun('LOSS_')
                run = False
            else:
                # no one won game carried onn
                # below is the code for various cards operations
                if rec_card.mark == '+2':
                    # give 2 cards to the next player
                    i += game.direction + 4
                    i %= 4
                    game.players[i].sendFun('GET__')
                    game.giveCard(game.players[i], 2)
                    game.counts[i] += 2

                elif rec_card.mark == '+4':
                    # give 4 cards to the next player
                    i += game.direction + 4
                    i %= 4
                    game.players[i].sendFun('GET__')
                    game.giveCard(game.players[i], 4)
                    game.counts[i] += 4

                elif rec_card.mark == 'skip':
                    # skip the chance of next player
                    i += game.direction + 4
                    i %= 4

                elif rec_card.mark == 'reverse':
                    # reverse the turns direction
                    game.direction = (-1) * game.direction

                elif rec_card.mark == 'color_change':
                    # change the color for the turns
                    # color = game.players[i].receiveFun()
                    # game.top_color = color
                    pass

        else:
            # invalid card was received
            print("Invalid Card was received ")
            while j < 4:
                try:
                    game.players[i].sendFun('ERROR')
                except:
                    print("ERROR in sending message 'ERROR' to player: " + str(game.players[j].id))
                j += 1
            pass

    elif reply == 'GIVE_':
        pc = game.deck[0]
        game.deck = game.deck[1: game.cards_remaining]
        game.cards_remaining -= 1
        game.players[i].sendFun(pc)
        game.counts[i] += 1

    i = (i + game.direction + 4) % 4
