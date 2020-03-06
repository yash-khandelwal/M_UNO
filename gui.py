import pygame
import cards
import player
pygame.font.init()


class GUI:
    def __init__(self, win):
        self.counts = [-1, -1, -1, -1]
        self.demo_card = cards.Card('blank', 'start', 'images/back.png')
        self.draw_card = cards.Card('blank', 'start', 'images/back.png')
        self.cards = []
        self.top_card = cards.Card('blank', 'start', 'images/back.png')
        self.back_ground = pygame.image.load('images/back_ground.png')
        self.win = win


    def update(self):
        self.win.fill((255, 255, 255))
        self.win.blit(pygame.image.load(self.top_card.image_path), (250, 125))      # top_card
        self.win.blit(pygame.image.load(self.draw_card.image_path), (170, 125))     # draw_card
        self.win.blit(pygame.image.load(self.demo_card.image_path), (100, 125))     # player 1
        self.win.blit(pygame.image.load(self.demo_card.image_path), (225, 0))       # player 2
        self.win.blit(pygame.image.load(self.demo_card.image_path), (320, 125))     # player 3
        adder = 0
        for crd in self.cards:
            # print(self.cards[itr])
            self.win.blit(pygame.image.load(crd.image_path), (50 + 40*adder, 250))
            adder += 1
        font = pygame.font.SysFont("comicsans", 80)
        text1 = font.render(str(self.counts[1]), 1, (255, 255, 255))
        self.win.blit(text1, (110, 135))
        text2 = font.render(str(self.counts[2]), 1, (255, 255, 255))
        self.win.blit(text2, (235, 10))
        text3 = font.render(str(self.counts[3]), 1, (255, 255, 255))
        self.win.blit(text3, (330, 135))
        pygame.display.update()
