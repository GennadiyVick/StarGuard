import pygame as pg
from pygame.sprite import Group
from random import randint
from bullet import Bullet

class Enemy(pg.sprite.Sprite):
    def __init__(self,screen,enemys,bullets):
        super(Enemy,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.enemys = enemys
        self.image = pg.image.load('./images/enemy1.png')
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x, self.y = float(self.rect.x), float(self.rect.y)
        self.lives = 1
        self.speed = 2.1
        self.angle = 0
        self.step_x = 0.0
        self.step_y = 0.0
        self.angle_change = 0
        self.lock = False
        self.bullets = bullets
        self.buletstimeinterval = randint(50,300)
        self.buletstime = 0

    def draw(self):
        if self.angle == 0:
            self.screen.blit(self.image,self.rect)

    def shot(self):
        bul = Bullet(self.screen,self,self.bullets, speed = 7, color = (74,136,210))

    def update(self):
        if self.lock: return
        self.y += self.step_y
        self.x += self.step_x
        self.rect.y = self.y
        self.rect.x = self.x
        if self.y >0:
            if self.step_x < 0:
                if self.x <= -self.rect.width:
                    self.step_x = -self.step_x
                    #self.angle_change = 90
            else:
                if self.x >= self.screen_rect.width:
                    self.step_x = -self.step_x
                    #self.angle_change = -90
            if self.y > self.screen_rect.height:
                self.kill()
                return
        self.buletstime +=1
        if self.buletstime > self.buletstimeinterval:
            self.buletstime = 0
            self.buletstimeinterval = randint(160,300)
            self.shot()




        if self.angle_change != 0:
            self.angle += self.angle_change
            self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.angle_change = 0
