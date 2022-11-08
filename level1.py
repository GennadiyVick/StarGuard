import pygame as pg
from level import Level


class Level1(Level):
    def __init__(self, screen, gun, bullets):
        super(Level1,self).__init__(screen, gun, bullets)
        self.allEnemyCount = 500
        self.createdEnemyCount = 0
        #self.Enemys.empty()


    def createEnemys(self):
        enemy = Enemy(screen,enemys, bullets,['./images/enemy1.png'])
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


    def update(self):
        #super(Level1, self).update()
        pass



