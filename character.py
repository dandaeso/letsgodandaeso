import pygame
import spritesheet
from util import *
class Character():
    def __init__(self,speed,center_x,center_y,health=50,max_health=50,direction="right",updat=12,level=1):
        character_im=get_im("assets/enemy_frame/character_spritesheet.png").convert_alpha()
        character_sheet = spritesheet.SpriteSheet(character_im)
        self.frame=[]
        for i in range(2):
            for j in range(8):
                self.frame.append(character_sheet.get_image(j,i,64,64, 2,(0,0,0)))
        self.health=health
        self.max_health=max_health
        self.im=self.frame[0]
        self.speed=speed
        self.hitbox=pygame.rect.Rect(0,0,64,64)
        self.hitbox.centerx=center_x
        self.hitbox.centery=center_y
        self.direction=direction
        self.updat=updat
        self.level=level
        self.death_c=True
    def screen_move_check(self,key_pressed,deltatime,scroll_x,scroll_y):
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            scroll_x -= self.speed * deltatime
            self.direction = "right"
        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            scroll_x += self.speed * deltatime
            self.direction = "left"
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
            scroll_y += self.speed * deltatime
        elif key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
            scroll_y -= self.speed * deltatime
        return scroll_x,scroll_y
    def change_frame(self,move,deltatime):
        self.updat+=0.015*deltatime
        if self.health>=0:
            if move:
                if self.updat>=13:
                    self.updat=6
            else:
                self.updat-=0.013*deltatime
                if self.updat>=14 or self.updat<=12:
                    self.updat=12
        elif self.updat>=5.8 and self.death_c:
            self.updat=0
            self.death_c=False
        elif self.updat>=5.8:
            return True


        if self.direction=="left":
            self.im = pygame.transform.flip(self.frame[int(self.updat)],True,False)
            self.im.set_colorkey((0,0,0))
        else:
            self.im = self.frame[int(self.updat)]

    def drawing(self,background):
        character_circle_surface = pygame.Surface((self.hitbox.width-10,25), pygame.SRCALPHA)
        pygame.draw.ellipse(character_circle_surface, (0,0,0,128), (0,0,self.hitbox.width-10,25))
        background.blit(character_circle_surface, (self.hitbox.left+5,self.hitbox.bottom-20))
        background.blit(self.im,(self.hitbox.left-self.hitbox.width//2,self.hitbox.top-self.hitbox.height//2))
        #pygame.draw.rect(background,(255,0,0),self.hitbox,5)


    def draw_health(self, background):
        ratio = self.health / self.max_health
        pygame.draw.rect(background, (240,0,0), (self.hitbox.left, self.hitbox.bottom,self.hitbox.width,15))
        pygame.draw.rect(background,(0,240,0), (self.hitbox.left, self.hitbox.bottom,self.hitbox.width * ratio,15))
        

        
