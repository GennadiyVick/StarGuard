import pygame as pg
from bullet import Bullet
from pygame.sprite import Group
from explossion import Explossion

class GunImage():
    def __init__(self):
        self.imageturn = 0 # 0 - прямо, -1 - лево, 1 - право
        self.firechangeinterval = 6
        self.firechangeindex = 0
        self.fire = 0
        self.images = []
        self.imageindex = 0
        for i in range(6):
            self.images.append(pg.image.load(f'./images/gun1/0{i}.png'))

    def update(self, left,right):
        if self.firechangeindex == 0:
            self.fire = 0 if self.fire == 1 else 1
        self.firechangeindex += 1

        if self.firechangeindex >= self.firechangeinterval:
            self.firechangeindex = 0

        if left:
            self.imageindex = 2
        elif right:
            self.imageindex = 4
        else:
            self.imageindex = 0

    def image(self):
        return self.images[self.imageindex + self.fire]

class Gun(pg.sprite.Sprite):
    def __init__(self, screen, enemys, expl):
        super(Gun,self).__init__()
        self.screen = screen
        self.expl = expl
        self.enemys = enemys
        self.image = GunImage() #pg.image.load('./images/gun1/gun.png')
        self.rect = self.image.image().get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #self.image = GunImage() #pg.image.load('./images/gun1/gun.png')
        self.rect = self.image.image().get_rect()
        self.screen_rect = screen.get_rect()
        self.sounds = {'me': pg.mixer.Sound('./sounds/playerexplossion.wav'), 'ee': pg.mixer.Sound('./sounds/explossion.wav'),'shot': pg.mixer.Sound('./sounds/laser.wav')}
        #my_sound.set_volume(0.5)
        self.init()

    def init(self):
        self.score = 0
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.bullets = Group()
        self.speed = 4.5
        self.moveleft = False
        self.moveright = False
        self.center = float(self.rect.centerx)
        self.buletstimeinterval = 24
        self.buletstime = 0
        self.shoting = False
        self.lock = False
        self.blinking = True
        self.blink = 0
        self.blink_cnt = 20
        self.blink_interval = 5
        self.blink_curint = 0
        self.dieloopcount = 140
        self.dieloop = 0
        self.life = 3

    def draw(self):
        if not self.lock:
            if self.blinking:
                if self.blink_curint == 0:
                    if self.blink % 2 == 0:
                        self.screen.blit(self.image.image(),self.rect)
                    self.blink += 1
                    if self.blink > self.blink_cnt:
                        self.blink = 0
                        self.blink_curint = 0
                        self.blinking = False
                self.blink_curint += 1
                if self.blink_curint >= self.blink_interval:
                    self.blink_curint = 0
            else:
                self.screen.blit(self.image.image(),self.rect)
        for bullet in self.bullets.sprites():
            bullet.draw()

    def shot(self):
        bul = Bullet(self.screen,self,self.bullets)
        self.sounds['shot'].play()

    def update(self):
        if not self.lock:
            if self.moveleft and self.rect.left > 0:
                self.center -= self.speed
                self.rect.centerx = int(self.center)
            if self.moveright and self.rect.right < self.screen_rect.right:
                self.center += self.speed
                self.rect.centerx = int(self.center)
            if self.shoting:
                if self.buletstime == 0:
                    self.shot()
                self.buletstime +=1
                if self.buletstime > self.buletstimeinterval:
                    self.buletstime = 0
            else:
                if self.buletstime > 0:
                    self.buletstime +=1
                    if self.buletstime > self.buletstimeinterval:
                        self.buletstime = 0
            self.image.update(self.moveleft,self.moveright)
        else:
            if self.life >= 0:
                self.dieloop += 1
                if self.dieloop >= self.dieloopcount:
                    self.life -= 1
                    if self.life > 0:
                        self.dieloop = 0
                        self.blinking = True
                        self.lock = False
                    else:
                        self.enemys.empty()
                    return
            else:
                #game over
                return
        self.bullets.update()
        if len(self.bullets)>0:
            collis = pg.sprite.groupcollide(self.bullets,self.enemys,True,False)
            for bul in  collis:
                for  enemy in collis[bul]:
                    enemy.lock = True
                    ex = Explossion(self.screen,enemy,self.expl,2)
                    self.sounds['ee'].play()
                    self.score += 1

        if not self.lock:
            checkcollis = False
            for enemy in self.enemys:
                if enemy.rect.y > 700:
                    checkcollis = True
                    break
            if checkcollis:
                collis = pg.sprite.spritecollideany(self,self.enemys)
                if collis != None and not self.blinking:
                    collis.lock = True
                    ex = Explossion(self.screen,collis,self.expl,2)
                    self.sounds['ee'].play()
                    self.lock = True
                    ex2 = Explossion(self.screen,self,self.expl)
                    self.sounds['me'].play()
            #{<Bullet Sprite(in 0 groups)>: [<Enemy Sprite(in 1 groups)>]}

