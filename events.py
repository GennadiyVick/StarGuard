import pygame as pg
import sys


def events(screen,gun, music):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            with open('records.txt', 'w') as f:
                f.write(str(gun.record))
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                gun.moveright = True
            elif event.key == pg.K_LEFT:
                gun.moveleft = True
            elif event.key == pg.K_SPACE:
                #gun.buletstime = 0
                gun.shoting = True
            elif event.key == pg.K_RETURN:
                if gun.life <= 0:
                    gun.init()

        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
               gun.moveright = False
            elif event.key == pg.K_LEFT:
               gun.moveleft = False
            elif event.key == pg.K_SPACE:
                gun.shoting = False
        elif event.type == music.MUSIC_ENDED:
            music.nextplay()
