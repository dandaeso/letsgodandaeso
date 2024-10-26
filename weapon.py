import pygame
import spritesheet
import random
import math
from util import *
from sound import sound_dict


class Buff_data:
    def __init__(self, name):
        self.name = name
        self.level = 0

    def get_data(self):
        try:
            return float(get_data(self.name, self.level))
        except:
            return float(get_data(self.name, self.level)[0]), float(get_data(self.name, self.level)[1])

class Weapon_Data:
    def __init__(self, character, screen_size, name):
        self.name = name
        self.level = 0
        self.repeat_count = 1
        self.character = character
        self.bg_width, self.bg_height = screen_size[0], screen_size[1]
        self.damage = 0
        self.cooltime = 0
        self.cooltime_limit = 100
        self.im = True

    def get_cooltime_limit(self):
        value = get_data(self.name, self.level)
        return float(value[2])

    def get_repeat(self):
        value = get_data(self.name, self.level)
        return float(value[0])

    def get_damage(self):
        value = get_data(self.name, self.level)
        return float(value[1])

    def get_data(self, random_angle, repeat, m_x, m_y):
        pass

class Dagger_Data(Weapon_Data):
    def __init__(self, character, screen_size, name):
        super().__init__(character, screen_size, name)
        self.im = get_im("assets/weapon/dagger.png")

    def get_data(self, random_angle, max_reapeat, repeat, m_x, m_y):
        angle = random_angle + math.radians(360 // max_reapeat * repeat)
        direction_x = math.cos(angle)
        direction_y = math.sin(angle)
        target_pos_x = self.character.hitbox.left + direction_x
        target_pos_y = self.character.hitbox.top + direction_y
        return self.im, pygame.Rect(0, 0, 64, 64), self.character.hitbox.left, self.character.hitbox.top, target_pos_x, target_pos_y, 320, self.get_damage()

class Staff_Data(Weapon_Data):
    def __init__(self, character, screen_size, name):
        super().__init__(character, screen_size, name)
        self.im = get_im("assets/weapon/staff.png")

    def get_data(self, random_angle, repeat, m_x, m_y):
        angle = math.radians(40 * repeat)
        direction_x = math.cos(angle)
        direction_y = math.sin(angle)
        target_x = m_x + direction_x * random.randint(80, 120) * random.choice([-1, 1])
        target_y = m_y + direction_y * random.randint(80, 120) * random.choice([-1, 1])
        return self.im, pygame.Rect(0, 0, 64, 64), self.character.hitbox.left, self.character.hitbox.top, target_x, target_y, self.get_damage()

class Star_Data(Weapon_Data):
    def __init__(self, character, screen_size, name):
        super().__init__(character, screen_size, name)
        self.im = get_im("assets/weapon/star.png")

    def get_data(self, random_angle, max_repeat, repeat, m_x, m_y):
        angle_offset = (2 * math.pi) / max_repeat
        angle = random_angle + repeat * angle_offset
        initial_x = self.character.hitbox.x
        initial_y = self.character.hitbox.y
        return self.im, pygame.Rect(0, 0, 32, 32), initial_x, initial_y, angle, m_y, self.get_damage()

class Missile_Data(Weapon_Data):
    def __init__(self, character, screen_size, name):
        super().__init__(character, screen_size, name)
        missile_im = get_im("assets/weapon/missile.png")
        missile_sheet = spritesheet.SpriteSheet(missile_im)
        self.im = []
        for i in range(2):
            for j in range(8):
                im = missile_sheet.get_image(j, i, 64, 64, 3, (0, 0, 0))
                self.im.append(im.convert_alpha())

    def get_data(self, random_angle, repeat, m_x, m_y):
        return self.im, pygame.Rect(0, 0, 96, 96), random.randint(0, self.bg_width - 256), -256, random.randint(0, self.bg_width - 256), random.randint(0, self.bg_height - 256), self.get_damage()

class Mine_Data(Weapon_Data):
    def __init__(self, character, screen_size, name):
        super().__init__(character, screen_size, name)
        im = get_im("assets/weapon/mine.png")
        sheet = spritesheet.SpriteSheet(im)
        self.im = []
        for i in range(2):
            for j in range(8):
                self.im.append(sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

    def get_data(self, random_angle, repeat, m_x, m_y):
        random_pos_x = random.randint(0, self.bg_width - 64)
        random_pos_y = random.randint(0, self.bg_height - 64)
        return self.im, random_pos_x, random_pos_y, pygame.Rect(random_pos_x, random_pos_y, 96, 96), random_pos_x, random_pos_y, self.get_damage()

class Sword_Data(Weapon_Data):
    def __init__(self, character, screen_size, name):
        super().__init__(character, screen_size, name)
        im = get_im("assets/weapon/sword.png")
        sheet = spritesheet.SpriteSheet(im)
        self.im = []
        for i in range(2):
            for j in range(8):
                self.im.append(sheet.get_image(j, i, 64, 64, 4, (0, 0, 0)))

    def get_data(self, repeat, m_x, m_y):
        return self.im, pygame.Rect(0, 0, 256, 256), self.character.hitbox.centerx, self.character.hitbox.centery, self.character.hitbox.centerx, self.character.hitbox.centery, self.get_damage()

class Weapon_effect:
    def __init__(self, im, hitbox, x, y, target_pos_x, target_pos_y, damage):
        self.disappear=True
        self.exploded = False
        self.im = im
        self.hitbox = hitbox.copy()
        self.hitbox.left = x
        self.hitbox.left = y
        self.x = x
        self.y = y
        self.damage = damage
        self.target_pos_x = target_pos_x
        self.target_pos_y = target_pos_y

    def screen_move_check(self, key_pressed, deltatime, speed):
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self.screen_move(-speed, 0, deltatime)
        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.screen_move(speed, 0, deltatime)
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
            self.screen_move(0, speed, deltatime)
        elif key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
            self.screen_move(0, -speed, deltatime)

    def extinction_condition(self, bg_rect, c_rect):
        pass

    def change_frame(self, deltatime, enemy):
        return False

    def screen_move(self, x_speed, y_speed, deltatime):
        self.x += x_speed * deltatime
        self.y += y_speed * deltatime

    def drawing(self, background):
        background.blit(self.rotate_im, (self.x + self.im.get_width() / 2 - self.rotate_im.get_width() / 2, self.y + self.im.get_height() / 2 - self.rotate_im.get_height() / 2))

    def update(self):
        self.hitbox.left = self.x
        self.hitbox.top = self.y

    def move(self, deltatime, c_x, c_y):
        self.x += self.direction.x * self.speed * deltatime
        self.y += self.direction.y * self.speed * deltatime

class Move_weapon(Weapon_effect):
    def __init__(self, im, hitbox, x, y, target_pos_x, target_pos_y, damage):
        super().__init__(im, hitbox, x, y, target_pos_x, target_pos_y, damage)
        self.speed = 0.5
        target_pos = pygame.Vector2(target_pos_x, target_pos_y)
        character_pos = pygame.Vector2(x, y)
        self.direction = (target_pos - character_pos).normalize()
        self.angle = math.degrees(math.atan2(target_pos_y - y, target_pos_x - x))
        try:
            self.rotate_im = pygame.transform.rotate(self.im, -self.angle)
        except:
            self.rotate_im = pygame.transform.rotate(self.im[0], -self.angle)
        self.rotated_rect = self.rotate_im.get_rect(center=(self.x, self.y))

class Missile(Move_weapon):
    def __init__(self, frame, hitbox, x, y, target_pos_x, target_pos_y, damage):
        super().__init__(frame, hitbox, x, y, target_pos_x, target_pos_y, damage)
        self.im = frame[0]
        self.frame = frame
        self.updat = 0
        self.speed = 0.5
        self.hitbox.left = self.x
        self.hitbox.top = self.y
        self.exploded = False

    def move(self, deltatime, c_x, c_y):
        if not self.exploded:
            self.x += self.direction.x * self.speed * deltatime
            self.y += self.direction.y * self.speed * deltatime

    def update(self):
        if not self.exploded:
            if self.y >= self.target_pos_y:
                play_sound(sound_dict['explosion_sound'])
                self.exploded = True
                self.updat = 0
        else:
            self.change_frame(1, None)
            self.hitbox.centerx = self.x + self.rotate_im.get_width() / 2
            self.hitbox.centery = self.y + self.rotate_im.get_height() / 2

    def change_frame(self, deltatime, enemy):
        if self.exploded:
            self.updat += 0.01 * deltatime
            if self.updat >= 8:
                self.updat = 7
            self.im = self.frame[int(self.updat)]
            self.rotate_im = pygame.transform.rotate(self.im, -self.angle)

    def extinction_condition(self, bg_rect, c_rect):
        if self.exploded and self.updat >= 7:
            return True
        return False

    def drawing(self, background):
        background.blit(self.rotate_im, (self.x, self.y))

class Dagger(Move_weapon):
    def __init__(self, im, hitbox, x, y, target_pos_x, target_pos_y, distance, damage):
        super().__init__(im, hitbox, x, y, target_pos_x, target_pos_y, damage)

        self.distance = distance
        self.pause = 200
        self.c_x, self.c_y = target_pos_x, target_pos_y
        self.speed = 2
        self.original_im = self.rotate_im
        self.return_t = False

    def extinction_condition(self, bg_rect, c_rect):
        if self.return_t and c_rect.colliderect(self.hitbox):
            return True
        else:
            return False

    def move(self, deltatime, c_x, c_y):
        distance_to_center = ((self.c_x - self.x) ** 2 + (self.c_y - self.y) ** 2) ** 0.5
        if distance_to_center < self.distance and self.return_t == False:
            self.x += self.direction.x * self.speed * deltatime
            self.y += self.direction.y * self.speed * deltatime
        else:
            if self.pause <= 0:
                character_pos = pygame.Vector2(c_x, c_y)
                current_pos = pygame.Vector2(self.x, self.y)
                self.direction = (character_pos - current_pos).normalize()
                self.x += self.direction.x * self.speed * deltatime
                self.y += self.direction.y * self.speed * deltatime
                self.rotate_im = pygame.transform.rotate(self.original_im, 180)
            else:
                if self.pause >= 30:
                    self.rotate_im = pygame.transform.rotate(self.original_im, self.pause * 6)
                else:
                    target_pos = pygame.Vector2(c_x, c_y)
                    character_pos = pygame.Vector2(self.x, self.y)
                    self.direction = (target_pos - character_pos).normalize()
                    self.angle = math.degrees(math.atan2(c_y - self.y, c_x - self.x))
                    self.rotate_im = pygame.transform.rotate(self.im, -self.angle)
                    self.rotated_rect = self.rotate_im.get_rect(center=(self.x, self.y))
                self.return_t = True
                self.pause -= 0.1 * deltatime

class Star(Move_weapon):
    def __init__(self, im, hitbox, x, y, angle, target_pos_y, damage):
        super().__init__(im, hitbox, x, y, angle, target_pos_y, damage)

        self.center_x = x
        self.center_y = y
        self.radius = 200
        self.angle = angle
        self.distance = 0
        self.shrinking = False

    def update(self):
        self.hitbox.left = self.x + self.hitbox.width // 2
        self.hitbox.top = self.y + self.hitbox.height // 2

    def move(self, deltatime, c_x, c_y):
        self.angle += 0.001 * deltatime
        cos = math.cos(self.angle)
        sin = math.sin(self.angle)
        self.x = self.center_x + self.radius * cos
        self.y = self.center_y + self.radius * sin
        if not self.shrinking:
            self.distance += abs(sin) + abs(cos)
            if self.distance >= 600:
                self.shrinking = True
        if self.shrinking:
            self.radius -= 0.1 * deltatime

    def extinction_condition(self, bg_rect, c_rect):
        if self.shrinking and self.hitbox.colliderect(c_rect):
            return True
        return False

class Staff(Move_weapon):
    def __init__(self, im, hitbox, x, y, target_pos_x, target_pos_y, damage):
        super().__init__(im, hitbox, x, y, target_pos_x, target_pos_y, damage)

    def extinction_condition(self, bg_rect, c_rect):
        if not bg_rect.colliderect(self.hitbox):
            return True
        else:
            return False

class Mine(Weapon_effect):
    def __init__(self, frame, x, y, hitbox, target_pos_x, target_pos_y, damage):
        super().__init__(frame, hitbox, x, y, target_pos_x, target_pos_y, damage)
        self.updat = 0
        self.im = frame[0]
        self.frame = frame
        self.exploded = False

    def update(self):
        self.hitbox.left = self.x + self.hitbox.width
        self.hitbox.top = self.y + self.hitbox.height

    def drawing(self, background):
        background.blit(self.im, (self.x, self.y))

    def extinction_condition(self, bg_rect, c_rect):
        if self.exploded and self.updat >= 8 or not bg_rect.colliderect(self.hitbox):
            play_sound(sound_dict['explosion_sound'])
            return True
        return False

    def change_frame(self, deltatime, enemy):
        for i in enemy:
            if i.colliderect(self.hitbox):
                self.exploded = True
        if self.exploded:
            self.updat += 0.02 * deltatime
            if self.updat >= len(self.frame):
                self.updat = len(self.frame) - 1
            self.im = self.frame[int(self.updat)]
            self.rotate_im = self.im

    def move(self, deltatime, c_x, c_y):
        pass

class Sword(Weapon_effect):
    def __init__(self, frame, x, y, hitbox, target_pos_x, target_pos_y, damage):
        super().__init__(frame, x, y, hitbox, target_pos_x, target_pos_y, damage)
        self.updat = 0
        self.im = frame[0]
        self.x -= self.im.get_width() // 2
        self.y -= self.im.get_height() // 2
        self.frame = frame
        self.rotate_im = self.im

    def screen_move(self, x_speed, y_speed, deltatime):
        pass

    def extinction_condition(self, bg_rect, c_rect):
        if self.updat >= 8:
            return True
        else:
            self.rotate_im = self.frame[int(self.updat)]
            return False


    def change_frame(self, deltatime, enemy_l):
        self.updat += 0.02 * deltatime

