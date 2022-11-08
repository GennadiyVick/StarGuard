import pygame as pg
from pygame.sprite import Group
class Level:
    def __init__(self, screen, gun, bullets):
        self.Finished = False
        self.Enemys = Group()
        self.screen = screen
        self.gun = gun
        self.bullets = bulles

    def update(self):
        pass
