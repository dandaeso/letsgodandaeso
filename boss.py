import enemy
import pygame
from spritesheet import *
class Boss(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.hitbox=pygame.rect.Rect(0,0,128,128)
        self.type="boss"
        self.name="boss"
        self.pattern_limit=5
        self.pattern_time=0
        self.bonus_life=0
        self.invincibility=False
class Zombie_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.type="zombie"
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/zombie_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
        self.im=self.frame[0]
class Skeleton_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/skeleton_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
        self.im=self.frame[0]
class Goblin_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/goblin_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
        self.im=self.frame[0]
class Mushroom_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/mushroom_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
        self.im=self.frame[0]
class Pumkin_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.type="pumkin"
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/pumkin_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
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
            if self.update>=5:
                self.update=0
        elif self.update>=5 and self.death_c:
            self.update=0
            self.death_c=False
        elif self.update>=5:
            return True
        return False

class Slime_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/slime_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
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


class Ghost_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/ghost_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
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
class Pharaoh_Boss(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.type="pharaoh"
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/pharaoh_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
        self.im=self.frame[0]
class Turtle_Boss(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/turtle_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
        self.im=self.frame[0]

class Desert_Goblin_Boss(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/desert_goblin_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
        self.im=self.frame[0]

class Jellyfish_Boss(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.type="jellyfish"
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/jellyfish_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
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
class Shellfish_Boss(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/shellfish_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
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
class Cactus_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed=0.06
        self.im=pygame.image.load("assets/enemy_frame/cactus_spritesheet.png").convert_alpha()
        self.sheet = SpriteSheet(self.im)
        self.frame=[]
        self.frame1=[]
        for i in range(2):
            for j in range(8):
                im=pygame.transform.flip(self.sheet.get_image(j,i,64,64, 4,(0,0,0)),True,False)
                im.set_colorkey((0,0,0))
                self.frame1.append(im)
                self.frame.append(self.sheet.get_image(j,i,64,64, 4,(0,0,0)))
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