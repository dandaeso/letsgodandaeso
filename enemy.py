
import pygame
import random
import math
from util import *
from spritesheet import *
from sound import sound_dict

zombie_frame1 = []
zombie_frame2 = []
zombie_im = get_im("assets/enemy_frame/zombie_spritesheet.png")
zombie_sheet = SpriteSheet(zombie_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(zombie_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        zombie_frame1.append(im)
        zombie_frame2.append(zombie_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))

skeleton_frame1 = []
skeleton_frame2 = []
skeleton_im = get_im("assets/enemy_frame/skeleton_spritesheet.png")
skeleton_sheet = SpriteSheet(skeleton_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(skeleton_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        skeleton_frame1.append(im)
        skeleton_frame2.append(skeleton_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


pharaoh_frame1 = []
pharaoh_frame2 = []
pharaoh_im = get_im("assets/enemy_frame/pharaoh_spritesheet.png")
pharaoh_sheet = SpriteSheet(pharaoh_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(pharaoh_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        pharaoh_frame1.append(im)
        pharaoh_frame2.append(pharaoh_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


turtle_frame1 = []
turtle_frame2 = []
turtle_im = get_im("assets/enemy_frame/turtle_spritesheet.png")
turtle_sheet = SpriteSheet(turtle_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(turtle_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        turtle_frame1.append(im)
        turtle_frame2.append(turtle_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


goblin_frame1 = []
goblin_frame2 = []
goblin_im = get_im("assets/enemy_frame/goblin_spritesheet.png")
goblin_sheet = SpriteSheet(goblin_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(goblin_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        goblin_frame1.append(im)
        goblin_frame2.append(goblin_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))

desert_goblin_frame1 = []
desert_goblin_frame2 = []
desert_goblin_im = get_im("assets/enemy_frame/desert_goblin_spritesheet.png")
desert_goblin_sheet = SpriteSheet(desert_goblin_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(desert_goblin_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        desert_goblin_frame1.append(im)
        desert_goblin_frame2.append(desert_goblin_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


mushroom_frame1 = []
mushroom_frame2 = []
mushroom_im = get_im("assets/enemy_frame/mushroom_spritesheet.png")
mushroom_sheet = SpriteSheet(mushroom_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(mushroom_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        mushroom_frame1.append(im)
        mushroom_frame2.append(mushroom_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


pumkin_frame1 = []
pumkin_frame2 = []
pumkin_im = get_im("assets/enemy_frame/pumkin_spritesheet.png")
pumkin_sheet = SpriteSheet(pumkin_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(pumkin_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        pumkin_frame1.append(im)
        pumkin_frame2.append(pumkin_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


slime_frame1 = []
slime_frame2 = []
slime_im = get_im("assets/enemy_frame/slime_spritesheet.png")
slime_sheet = SpriteSheet(slime_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(slime_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        slime_frame1.append(im)
        slime_frame2.append(slime_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


ghost_frame1 = []
ghost_frame2 = []
ghost_im = get_im("assets/enemy_frame/ghost_spritesheet.png")
ghost_sheet = SpriteSheet(ghost_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(ghost_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        ghost_frame1.append(im)
        ghost_frame2.append(ghost_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


jellyfish_frame1 = []
jellyfish_frame2 = []
jellyfish_im = get_im("assets/enemy_frame/jellyfish_spritesheet.png")
jellyfish_sheet = SpriteSheet(jellyfish_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(jellyfish_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        jellyfish_frame1.append(im)
        jellyfish_frame2.append(jellyfish_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


shellfish_frame1 = []
shellfish_frame2 = []
shellfish_im = get_im("assets/enemy_frame/shellfish_spritesheet.png")
shellfish_sheet = SpriteSheet(shellfish_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(shellfish_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        shellfish_frame1.append(im)
        shellfish_frame2.append(shellfish_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))


cactus_frame1 = []
cactus_frame2 = []
cactus_im = get_im("assets/enemy_frame/cactus_spritesheet.png")
cactus_sheet = SpriteSheet(cactus_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(cactus_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        cactus_frame1.append(im)
        cactus_frame2.append(cactus_sheet.get_image(j, i, 64, 64, 2, (0, 0, 0)))

class Enemy():
    def __init__(self):
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.05
        self.gen=True
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
    def setting(self,wave):
        self.x, self.y = get_random_position(640,405,1000)
        self.max_health*=(1+0.1*wave)
        self.health = self.max_health
        self.damage*=(1+0.1*wave)
        self.speed*=(1+0.005*wave)
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
        self.speed = 0.05
        self.name = "zombie"
        self.frame = zombie_frame2
        self.frame1 = zombie_frame1
        self.im = self.frame[0]

class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.06
        self.name = "skeleton"
        self.frame = skeleton_frame2
        self.frame1 = skeleton_frame1
        self.im = self.frame[0]

class Pharaoh(Enemy):
    def __init__(self):
        super().__init__()
        self.speed = 0.05
        self.max_health = 100
        self.health = self.max_health
        self.name = "pharaoh"
        self.frame = pharaoh_frame2
        self.frame1 = pharaoh_frame1
        self.im = self.frame[0]

class Turtle(Enemy):
    def __init__(self):
        super().__init__()
        self.speed = 0.04
        self.max_health = 100
        self.health = self.max_health
        self.name = "turtle"
        self.frame = turtle_frame2
        self.frame1 = turtle_frame1
        self.im = self.frame[0]

class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.07
        self.name = "goblin"
        self.frame = goblin_frame2
        self.frame1 = goblin_frame1
        self.im = self.frame[0]

class Desert_Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.07
        self.name = "desert_Goblin"
        self.frame = desert_goblin_frame2
        self.frame1 = desert_goblin_frame1
        self.im = self.frame[0]

class Mushroom(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.06
        self.name = "mushroom"
        self.frame = mushroom_frame2
        self.frame1 = mushroom_frame1
        self.im = self.frame[0]

class Pumkin(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.05
        self.name = "pumkin"
        self.frame = pumkin_frame2
        self.frame1 = pumkin_frame1
        self.im = self.frame[0]

    def flip_im(self):
        if self.direction.x >= 0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256 - (self.damage_tick_limit - self.damage_tick) * 128 // self.damage_tick_limit)
        else:
            self.im.set_alpha(256)

    def extinction(self, deltatime):
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
        self.speed = 0.05
        self.name = "slime"
        self.frame = slime_frame2
        self.frame1 = slime_frame1
        self.im = self.frame[0]

    def extinction(self, deltatime):
        self.update += 0.012 * deltatime
        if self.health >= 0:
            if self.update >= 4:
                self.update = 0
        elif self.update <= 5 and self.death_c:
            self.update = 6
            self.death_c = False
        elif self.update >= 10:
            return True
        return False

    def flip_im(self):
        if self.direction.x >= 0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256 - (self.damage_tick_limit - self.damage_tick) * 128 // self.damage_tick_limit)
        else:
            self.im.set_alpha(256)

class Ghost(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.07
        self.name = "ghost"
        self.frame = ghost_frame2
        self.frame1 = ghost_frame1
        self.im = self.frame[0]

    def flip_im(self):
        if self.direction.x >= 0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256 - (self.damage_tick_limit - self.damage_tick) * 128 // self.damage_tick_limit)
        else:
            self.im.set_alpha(256)

    def extinction(self, deltatime):
        self.update += 0.012 * deltatime
        if self.health >= 0:
            if self.update >= 2:
                self.update = 0
        elif self.update <= 2 and self.death_c:
            self.update = 3
            self.death_c = False
        elif self.update >= 7:
            return True
        return False

class Jellyfish(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.05
        self.name = "jellyfish"
        self.frame = jellyfish_frame2
        self.frame1 = jellyfish_frame1
        self.im = self.frame[0]

    def flip_im(self):
        if self.direction.x >= 0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256 - (self.damage_tick_limit - self.damage_tick) * 128 // self.damage_tick_limit)
        else:
            self.im.set_alpha(256)

    def extinction(self, deltatime):
        self.update += 0.012 * deltatime
        if self.health >= 0:
            if self.update >= 2:
                self.update = 0
        elif self.update <= 2 and self.death_c:
            self.update = 3
            self.death_c = False
        elif self.update >= 7:
            return True
        return False

class Shellfish(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.05
        self.name = "shellfish"
        self.frame = shellfish_frame2
        self.frame1 = shellfish_frame1
        self.im = self.frame[0]

    def flip_im(self):
        if self.direction.x >= 0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256 - (self.damage_tick_limit - self.damage_tick) * 128 // self.damage_tick_limit)
        else:
            self.im.set_alpha(256)

    def extinction(self, deltatime):
        self.update += 0.012 * deltatime
        if self.health >= 0:
            if self.update >= 3:
                self.update = 0
        elif self.update <= 3 and self.death_c:
            self.update = 4
            self.death_c = False
        elif self.update >= 8:
            return True
        return False

class Cactus(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.speed = 0.06
        self.name = "cactus"
        self.frame = cactus_frame2
        self.frame1 = cactus_frame1
        self.im = self.frame[0]

    def flip_im(self):
        if self.direction.x >= 0:
            self.im = self.frame[int(self.update)]
        else:
            self.im = self.frame1[int(self.update)]
        if self.damage_tick <= self.damage_tick_limit:
            self.im.set_alpha(256 - (self.damage_tick_limit - self.damage_tick) * 128 // self.damage_tick_limit)
        else:
            self.im.set_alpha(256)

    def extinction(self, deltatime):
        self.update += 0.012 * deltatime