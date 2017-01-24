import pygame
import sys
from SnakeGame import Game
pygame.init()

size = width, height = 480, 480
grid = colloms, rows = 20, 20
clock = pygame.time.Clock()
yellow = 255,255,0
black = 0, 0, 0
white = 255,255,255
basicfont = pygame.font.Font('freesansbold.ttf', 18)
displaysurf = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode(size)
hard = input("hard mode? type y/n").lower()
if hard == "y":
    hard = True
else:
    hard = False
game = Game(colloms,rows,width,height,hard)


def drawScore(score):
    scoreSurf = basicfont.render('Score: %s' % (score), True, white)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (width - 120, 10)
    displaysurf.blit(scoreSurf, scoreRect)

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    dt = clock.tick(60)/1000

    game.update(events, dt)

    if game.reset:
        game = Game(colloms,rows,width,height,hard)

    screen.fill(black)

    game.draw(screen)

    drawScore(game.score)

    pygame.display.flip()
