import pygame as pg
from pygame.sprite import Group
from random import randint
from bullet import Bullet

class Images(list):
    def __init__(self, filenames, interval = 10):
        super(Images,self).__init__()
        for fn in filenames:
            img = pg.image.load(fn).convert_alpha()
            self.append(img)
        self.interval = interval
        self.curintervalindex = 0
        self.current = 0
        self.count = len(self)

    def draw(self, screen, rect):
        if self.count == 0: return
        screen.blit(self[self.current],rect)
        if self.count == 1: return

        self.curintervalindex += 1
        if self.curintervalindex >= self.interval:
            self.current += 1
            if self.current >= self.count:
                self.current = 0
            self.curintervalindex = 0

    def get_rect(self):
        if self.count == 0: return None
        return self[0].get_rect()

    def image(self):
        if self.count == 0: return None
        return self[self.current]



class Enemy(pg.sprite.Sprite):
    def __init__(self,screen,enemys,bullets,imagefn):
        super(Enemy,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.enemys = enemys
        self.images = Images(imagefn)
        #self.orig_image = self.image
        self.rect = self.images.get_rect()
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
        self.images.draw(self.screen,self.rect)
        #self.screen.blit(self.image,self.rect)

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

        #if self.angle_change != 0:
        #    self.angle += self.angle_change
        #    self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        #    self.rect = self.image.get_rect(center=self.rect.center)
        #    self.angle_change = 0

    @property
    def image(self):
        return self.images.image()

    #@x.setter
    #def x(self, value):
    #    print("setter of x called")
    #    self._x = value

    #@x.deleter
    #def x(self):
    #    print("deleter of x called")
    #    del self._x

