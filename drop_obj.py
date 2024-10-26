import random
import pygame
class Exp():
    def __init__(self,im,x,y,hitbox):
        self.situ=False
        self.type="exp"
        self.im=im
        self.im = pygame.transform.scale(self.im, (175,175))
        self.x=x+random.randint(-40,40)
        self.y=y+random.randint(-40,40)
        self.hitbox=hitbox
        
    def screen_move_check(self,key_pressed,deltatime,speed):
        if key_pressed[pygame.K_RIGHT]or key_pressed[pygame.K_d]:
            self.screen_move(-speed,0,deltatime)
        elif key_pressed[pygame.K_LEFT]or key_pressed[pygame.K_a]:
            self.screen_move(speed,0,deltatime)
        if key_pressed[pygame.K_UP]or key_pressed[pygame.K_w]:
            self.screen_move(0,speed,deltatime)
        elif key_pressed[pygame.K_DOWN]or key_pressed[pygame.K_s]:
            self.screen_move(0,-speed,deltatime)

    def updat(self):
        self.hitbox.right=self.x+self.im.get_size()[0]//2
        self.hitbox.bottom=self.y+self.im.get_size()[1]//2
        
    def screen_move(self,x_speed,y_speed,deltatime):
        self.x+=x_speed*deltatime
        self.y+=y_speed*deltatime

    def drawing(self, background):
        exp1_circle_surface = pygame.Surface((self.hitbox.width,25), pygame.SRCALPHA)
        pygame.draw.ellipse(exp1_circle_surface, (0,0,0,128), (0,0,self.hitbox.width,25))
        background.blit(exp1_circle_surface, (self.hitbox.left,self.hitbox.bottom-20))

        background.blit(self.im, (self.x - self.hitbox.width // 2, self.y - self.hitbox.height // 2))
        #pygame.draw.rect(background, (0, 0, 255), self.hitbox, 5)

    def magnetic(self,deltatime,character_x,character_y):
        player_pos = pygame.Vector2([self.hitbox.centerx,self.hitbox.centery])
        enemy_pos = pygame.Vector2([character_x,character_y])
        direction = (player_pos - enemy_pos).normalize()
        self.x-=deltatime*direction.x
        self.y-=deltatime*direction.y
class Meet(Exp):
    def __init__(self,im,x,y,hitbox):
        super().__init__(im,x,y,hitbox)
        self.type="meet"
class Magnetic(Exp):
    def __init__(self,im,x,y,hitbox):
        super().__init__(im,x,y,hitbox)
        self.type="magnetic"





