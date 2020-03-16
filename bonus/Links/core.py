import pygame
import constant

# pylint: disable=too-many-function-args
class Core():
    
    def __init__(self, friends, friendsLinks):
        super().__init__()
        self.window = pygame.display.set_mode(constant.WINDOW_SIZE)
        self.clock = pygame.time.Clock()

    def gameLoop(self):
        while True:
            self.clock.tick(constant.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.window.fill(constant.WHITE)
            pygame.display.update()


