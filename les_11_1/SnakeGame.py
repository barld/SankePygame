import pygame
import random


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_same(self, v2):
        return self.x == v2.x and self.y == v2.y

class Snake:
    def __init__(self, pos:Vector2, tail=None):
        self.pos = pos
        self.tail = tail

    def take(self, n):
        if n == 0:
            return None
        else:
            return Snake(self.pos, self.tail.take(n-1) if self.tail is not None else None)

    def draw(self, screen, cSize, rSize):
        pygame.draw.rect(screen, (0, 255, 0), [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
        if self.tail is not None:
            self.tail.draw(screen,cSize,rSize)

class Game:
    def __init__(self, colloms, rows, width, height):
        self.snake = Snake(Vector2(10,10))
        self.colloms = colloms
        self.rows = rows
        self.setfood()
        self.width = width
        self.height = height
        self.speed = 0.5
        self.cooldown = self.speed

        self.direction = pygame.K_UP
        self.length = 1



    def draw(self, screen):
        cSize = self.width//self.colloms
        rSize = self.height//self.rows

        self.snake.draw(screen,cSize,rSize)
        pygame.draw.rect(screen, (0,0,255), [self.food.x * cSize, self.food.y * rSize, cSize-2, rSize-2])


    def update(self, events, dt):
        self.cooldown = self.cooldown - dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction = pygame.K_UP
        elif keys[pygame.K_RIGHT]:
            self.direction = pygame.K_RIGHT
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.K_DOWN
        elif keys[pygame.K_LEFT]:
            self.direction = pygame.K_LEFT

        if self.cooldown < 0.0:

            if self.direction == pygame.K_UP:
                newpos = Vector2(self.snake.pos.x, self.snake.pos.y - 1)
            elif self.direction == pygame.K_RIGHT:
                newpos = Vector2(self.snake.pos.x+1, self.snake.pos.y)
            elif self.direction == pygame.K_DOWN:
                newpos = Vector2(self.snake.pos.x, self.snake.pos.y + 1)
            else:
                newpos = Vector2(self.snake.pos.x-1, self.snake.pos.y)
            self.snake = Snake(newpos, self.snake)
            self.snake = self.snake.take(self.length)

            self.cooldown = self.speed

            if self.snake.pos.is_same(self.food):
                self.length += 1
                snake = Snake(self.food, self.snake)
                self.setfood()

    def setfood(self):
        self.food = Vector2(random.randint(0,self.rows-1), random.randint(0,self.colloms-1))
