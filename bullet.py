import pygame as pg

class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, gun, bullets, speed = -8, color = (139,195,74)):
        super(Bullet,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.bullets = bullets
        self.rect = pg.Rect(0,0,4,8)
        self.color = color
        self.speed = speed
        self.rect.centerx = gun.rect.centerx
        if speed < 0:
            self.rect.top = gun.rect.top
        else:
            self.rect.top = gun.rect.bottom
        self.y = float(self.rect.y)
        self.bullets.add(self)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.speed < 0:
            if self.rect.bottom < 0:
                self.bullets.remove(self)
        else:
            if self.rect.top > self.screen_rect.bottom:
                self.bullets.remove(self)

    def draw(self):
        pg.draw.rect(self.screen,self.color,self.rect)
