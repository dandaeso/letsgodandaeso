import random
import pygame
from spritesheet import *
from util import *

digging_sound=get_sound('assets/enemy_sound/digging.MP3')
storm_sound=get_sound('assets/enemy_sound/storm.MP3')
sparke_sound=get_sound('assets/enemy_sound/spark.MP3')

class boss_pattern:
    def __init__(self):
        pass

    def drawing(self, background):
        try:
            background.blit(self.im, (self.x - self.hitbox.width // 4, self.y - self.hitbox.height // 4))
        except:
            pass

    def screen_move_check(self,key_pressed,speed,deltatime):
        if key_pressed[pygame.K_RIGHT]or key_pressed[pygame.K_d]:
            self.screen_move(-speed,0,deltatime)
        elif key_pressed[pygame.K_LEFT]or key_pressed[pygame.K_a]:
            self.screen_move(speed,0,deltatime)
        if key_pressed[pygame.K_UP]or key_pressed[pygame.K_w]:
            self.screen_move(0,speed,deltatime)
        elif key_pressed[pygame.K_DOWN]or key_pressed[pygame.K_s]:
            self.screen_move(0,-speed,deltatime)

    def screen_move(self, x_speed, y_speed, deltatime):
        self.x += x_speed * deltatime
        self.y += y_speed * deltatime
    def move(self,deltatime):
        pass
    def update(self):
        self.hitbox.left=self.x
        self.hitbox.top=self.y

class Boss_pattern1(boss_pattern):
    def __init__(self):
        self.x,self.y=random.randint(0,1280),random.randint(0,840)
        self.target_x,self.target_y=1280,840
        self.frame=False
        self.im=False
        self.damage=1
        self.updat=0
        self.hitbox=pygame.rect.Rect(self.x,self.y,128,128)
    def change_frame(self,deltatime):
        try:
            if self.updat<=1:
                self.updat+=0.0007*deltatime
            else:
                self.updat+=0.032*deltatime
            self.im=self.frame[int(self.updat)]
            return False
        except IndexError:
            return True
        
class Boss_pattern2(boss_pattern):
    def __init__(self):
        self.target_x,self.target_y=random.randint(0, 1280 - 256), random.randint(0, 840 - 256)
        self.x,self.y=random.randint(0, 1280 - 256),-256
        self.frame=False
        self.im=False
        self.damage=1
        self.updat=0
        self.hitbox=pygame.rect.Rect(self.x,self.y,64,64)
        self.direction=pygame.Vector2(self.x-self.target_x,self.y-self.target_y).normalize()
    def change_frame(self,deltatime):
        if self.frame:
            self.updat+=0.012*deltatime
            if self.updat>5:
                self.updat=0
            self.im=self.frame[int(self.updat)]
        else:
            pass
        return False
    
    def move(self, deltatime):
        self.x -= self.direction.x * deltatime*0.1
        self.y -= self.direction.y  * deltatime*0.1

class pumkin_pattern1(Boss_pattern1):
    def __init__(self):
        super().__init__()
        digging_sound.play()
        self.im=get_im("assets/pattern1/pumkin.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        for i in range(2):
            for j in range(8):
                self.frame.append(self.sheet.get_image(j,i,64,64, 3,(0,0,0)))
        self.im=self.frame[0]




class zombie_pattern1(Boss_pattern1):
    def __init__(self):
        super().__init__()
        digging_sound.play()
        self.im=get_im("assets/pattern1/zombie.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        for i in range(2):
            for j in range(8):
                self.frame.append(self.sheet.get_image(j,i,64,64, 3,(0,0,0)))
        self.im=self.frame[0]
    def drawing(self, background):
        try:
            #pygame.draw.rect(background,(255,0,0),self.hitbox,5)
            background.blit(self.im, (self.x - self.hitbox.width, self.y - self.hitbox.height))
        except:
            pass



class jellyfish_pattern1(Boss_pattern1):
    def __init__(self):
        super().__init__()
        sparke_sound.play()
        self.im=get_im("assets/pattern1/jellyfish.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        for i in range(2):
            for j in range(8):
                self.frame.append(self.sheet.get_image(j,i,64,64, 3,(0,0,0)))
        self.im=self.frame[0]


class pharaoh_pattern1(Boss_pattern1):
    def __init__(self):
        super().__init__()
        digging_sound.play()
        self.im=get_im("assets/pattern1/desert.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        for i in range(2):
            for j in range(8):
                self.frame.append(self.sheet.get_image(j,i,64,64, 3,(0,0,0)))
        self.im=self.frame[0]




class pumkin_pattern2(Boss_pattern2):
    def __init__(self):
        super().__init__()
        self.im=get_im("assets/pattern2/pumkin.png").convert_alpha()
        self.im=pygame.transform.scale(self.im,(128,128))



class zombie_pattern2(Boss_pattern2):
    def __init__(self):
        super().__init__()
        self.im=get_im("assets/pattern2/zombie.png").convert_alpha()
        self.im=pygame.transform.scale(self.im,(96,96))




class jellyfish_pattern2(Boss_pattern2):
    def __init__(self):
        super().__init__()
        storm_sound.play()
        self.im=get_im("assets/pattern2/sea.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        for i in range(2):
            for j in range(8):
                self.frame.append(self.sheet.get_image(j,i,64,64, 3,(0,0,0)))
        self.im=self.frame[0]


class pharaoh_pattern2(Boss_pattern2):
    def __init__(self):
        super().__init__()
        storm_sound.play()
        self.im=get_im("assets/pattern2/desert.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        for i in range(2):
            for j in range(8):
                self.frame.append(self.sheet.get_image(j,i,64,64, 3,(0,0,0)))
        self.im=self.frame[0]

