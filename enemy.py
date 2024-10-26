
import pygame
import random
import math
from util import *
from spritesheet import *
class Enemy():
    def __init__(self):
        self.move_check=True
        self.damage_count_pos=0
        self.damage_tick=0
        self.damage_tick_limit=20
        self.type = "common"
        self.x, self.y = get_random_position(640,405,1000)
        self.damage = 0.1
        self.hitbox = pygame.Rect(0,0,64,64)
        self.hitbox.left = -100
        self.hitbox.top = -100
        self.update = 6
        self.death_c = True

    def screen_move_check(self,key_pressed,speed,deltatime):
        if key_pressed[pygame.K_RIGHT]or key_pressed[pygame.K_d]:
            self.screen_move(-speed,0,deltatime)
        elif key_pressed[pygame.K_LEFT]or key_pressed[pygame.K_a]:
            self.screen_move(speed,0,deltatime)
        if key_pressed[pygame.K_UP]or key_pressed[pygame.K_w]:
            self.screen_move(0,speed,deltatime)
        elif key_pressed[pygame.K_DOWN]or key_pressed[pygame.K_s]:
            self.screen_move(0,-speed,deltatime)
    def  extinction(self, deltatime):
        self.update+=0.012 * deltatime  # 플레이어보다 왼쪽에 있다
        if self.health>=0:
            if self.update>=13:
                self.update=6
        elif self.update>=5.8 and self.death_c:
            self.update=0
            self.death_c=False
        elif self.update>=5.8:
            return True
        return False

    def flip_im(self):
        if self.direction.x<=0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256-(self.damage_tick_limit-self.damage_tick)*128//self.damage_tick_limit)
        else:
            self.im.set_alpha(256)

    def screen_move(self, x_speed, y_speed, deltatime):
        self.x += x_speed * deltatime
        self.y += y_speed * deltatime

    def updat(self):
        self.hitbox.left = self.x  # +self.im.get_size()[0]//2
        self.hitbox.top = self.y  # +self.im.get_size()[1]//2

    def select_speed(self, c_x, c_y):
        player_pos = pygame.Vector2([self.hitbox.centerx, self.hitbox.centery])
        enemy_pos = pygame.Vector2([c_x, c_y])
        self.direction = (player_pos - enemy_pos).normalize()

    def move(self, deltatime):
        self.x -= self.direction.x * self.speed * deltatime
        self.y -= self.direction.y * self.speed * deltatime

    def drawing(self, background):
        enemy_circle_surface = pygame.Surface((self.hitbox.width-10,25), pygame.SRCALPHA)
        pygame.draw.ellipse(enemy_circle_surface, (0,0,0,128), (0,0,self.hitbox.width-10,25))
        background.blit(enemy_circle_surface, (self.hitbox.left+5,self.hitbox.bottom-20))
        
        background.blit(self.im, (self.x - self.hitbox.width // 2, self.y - self.hitbox.height // 2))
        # if self.damage_tick>=self.damage_tick_limit:
        #     pygame.draw.rect(background, (0, 0, 255), self.hitbox, 5)

class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.05
        self.name = "zombie"
        self.im=pygame.image.load("assets/enemy_frame/zombie_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.06
        self.name = "skeleton"
        self.im=pygame.image.load("assets/enemy_frame/skeleton_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]
class Pharaoh(Enemy):
    def __init__(self):
        super().__init__()
        self.speed=0.05
        self.max_health = 100
        self.health = self.max_health
        self.name = "pharaoh"
        self.im=pygame.image.load("assets/enemy_frame/pharaoh_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

class Turtle(Enemy):
    def __init__(self):
        super().__init__()
        self.speed=0.04
        self.max_health = 100
        self.health = self.max_health
        self.name = "turtle"
        self.im=pygame.image.load("assets/enemy_frame/turtle_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.07
        self.name = "goblin"
        self.im=pygame.image.load("assets/enemy_frame/goblin_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

class Desert_Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.07
        self.name = "desert_Goblin"
        self.im=pygame.image.load("assets/enemy_frame/desert_goblin_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

class Mushroom(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.06
        self.name = "mushroom"
        self.im=pygame.image.load("assets/enemy_frame/mushroom_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]


class Pumkin(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.05
        self.name = "pumkin"
        self.im=pygame.image.load("assets/enemy_frame/pumkin_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

    def flip_im(self):
        if self.direction.x>=0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256-(self.damage_tick_limit-self.damage_tick)*128//self.damage_tick_limit)
        else:
            self.im.set_alpha(256)
    def  extinction(self, deltatime):
        self.update += 0.012 * deltatime
        if self.health >= 0:
            if self.update >= 5:
                self.update = 0
        elif self.update < 6 and self.death_c:
            self.damage = 0.2
            self.update = 6
            self.death_c = False
        elif self.update >= 12.8:
            return True
        return False

class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.05
        self.name = "slime"
        self.im=pygame.image.load("assets/enemy_frame/slime_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

    def  extinction(self,deltatime):
        self.update+=0.012*deltatime
        if self.health>=0:
            if self.update>=4:
                self.update=0
        elif self.update<=5 and self.death_c:
            self.update=6
            self.death_c=False
        elif self.update>=10:
            return True
        return False
    
    def flip_im(self):
        if self.direction.x>=0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256-(self.damage_tick_limit-self.damage_tick)*128//self.damage_tick_limit)
        else:
            self.im.set_alpha(256)
class Ghost(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.07
        self.name = "ghost"
        self.im=pygame.image.load("assets/enemy_frame/ghost_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]
    def flip_im(self):
        if self.direction.x>=0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256-(self.damage_tick_limit-self.damage_tick)*128//self.damage_tick_limit)
        else:
            self.im.set_alpha(256)
    def  extinction(self,deltatime):
        self.update+=0.012*deltatime
        if self.health>=0:
            if self.update>=2:
                self.update=0
        elif self.update<=2 and self.death_c:
            self.update=3
            self.death_c=False
        elif self.update>=7:
            return True
        return False
class Jellyfish(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.05
        self.name="jellyfish"
        self.im=pygame.image.load("assets/enemy_frame/jellyfish_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]

    def flip_im(self):
        if self.direction.x>=0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256-(self.damage_tick_limit-self.damage_tick)*128//self.damage_tick_limit)
        else:
            self.im.set_alpha(256)
    def  extinction(self,deltatime):
        self.update+=0.012*deltatime
        if self.health>=0:
            if self.update>=2:
                self.update=0
        elif self.update<=2 and self.death_c:
            self.update=3
            self.death_c=False
        elif self.update>=7:
            return True
        return False
class Shellfish(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.05
        self.name="sellfish"
        self.im=pygame.image.load("assets/enemy_frame/shellfish_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]
    def flip_im(self):
        if self.direction.x>=0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256-(self.damage_tick_limit-self.damage_tick)*128//self.damage_tick_limit)
        else:
            self.im.set_alpha(256)
    def  extinction(self,deltatime):
        self.update+=0.012*deltatime
        if self.health>=0:
            if self.update>=3:
                self.update=0
        elif self.update<=3 and self.death_c:
            self.update=4
            self.death_c=False
        elif self.update>=8:
            return True
        return False
class Cactus(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed=0.06
        self.name="cactus"
        self.im=pygame.image.load("assets/enemy_frame/cactus_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 2,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.im=self.frame[0]
    def flip_im(self):
        if self.direction.x>=0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256-(self.damage_tick_limit-self.damage_tick)*128//self.damage_tick_limit)
        else:
            self.im.set_alpha(256)
    def  extinction(self,deltatime):
        self.update+=0.012*deltatime
        if self.health>=0:
            if self.update>=4:
                self.update=0
        elif self.update<=4 and self.death_c:
            self.update=5
            self.death_c=False
        elif self.update>=8:
            return True
        return False