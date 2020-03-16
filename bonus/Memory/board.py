import constant

import card

class Board:
    friends = []
    friendsLinks = []
    cards = []

    def __init__(self, core, friends, friendsLinks):
        self.core = core
        self.friends = friends
        self.friendsLinks = friendsLinks

        self.createCards()
    
    def createCards(self):
        x = 0
        y = 0
        for friend in self.friends:
            self.cards.append(card.Card(self.core, friend, (x * (constant.CARD_WIDTH + constant.CARD_MARGIN) + constant.CARD_MARGIN, y * (constant.CARD_HEIGHT + constant.CARD_MARGIN) + constant.CARD_MARGIN)))
            x += 1
            if x == constant.NB_CARD_PER_LINE:
                x = 0
                y += 1

    def detectCardClick(self):
        if self.core.mouse[0] < 0 or self.core.mouse[0] > constant.BOARD_WIDTH \
        or self.core.mouse[1] < 0 or self.core.mouse[1] > constant.BOARD_HEIGHT:
            return
        
        for card in self.cards:
            if self.core.mouse[0] 

        print(self.core.mouse)

