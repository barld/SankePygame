import pygame
import random


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_same(self, v2):
        return self.x == v2.x and self.y == v2.y


class Snake:
    def __init__(self, pos: Vector2, tail=None):
        self.pos = pos
        self.tail = tail

    def take(self, n):
        if n == 0:
            return None
        else:
            return Snake(self.pos, self.tail.take(n - 1) if self.tail is not None else None)

    def draw(self, screen, cSize, rSize):
        pygame.draw.rect(screen, (0, 255, 0), [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
        if self.tail is not None:
            self.tail.draw(screen, cSize, rSize)

    def length(self):
        if self.tail is None:
            return 1
        else:
            return 1 + self.tail.length()

    def skip(self, n):
        if n == 0:
            return self
        elif self.tail is None:
            return None
        else:
            return self.tail.skip(n - 1)

    def exist(self, p):
        if p(self.pos):
            return True
        elif self.tail is None:
            return False
        else:
            return self.tail.exist(p)


class Game:
    def __init__(self, colloms, rows, width, height):
        self.snake = Snake(Vector2(colloms//2, rows//2))
        self.colloms = colloms
        self.rows = rows + 2
        self.setfood()
        self.width = width
        self.height = height
        self.reset = False
        self.speed = 0.05
        self.score = 0
        self.cooldown = self.speed

        self.direction = pygame.K_UP
        self.length = 1

    def draw(self, screen):
        cSize = self.width / self.colloms
        rSize = self.height / self.rows
        for collom in range(0,self.colloms):
            for row in range(2):
                pygame.draw.rect(screen, (255,0,0), [collom * cSize, row * rSize, cSize, rSize])
        self.snake.draw(screen, cSize, rSize)
        pygame.draw.rect(screen, (0, 0, 255), [self.food.x * cSize, self.food.y * rSize, cSize - 2, rSize - 2])

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
                newpos = Vector2(self.snake.pos.x + 1, self.snake.pos.y)
            elif self.direction == pygame.K_DOWN:
                newpos = Vector2(self.snake.pos.x, self.snake.pos.y + 1)
            elif self.direction == pygame.K_LEFT:
                newpos = Vector2(self.snake.pos.x - 1, self.snake.pos.y)

            self.snake = Snake(newpos, self.snake)
            if self.isdead(self.snake):
                self.reset = True
            self.snake = self.snake.take(self.length)
            self.teleport(self.snake)
            self.cooldown = self.speed

            if self.snake.pos.is_same(self.food):
                self.length += 1
                self.score += 1
                snake = Snake(self.food, self.snake)
                self.setfood()

    def setfood(self):
        self.food = Vector2(random.randint(0, self.rows - 1), random.randint(2, self.colloms - 1))

    def isdead(self, snake):
        if(snake.pos.x < 0 or snake.pos.x > self.colloms-1) or (snake.pos.y < 2 or snake.pos.y > self.rows -1):
            return True
        if snake.length() > 1:
            return snake.skip(1).exist(lambda x: x.is_same(snake.pos))
        return False

    def teleport(self, snake):
            if snake.pos.x == self.colloms:
                snake.pos.x = 0
            if snake.pos.x == -1:
                snake.pos.x = self.colloms -1
            if snake.pos.y == self.rows:
                snake.pos.y = 2
            if snake.pos.y == 1:
                snake.pos.y = self.rows -1

