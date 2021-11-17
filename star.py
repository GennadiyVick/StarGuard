import pygame as pg
from random import randint, random

class Star():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = random() * 2 + 1
        if self.speed  > 2.4:
            self.starwidth = 1
        else: self.starwidth = 0
        col = 95 + int((self.speed-1) * 80)
        self.color = (col,col,col)


class Stars(list):
    def __init__(self,screen):
        super(Stars,self).__init__()
        self.screen = screen
        screenrect = screen.get_rect()
        self.screenw = screenrect.width
        self.screenh = screenrect.height
        for s in range(randint(30,40)):
            star = Star(random() * self.screenw,random() *  self.screenh)
            self.append(star)

    def update(self):
        for star in self:
            star.y += star.speed
            if star.y > self.screenh:
                star.x = random() * self.screenw
                star.y = -5

    def draw(self):
        for star in self:
            x = int(star.x)
            y = int(star.y)

            pg.draw.line(self.screen, star.color, (x,y), (x+star.starwidth,y))


