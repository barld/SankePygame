import pygame, sys

from game import *

pygame.init()
size = width, height = 800, 800
black = 0, 0, 0
myfont = pygame.font.SysFont("monospace", 25)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game = Game(20, 800)

while True:
    # limit frames at 120 fps
    dt = clock.tick(120) / 1000.0

    events = pygame.event.get()
    game.update(events, dt)

    for event in events:
        if event.type == pygame.QUIT: sys.exit()



    screen.fill(black)
    game.draw(screen)
    pygame.display.flip()