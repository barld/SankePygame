import pygame
import sys

from SnakeGame import Game

pygame.init()

size = width, height = 500, 500

black = 0,0,0
screen = pygame.display.set_mode(size)

game = Game(20,20,500,500)
clock = pygame.time.Clock()

while True:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    dt = clock.tick(120) / 1000.0

    game.update(events, dt)

    screen.fill(black)

    game.draw(screen)

    pygame.display.flip()