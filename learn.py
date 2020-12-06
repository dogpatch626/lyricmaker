# import os
# os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame, sys 
pygame.init()
# pygame.display.init()
# pygame.font.init()
# pygame.get.init()
win = pygame.display.set_mode((600,600))

pygame.display.set_caption("Game")

x = 50
y = 50

width = 40
height = 60
vel = 5

run = True
while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False

pygame.quit()