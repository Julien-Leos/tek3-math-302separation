import pygame
import textwrap
import constant

# pylint: disable=too-many-function-args
class Card:
    name = ""
    card = None
    texts = []
    textRects = []
    isReturn = True
    pos = []

    def __init__(self, core, name, pos):
        self.core = core
        self.name = name
        self.pos = pos
        
        self.create()

    def create(self):
        self.card = pygame.Surface(constant.CARD_SIZE)
        self.card.fill(constant.BLUE)
        wrapedText = textwrap.wrap(self.name, constant.MAX_CARD_CHAR)
        for (index, text) in enumerate(wrapedText):
            self.texts.append(self.core.font.render(text, True, constant.WHITE))
            self.textRects.append(self.texts[-1].get_rect())
            self.textRects[-1].center = (self.pos[0] + constant.CARD_WIDTH / 2, (self.pos[1] + constant.CARD_HEIGHT / 2) + ((index - len(wrapedText) / 2 + 1) * constant.FONT_SIZE) + ((index - len(wrapedText) / 2 + 1) * constant.GAP_BETWEEN_LINES))            
