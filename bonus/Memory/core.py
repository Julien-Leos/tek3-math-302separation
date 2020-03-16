import pygame
import constant

import board

# pylint: disable=too-many-function-args
class Core():
    window = None
    clock = None
    font = None
    mouse = []

    board = None

    def __init__(self, friends, friendsLinks):
        pygame.init()
        self.window = pygame.display.set_mode(constant.WINDOW_SIZE)
        pygame.display.set_caption('Memory Link') 
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', constant.FONT_SIZE)

        self.board = board.Board(self, friends, friendsLinks)

    def gameLoop(self):
        while True:
            self.clock.tick(constant.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse = pygame.mouse.get_pos()
                    self.board.detectCardClick()

            self.window.fill(constant.WHITE)
            self.draw()
            pygame.display.update()

    def draw(self):
        for card in self.board.cards:
            self.window.blit(card.card, card.pos)
            if card.isReturn == True:
                for index in range(len(card.texts)):
                    self.window.blit(card.texts[index], card.textRects[index])
