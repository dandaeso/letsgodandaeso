import pygame
import random
import math
import pandas as pd
pygame.init()
map_l=[['mushroom', 'goblin', 'slime', 'pumkin'],
        ['ghost', 'skeleton', 'pumkin', 'zombie'],
        ['turtle', 'shellfish', 'slime','jellyfish'],
        ['cactus', 'desert_goblin', 'skeleton', 'pharaoh']]
skill_data_df = pd.read_csv('assets/skill_data.csv',encoding='utf-8')
skill_explanation_df = pd.read_csv('assets/skill_explanation.csv',encoding='utf-8')
image_cache = {}
font_path = 'assets/word.ttf'
font_path1 = 'assets/word1.ttf'
custom_font18 = pygame.font.Font(font_path, 18)
custom_font24 = pygame.font.Font(font_path, 24)
custom_font24b = pygame.font.Font(font_path1, 24)
image_cache = {}

#이미지를 캐싱하는 함수(예시)
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

