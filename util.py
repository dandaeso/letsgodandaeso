import pygame
import random
import math
import pandas as pd
import os
pygame.init()
dummy_surface = pygame.Surface((640, 480))
map_l=[['mushroom', 'goblin', 'slime', 'pumkin'],
        ['ghost', 'skeleton', 'pumkin', 'zombie'],
        ['turtle', 'shellfish', 'slime','jellyfish'],
        ['cactus', 'desert_goblin', 'skeleton', 'pharaoh']]
base_path = os.path.dirname(__file__)
full_path = os.path.join(base_path,'assets/skill_data.csv')
skill_data_df=pd.read_csv(full_path,encoding='utf-8')

full_path = os.path.join(base_path,'assets/skill_explanation.csv')
skill_explanation_df=pd.read_csv(full_path,encoding='utf-8')

full_path = os.path.join(base_path,'assets/word.ttf')
custom_font18 = pygame.font.Font(full_path, 18)


full_path = os.path.join(base_path,'assets/word.ttf')
custom_font24 = pygame.font.Font(full_path, 24)

full_path = os.path.join(base_path,'assets/word1.ttf')
custom_font24b = pygame.font.Font(full_path, 24)


def get_im(path):
    print("d")
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, path)
    image = pygame.image.load(full_path)
    return image
    
def text_draw(text, tx, ty, size,alpha, background,  outline=False,color=False,pos=False):
    if color:
            text_color = (245, 245, 245)
    elif outline:
        text_color = (255, 0, 0)
    else:
        text_color = (0, 0, 0)

    if size==18:
        text_render = custom_font18.render(text, True, text_color)
    elif outline:
        text_render = custom_font24b.render(text, True, text_color)
    else:
        text_render = custom_font24.render(text, True, text_color)
        
    text_render.set_alpha(256-alpha*5)
    if pos:
        text_rect = text_render.get_rect(center=(tx, ty))
    else:
        text_rect = text_render.get_rect(topleft=(tx, ty))
    background.blit(text_render, text_rect)


def get_text(type, level):
    if type in skill_explanation_df.columns:
        return skill_explanation_df[type].iloc[level]
def get_data(type, level):
    available_buff=["Damage","defense","magnet","vampirism","execute","luck"]
    if type in available_buff:
        if type in skill_data_df.columns:
            if type=="vampirism":
                return skill_data_df[type].iloc[level].split(" ")
            else:
                return skill_data_df[type].iloc[level]
    else:
        if type in skill_data_df.columns:
            return skill_data_df[type].iloc[level-1].split(" ")

def probability(percentage):
    value=random.randint(1,100)
    if value<=percentage:
        return True
    return False
def get_random_position(c_x, c_y, distance):
    angle = random.uniform(0, 360)

    angle_rad = math.radians(angle)

    random_x = c_x + distance * math.cos(angle_rad)
    random_y = c_y + distance * math.sin(angle_rad)
    
    return random_x,random_y

