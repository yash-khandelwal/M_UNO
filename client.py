import pygame
import player
import network
import time
import _thread
import cards
import gui

pygame.font.init()
# important fields to display
top_card = cards.Card('blank', 'start', 'images/back.png')
draw_card = (100, 100, 150, 100)
counts = [7, 7, 7, 7]

clicked = False

def throwCard():
    global clicked
    print("throwCard() started")
    font = pygame.font.SysFont("comicsans", 60)
    text = font.render('PLEASE THROW A CARD', 1, (0, 255, 0))
    global pos
    for i in range(60):
        clock.tick(60)
        win.blit(text, (0, 0))
        g.update()
    thrown = False
    draw = False
    global run
    thrown_card = cards.Card('blank', 'start', 'images/back.png')
    while not (thrown or draw):
        # print("while not thrown started")
        while not clicked:
            time.sleep(0.5)
            print("click the suitable card")
        if 250 <= pos[1] <= 350:
            for t in range(len(g.cards)):
                if 50 + t * 40 <= pos[0] < 50 + (t + 1) * 40:
                    thrown_card = g.cards[t]
                    n.sendFun('CARD')
                    player.cards = player.cards[0:t] + player.cards[t + 1:len(player.cards)]
                    g.cards = g.cards[0:t] + g.cards[t + 1:len(g.cards)]
                    print("selected card is :")
                    print(thrown_card)
                    thrown = True
                    break

        elif 125 <= pos[1] <= 200:
            if 170 <= pos[0] <= 220:
                print("chose to draw a card")
                n.sendFun('GIVE_')
                draw = True
    if thrown:
        n.sendFun(thrown_card)

    elif draw:
        rec_card = n.receiveFun()
        player.cards.append(rec_card)
        player.count += 1
    clicked = False
    print("thrownCard() method fully executed")


def updateState():
    global top_card, counts
    top_card = n.receiveFun()
    print("top_card = ")
    print(top_card)
    counts = n.receiveFun()
    print(*counts)
    g.top_card = top_card
    itr = player.id
    itr = (itr + 1) % 4
    c = 1
    g.cards = player.cards
    while itr != player.id:
        g.counts[c] = counts[itr]
        itr += 1
        itr %= 4
        c += 1
    print("updateState() fully executed")


def receiveCards():
    print("receiveCard() Method started")
    extra_cards = n.receiveFun()
    print(extra_cards)
    for rc in extra_cards:
        player.cards.append(rc)
        # g.cards.append(rc)


def gameEnd():
    result = n.receiveFun()
    print(result)


def colorChange():
    pass


def errorHandler():
    pass


n = network.Network()
crds = []
try:
    crds = n.receiveFun()
except:
    print("ERROR in RECEIVING CRDS")
player = player.CPlayer(n.id, crds)
for card in player.cards:
    print(card)

win = pygame.display.set_mode((500, 400))
g = gui.GUI(win)
win.fill((255, 255, 255))
pygame.display.set_caption('Player ' + str(player.id))
# image = pygame.image.load(player.cards[0].image_path)
# win.blit(image, (100, 100))
g.update()

keys = pygame.key.get_pressed()

run = True
i = 0


def getServerMessage():
    game_running = True
    while game_running:
        message = n.receiveFun()
        print(message)
        if message == 'TURN_':
            throwCard()
        elif message == 'STATE':
            updateState()
        elif message == 'GET__':
            receiveCards()
        elif message == 'END__':
            gameEnd()
            global run
            run = False
            break
        elif message == 'REPLY':
            colorChange()
        elif message == 'ERROR':
            game_running = False
            errorHandler()

        # global i, image
        # i += 1
        # image = pygame.image.load(player.cards[i].image_path)
        # # image = pygame.transform.scale(image, (50 + i, 80 + i))
        # if i >= 6:
        #     i = 0


pos = [0, 0]
_thread.start_new_thread(getServerMessage, ())
clock = pygame.time.Clock()
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse clicked")
            clicked = True
            pos = pygame.mouse.get_pos()
            print(*pos)
    # win.fill((255, 255, 255))
    # win.blit(image, (100, 100))
    # pygame.display.update()
    g.update()
