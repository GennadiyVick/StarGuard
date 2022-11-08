import pygame as pg

class Explossion(pg.sprite.Sprite):
    def __init__(self,screen,enemy,explist, kind = 1):
        super(Explossion,self).__init__()
        self.images = []
        self.screen = screen
        if kind == 1:
            for i in range(1,33):
                if i < 10: fn = f'./images/explossion/0{i}.png'
                else: fn = f'./images/explossion/{i}.png'
                image = pg.image.load(fn)
                self.images.append(image)
        else:
            for i in range(20):
                if i < 10: fn = f'./images/explossion2/0{i}.png'
                else: fn = f'./images/explossion2/{i}.png'
                image = pg.image.load(fn)
                self.images.append(image)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = enemy.rect.centerx-1
        self.rect.centery = enemy.rect.centery-2

        self.imageindex = 0
        self.frames = len(self.images)
        self.loopinterval = 4
        self.loop = 0
        if hasattr(enemy,'step_x'):
            self.stepx = enemy.step_x
            self.stepy = enemy.step_y
            enemy.kill()
        else:
            self.stepx = 0
            self.stepy = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.tormoz = 0.96
        explist.add(self)

    def draw(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.stepx != 0:
            self.x += self.stepx
            self.rect.x = self.x
            self.stepx *= self.tormoz
            if abs(self.stepx) < 0.1: self.stepx = 0
        if self.stepy != 0:
            self.y += self.stepy
            self.rect.y = self.y
            self.stepy *= self.tormoz
            if abs(self.stepy) < 0.1: self.stepy = 0

        self.loop += 1
        if self.loop >= self.loopinterval:
            self.loop = 0
            self.imageindex += 1
            if self.imageindex >= self.frames:
                self.kill()
            else:
                self.image = self.images[self.imageindex]

