import enemy
import pygame
from spritesheet import *
from util import *
pygame.init()

zombie_boss_frame1 = []
zombie_boss_frame2 = []
zombie_boss_im = get_im("assets/enemy_frame/zombie_spritesheet.png")
zombie_boss_sheet = SpriteSheet(zombie_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(zombie_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        zombie_boss_frame1.append(im)
        zombie_boss_frame2.append(zombie_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Skeleton_Boss
skeleton_boss_frame1 = []
skeleton_boss_frame2 = []
skeleton_boss_im = get_im("assets/enemy_frame/skeleton_spritesheet.png")
skeleton_boss_sheet = SpriteSheet(skeleton_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(skeleton_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        skeleton_boss_frame1.append(im)
        skeleton_boss_frame2.append(skeleton_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Goblin_Boss
goblin_boss_frame1 = []
goblin_boss_frame2 = []
goblin_boss_im = get_im("assets/enemy_frame/goblin_spritesheet.png")
goblin_boss_sheet = SpriteSheet(goblin_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(goblin_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        goblin_boss_frame1.append(im)
        goblin_boss_frame2.append(goblin_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Mushroom_Boss
mushroom_boss_frame1 = []
mushroom_boss_frame2 = []
mushroom_boss_im = get_im("assets/enemy_frame/mushroom_spritesheet.png")
mushroom_boss_sheet = SpriteSheet(mushroom_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(mushroom_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        mushroom_boss_frame1.append(im)
        mushroom_boss_frame2.append(mushroom_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Pumkin_Boss
pumkin_boss_frame1 = []
pumkin_boss_frame2 = []
pumkin_boss_im = get_im("assets/enemy_frame/pumkin_spritesheet.png")
pumkin_boss_sheet = SpriteSheet(pumkin_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(pumkin_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        pumkin_boss_frame1.append(im)
        pumkin_boss_frame2.append(pumkin_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Slime_Boss
slime_boss_frame1 = []
slime_boss_frame2 = []
slime_boss_im = get_im("assets/enemy_frame/slime_spritesheet.png")
slime_boss_sheet = SpriteSheet(slime_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(slime_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        slime_boss_frame1.append(im)
        slime_boss_frame2.append(slime_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Ghost_Boss
ghost_boss_frame1 = []
ghost_boss_frame2 = []
ghost_boss_im = get_im("assets/enemy_frame/ghost_spritesheet.png")
ghost_boss_sheet = SpriteSheet(ghost_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(ghost_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        ghost_boss_frame1.append(im)
        ghost_boss_frame2.append(ghost_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Pharaoh_Boss
pharaoh_boss_frame1 = []
pharaoh_boss_frame2 = []
pharaoh_boss_im = get_im("assets/enemy_frame/pharaoh_spritesheet.png")
pharaoh_boss_sheet = SpriteSheet(pharaoh_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(pharaoh_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        pharaoh_boss_frame1.append(im)
        pharaoh_boss_frame2.append(pharaoh_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Turtle_Boss
turtle_boss_frame1 = []
turtle_boss_frame2 = []
turtle_boss_im = get_im("assets/enemy_frame/turtle_spritesheet.png")
turtle_boss_sheet = SpriteSheet(turtle_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(turtle_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        turtle_boss_frame1.append(im)
        turtle_boss_frame2.append(turtle_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Desert_Goblin_Boss
desert_goblin_boss_frame1 = []
desert_goblin_boss_frame2 = []
desert_goblin_boss_im = get_im("assets/enemy_frame/desert_goblin_spritesheet.png")
desert_goblin_boss_sheet = SpriteSheet(desert_goblin_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(desert_goblin_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        desert_goblin_boss_frame1.append(im)
        desert_goblin_boss_frame2.append(desert_goblin_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Jellyfish_Boss
jellyfish_boss_frame1 = []
jellyfish_boss_frame2 = []
jellyfish_boss_im = get_im("assets/enemy_frame/jellyfish_spritesheet.png")
jellyfish_boss_sheet = SpriteSheet(jellyfish_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(jellyfish_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        jellyfish_boss_frame1.append(im)
        jellyfish_boss_frame2.append(jellyfish_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Shellfish_Boss
shellfish_boss_frame1 = []
shellfish_boss_frame2 = []
shellfish_boss_im = get_im("assets/enemy_frame/shellfish_spritesheet.png")
shellfish_boss_sheet = SpriteSheet(shellfish_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(shellfish_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        shellfish_boss_frame1.append(im)
        shellfish_boss_frame2.append(shellfish_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

# Cactus_Boss
cactus_boss_frame1 = []
cactus_boss_frame2 = []
cactus_boss_im = get_im("assets/enemy_frame/cactus_spritesheet.png")
cactus_boss_sheet = SpriteSheet(cactus_boss_im)
for i in range(2):
    for j in range(8):
        im = pygame.transform.flip(cactus_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)), True, False)
        im.set_colorkey((0, 0, 0))
        cactus_boss_frame1.append(im)
        cactus_boss_frame2.append(cactus_boss_sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))
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
        self.type = "zombie"
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = zombie_boss_frame2
        self.frame1 = zombie_boss_frame1
        self.im = self.frame[0]

# Skeleton_Boss
class Skeleton_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = skeleton_boss_frame2
        self.frame1 = skeleton_boss_frame1
        self.im = self.frame[0]

# Goblin_Boss
class Goblin_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = goblin_boss_frame2
        self.frame1 = goblin_boss_frame1
        self.im = self.frame[0]

# Mushroom_Boss
class Mushroom_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = mushroom_boss_frame2
        self.frame1 = mushroom_boss_frame1
        self.im = self.frame[0]

# Pumkin_Boss
class Pumkin_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.type = "pumkin"
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = pumkin_boss_frame2
        self.frame1 = pumkin_boss_frame1
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
        elif self.update >= 5 and self.death_c:
            self.update = 0
            self.death_c = False
        elif self.update >= 5:
            return True
        return False

# Slime_Boss
class Slime_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = slime_boss_frame2
        self.frame1 = slime_boss_frame1
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

# Ghost_Boss
class Ghost_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = ghost_boss_frame2
        self.frame1 = ghost_boss_frame1
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

# Pharaoh_Boss
class Pharaoh_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.type = "pharaoh"
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = pharaoh_boss_frame2
        self.frame1 = pharaoh_boss_frame1
        self.im = self.frame[0]

# Turtle_Boss
class Turtle_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = turtle_boss_frame2
        self.frame1 = turtle_boss_frame1
        self.im = self.frame[0]

# Desert_Goblin_Boss
class Desert_Goblin_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = desert_goblin_boss_frame2
        self.frame1 = desert_goblin_boss_frame1
        self.im = self.frame[0]

# Jellyfish_Boss
class Jellyfish_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.type = "jellyfish"
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = jellyfish_boss_frame2
        self.frame1 = jellyfish_boss_frame1
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

# Shellfish_Boss
class Shellfish_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = shellfish_boss_frame2
        self.frame1 = shellfish_boss_frame1
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

# Cactus_Boss
class Cactus_Boss(Boss):
    def __init__(self):
        super().__init__()
        self.max_health = 3000
        self.health = self.max_health
        self.speed = 0.06
        self.frame = cactus_boss_frame2
        self.frame1 = cactus_boss_frame1
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