import os
from time import sleep


class ExtraScreen:
    def __init__(self, parentScreen):
        self.ps = parentScreen
        self.fc = 0

    def update(self):
        self.fc += 1
        if self.fc == 10:
            return self.ps
        else:
            return self

    def draw(self):
        print("ExtraScreen: frame: %i" % self.fc)


class MainScreen:
    frameCount = 0

    def update(self):
        self.frameCount += 1
        if self.frameCount % 30 == 0:
            return ExtraScreen(self)
        else:
            return self

    def draw(self):
        print("MainScreen: frame: %i" % self.frameCount)

screen = MainScreen()

while True:
    screen = screen.update()
    #clear screen
    os.system("cls")
    screen.draw()
    sleep(0.1)