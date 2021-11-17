#!/usr/bin/python3

import pygame as pg
import math
from gun import Gun
from pygame.sprite import Group
from enemy import Enemy
import events
import pathlib
from random import randint, random
from explossion import Explossion
from star import Stars
import os.path
from music import Music
#from config import enemy_step_x, enemy_step_y, enemy_angle


def createEnemys(screen, enemys, bullets):
    enemy = Enemy(screen,enemys, bullets)
    enemy_w = enemy.rect.width+4
    enemy_h = enemy.rect.height-20
    screenrect = screen.get_rect()
    start_x = screenrect.width // 2
    start_y = -enemy_h
    enemy_speed = random() * 2.6 + 3.8
    if randint(0,1) == 0:
        enemy_angle = randint(96,120)
        enemy_ofs_angle = enemy_angle + 180
    else:
        enemy_angle = randint(240,264)
        enemy_ofs_angle = enemy_angle - 180
    enemy_rad = math.radians(enemy_angle)
    enemy_ofs_rad = math.radians(enemy_ofs_angle)

    enemy_step_x = math.sin(enemy_rad) * enemy_speed
    enemy_step_y = -math.cos(enemy_rad) * enemy_speed
    enemy_offset = 80 #(enemy_w+enemy_h) // 2
    enemy_ofs_x =  math.sin(enemy_ofs_rad) * enemy_offset
    enemy_ofs_y =  -math.cos(enemy_ofs_rad) * enemy_offset


    for num in range(8+randint(0,14)):
        enemy = Enemy(screen,enemys, bullets)
        enemy.x = float(start_x + num * enemy_ofs_x)
        enemy.y = float(start_y + num * enemy_ofs_y)
        enemy.step_x = enemy_step_x
        enemy.step_y = enemy_step_y
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y
        enemys.add(enemy)


def strtoint(s, default = 0):
    try:
        return int(s)
    except:
        return default



def run():
    pg.init()
    music = Music()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption('Космические защитники')
    bg_color = (0,0,0)
    enemys = Group()
    expl = Group()
    gun = Gun(screen,enemys,expl)
    clock = pg.time.Clock()
    bullets = Group()
    createEnemys(screen,enemys, bullets)
    pg.font.init()
    #font_info = pg.font.SysFont('Ubuntu', 14)
    font_info = pg.freetype.Font("./fonts/calibri.ttf", 12)
    font_game_over = pg.freetype.Font("./fonts/calibrib.ttf", 72)
    stars = Stars(screen)
    gameover = False
    gun.record = 0
    if os.path.isfile('records.txt'):
        with open('records.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) > 0 and len(lines[0]) > 0:
                gun.record = strtoint(lines[0])

    while True:
        events.events(screen,gun,music)
        screen.fill(bg_color)
        stars.update()
        stars.draw()
        gun.update()
        gun.draw()
        bullets.update()
        enemys.update()
        enemys.draw(screen)
        for bullet in bullets.sprites():
            bullet.draw()
        expl.update()
        expl.draw(screen)

        if not gun.lock and not gun.blinking:
            collis = pg.sprite.spritecollide(gun, bullets, True)
            if len(collis) > 0:
                gun.lock = True
                ex2 = Explossion(screen,gun,gun.expl)
                gun.sounds['me'].play()
            #collis = pg.sprite.spritecollideany(gun,bullets)
        for i in range(gun.life-1):
            screen.blit(gun.image.images[0],(i*40+5,5))
        if gun.score > gun.record:
            gun.record = gun.score

        font_info.render_to(screen, (640, 5), f"Рекорд: {gun.record}, cчет: {gun.score}", (255, 100, 100))

        if gun.life <= 0:
            font_game_over.render_to(screen, (210, 360), "GAME OVER", (255, 50, 50))

        pg.display.flip()
        clock.tick(60)
        if len(enemys) == 0 and gun.life >= 1:
            createEnemys(screen,enemys,bullets)




run()

pg.quit()
