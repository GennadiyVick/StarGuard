import pygame as pg


class Music():
    def __init__(self):
        pg.mixer.init()
        self.lst = ['./music/01.mp3','./music/02.mp3','./music/03.mp3']
        self.index = -1
        self.MUSIC_ENDED = pg.USEREVENT
        pg.mixer.music.set_endevent(self.MUSIC_ENDED)
        pg.mixer.music.set_volume(0.4)
        self.nextplay()


    def nextplay(self):
        self.index += 1
        if self.index >= len(self.lst):
            self.index = 0
        pg.mixer.music.load(self.lst[self.index])
        pg.mixer.music.play()
