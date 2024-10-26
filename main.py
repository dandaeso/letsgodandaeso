import pygame
import random
import button
import traceback
import math
pygame.init()
background = pygame.display.set_mode((1280, 810))
import enemy
import weapon
import character
import spritesheet
import drop_obj
import boss
from util import *
import effect
import boss_pattern  

if True:
    select_im=get_im('assets/select.png')
    pygame.display.set_caption("Mobmania")
    b_size = background.get_size()
    play = 1
    fps = pygame.time.Clock()
    clock = pygame.time.Clock()

    fail_im = get_im("assets/fail.png")
    im_d = get_im("assets/im.png")
    fail_im = pygame.transform.rotate(fail_im,-25)
    fail_frame=[pygame.transform.scale(fail_im,(fail_im.get_width()//13*(20-i),fail_im.get_height()//13*(20-i))) for i in range(12)]


    clear_im=get_im("assets/clear.png")
    clear_im = pygame.transform.rotate(clear_im,-25)
    clear_frame=[pygame.transform.scale(clear_im,(clear_im.get_width()//13*(20-i),clear_im.get_height()//13*(20-i))) for i in range(12)]

    frame=0

    logo_im = pygame.transform.scale(get_im("assets/logo.png"), (960, 540))

    ui_l = []
    for i in range(6):
        im = get_im(f"assets/ui/sprite_{i}.png")
        ui_l.append(pygame.transform.scale(im, (64, 64)))

    for i in range(6):
        im = get_im(f"assets/ui/sprites_{i}.png")
        ui_l.append(pygame.transform.scale(im, (64, 64)))

    im7 = pygame.transform.scale(get_im("assets/ui/sprite.png"), (288, 64))

    pos_im = get_im("assets/pos.png")

    exp_im = get_im("assets/drop_obj/exp.png")
    magnetic_im = get_im("assets/drop_obj/magnetic.png")
    meet_im = get_im("assets/drop_obj/meet.png")
    show_stat1 = get_im("assets/show_stat1.png")
    show_stat2 = get_im("assets/show_stat2.png")

    weapon_0 = get_im("assets/weapon/dagger.png")
    weapon_1 = get_im("assets/weapon/star.png")
    weapon_2 = get_im("assets/weapon/staff.png")

    wave_frame = []
    for i in range(1, 236):
        if i < 10:
            wave_im = get_im(f"assets/boss_wave_f/sprite_00{i}.png")
        elif i < 100:
            wave_im = get_im(f"assets/boss_wave_f/sprite_0{i}.png")
        else:
            wave_im = get_im(f"assets/boss_wave_f/sprite_{i}.png")
        wave_frame.append(wave_im)

    sword_im = get_im("assets/weapon/sword.png")
    sword_sheet = spritesheet.SpriteSheet(sword_im)
    sword_frame = []
    for i in range(2):
        for j in range(8):
            sword_frame.append(sword_sheet.get_image(j, i, 64, 64, 1, (0, 0, 0)))

    map_im_l = []
    s_map_im_l = []
    for i in range(4):
        im = get_im(f"assets/map/map{i}.png")
        im = pygame.transform.scale(im, (im.get_width() * 7, im.get_height() * 6))
        map_im_l.append(im)
        im = pygame.transform.scale(im, (im.get_width() * 0.7, im.get_height() * 0.6))
        s_map_im_l.append(im)

    cooltime_frame = []
    for i in range(17):
        im = get_im(f"assets/cooltime/cooltime{i}.png")
        im.set_alpha(200)
        cooltime_frame.append(im)

    missile_im = get_im("assets/weapon/missile.png")
    missile_sheet = spritesheet.SpriteSheet(missile_im)
    missile_frame = []
    for i in range(2):
        for j in range(8):
            im = missile_sheet.get_image(j, i, 64, 64, 3, (0, 0, 0))
            missile_frame.append(im)

    mine_im = get_im("assets/weapon/mine.png")
    mine_sheet = spritesheet.SpriteSheet(mine_im)
    mine_frame = []
    for i in range(2):
        for j in range(8):
            im = mine_sheet.get_image(j, i, 64, 64, 3, (0, 0, 0))
            mine_frame.append(im)

    screen_image = [pygame.transform.scale(get_im(f"assets/ground{i}.png"), (1280, 810)) for i in range(1, 5)]

    bg_width, bg_height = background.get_size()
    scroll_x = 0
    scroll_y = 0
    screen_rect = pygame.Rect(0, 0, bg_width, bg_height)
    back = get_im("assets/back.png")
    game="lose"
    rect2 = pygame.Surface((1280, 80), pygame.SRCALPHA)
    rect2.fill((0, 0, 0, 128))
    reset=True
    rect4 = pygame.Surface((80, 24), pygame.SRCALPHA)
    rect4.fill((0, 0, 0, 128))
    rect4.set_alpha(220)

    image1 = get_im("assets/buttons/button0_0.png")
    image2 = get_im("assets/buttons/button1_0.png")
    image3 = pygame.transform.scale(get_im("assets/buttons/button3.png"), (537.6, 806.4))
    image4 = get_im("assets/buttons/button2.png")
    image5 = get_im("assets/buttons/button0_1.png")
    image6 = get_im("assets/buttons/button1_1.png")
    levelup_l = [get_im(f"assets/LEVEL_UP/sprite_{i}.png") for i in range(4)]

    rect_surface = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
    rect_surface.fill((0, 0, 0, 128))
    rect_surface.set_alpha(164)
    clear_map=[]
    damage_mount=0
    heal_mount=0
    damaged_mount=0
    move_len=0
    execute_count=0

    rect_surface1 = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
    rect_surface1.fill((0, 0, 0, 128))
    menu_button = []
    menu_button_rect = []
    for i in range(4):
        menu_button.append(get_im(f"assets/menu_button/button{i}.png"))
    for i in range(4):
        menu_button.append(pygame.transform.scale(get_im(f"assets/menu_button/button{i}.png"), (220 * 0.8, 200 * 0.8)))

    center_x,center_y=bg_width//2,bg_height//2
    menu_button_rect.append(pygame.rect.Rect(center_x-384,center_y,232,192))
    menu_button_rect.append(pygame.rect.Rect(center_x-menu_button[3].get_width()//2,center_y,232,192))
    menu_button_rect.append(pygame.rect.Rect(center_x+384-menu_button[3].get_width(),center_y,232,192))
    map_type=0

    available_buff=["Damage","defense","magnet","vampirism","execute","luck"] # 선택 가능한 무기 리스트
    korean_weapon_name=["암살용 단검","불의 지팡이","유성우","대공미사일","대형지뢰","카타나","대미지 증가","방어력 증가","자력범위증가","흡혈","처형","행운"]

    explanation=["푸른 초원","어두운 할로윈","밝은 바다","텁텁한 사막"]
    map_l=[['mushroom', 'goblin', 'slime', 'pumkin'],
           ['ghost', 'skeleton', 'pumkin', 'zombie'],
           ['turtle', 'shellfish', 'slime','jellyfish'],
           ['cactus', 'desert_goblin', 'skeleton', 'pharaoh']]

    challenge_name=["처형자","폭격기","흡혈귀","마라토너","탱크","학살자","승리자"]
    challenge_explanation=['"프랑스의 악몽"','"때린다. 그뿐."','"죽기가 더 힘들지 않았나요?"','"도망친건가요?"','"꽤 아팠겠는걸요"','"좋은 뜻은 아닌것 같네요."',"고마워요!"]
    challenge_condition=["한판에 44마리 이상의 적을 처형하세요.",
                        "한판에 50000이 넘는 대미지를 넣으세요.",
                        '한판에 77이상의 체력을 흡혈하세요.',
                        '한판에 15000이상의 거리를 이동하세요.',
                        '한판에 120이상의 대미지를 받으세요.',
                        '한판에 150마리가 넘는 적을 처치하세요.',
                        '모든맵을 클리어하세요.']

    challenge_check=[False,False,False,False,False,False,False]
    #challenge_check=[True,True,True,True,True,True,True]
    back_rect=pygame.rect.Rect(0,bg_height-64,64,64)
    show_stat=False
    sequence="menu"
    rect1=[]
    rect1.append(pygame.Rect(center_x-image3.get_size()[0]//2,
                            center_y-image3.get_size()[1]//2,
                            image3.get_size()[0],
                            image3.get_size()[1]))
    first_iteration = True
    y_scroll=0
    tear = [
    "F-", "F", "F+", 
    "E-", "E", "E+", 
    "D-", "D", "D+", 
    "C-", "C", "C+", 
    "B-", "B", "B+", 
    "A-", "A", "A+", 
    "S-", "S", "S+"
]
    challenge=False

while play:
    scroll_x %= bg_width
    scroll_y %= bg_height
    map_type%=4
    clock.tick(60)
    m_x, m_y = pygame.mouse.get_pos()
    deltatime = fps.tick(60)
    key_pressed=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL and y_scroll>-1500 and y_scroll<1000:
            y_scroll += event.y * 0.8 * deltatime
        elif  y_scroll>1000:
            y_scroll +=  -0.1 * deltatime
        elif  y_scroll<-1500:
            y_scroll +=  0.1 * deltatime
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYUP: 
            if  gameover:
                if event.key == pygame.K_SPACE:
                    sequence = "menu"
                    reset=True
            if  sequence == "select_map":
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    map_type += 1
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    map_type -= 1
                if event.key == pygame.K_RETURN:
                    sequence = "game"

        if event.type == pygame.MOUSEBUTTONUP:
            if sequence == "select_map" or sequence == "challenge":
                if back_rect.collidepoint((m_x, m_y)):
                    sequence = "menu"
            if sequence=="menu":
                for rect in menu_button_rect:
                    if rect.collidepoint((m_x,m_y)):
                        if  menu_button_rect.index(rect)==0:
                            sequence="select_map"
                        elif  menu_button_rect.index(rect)==1:
                            sequence="challenge"
                        elif  menu_button_rect.index(rect)==2:
                            play=False
            if sequence=="game":
                if rect3_hitbox.collidepoint((m_x,m_y)):
                    if show_stat:
                        show_stat=False
                    else:
                        show_stat=True
    if reset:
        y_scroll=0
        frame=0
        available_weapons = ["Dagger", "Staff", "Star", "Missile", "Mine", "Sword"]
        level_limit = 30

        boss_attack=[]
        drop_obj_l=[]
        attackeffect_l=[]
        enemy_l=[]
        draw_l=[]
        select_skill=[]
        buttons=[]
        level_animation=0

        game="lose"

        reset=False

        damage_mount=0
        heal_mount=0
        damaged_mount=0
        move_len=0
        execute_count=0

        re_count=100
        monster_kill_count=0
        enemy_mount=7
        wave=0
        boss_wave=1
        draw_l=[]
        enemy_l=[]
        character1=character.Character(0.09,center_x,center_y)

        time=0
        wave_time=0

        skill_data_l=[]

        skill_data_l.append(weapon.Dagger_Data(character1,[bg_width,bg_height],"Dagger"))
        skill_data_l.append(weapon.Staff_Data(character1,[bg_width,bg_height],"Staff"))
        skill_data_l.append(weapon.Star_Data(character1,[bg_width,bg_height],"Star"))
        skill_data_l.append(weapon.Missile_Data(character1,[bg_width,bg_height],"Missile"))
        skill_data_l.append(weapon.Mine_Data(character1,[bg_width,bg_height],"Mine"))
        skill_data_l.append(weapon.Sword_Data(character1,[bg_width,bg_height],"Sword"))

        for i in range(6):
            skill_data_l.append(weapon.Buff_data(available_buff[i]))

        show_stat=False
        exp_mount=30
        frame_counter = 0
        damage_multiplier=1
        defense_multiplier=1
        magnet_multiplier=1
        vampirism_probability=0
        vampirism=0
        execute=0
        gameover=False
        luck=0
        order=[]
        order1=[]
    for x in range(-bg_width, bg_width + bg_width, bg_width):
        for y in range(-bg_height, bg_height + bg_height, bg_height):
            background.blit(screen_image[map_type%4], (x + scroll_x, y + scroll_y))
    if execute_count>=44:
        challenge_check[0]=True
        challenge=True
    if damage_mount>=50000:
        challenge_check[1]=True
        challenge=True
    if heal_mount>=77:
        challenge_check[2]=True
        challenge=True
    if move_len>=15000:
        challenge_check[3]=True
        challenge=True
    if damaged_mount>=120:
        challenge_check[4]=True
        challenge=True
    if monster_kill_count>=150:
        challenge=True
        challenge_check[5]=True
    if "0" in clear_map and "1" in clear_map and "2" in clear_map and "3" in clear_map:
        challenge=True
        challenge_check[6]=True
    if sequence=="menu":
        rect_surface.set_alpha(128)
        background.blit(rect_surface, (0, 0))
        background.blit(logo_im,(center_x-logo_im.get_width()//2,center_y-450))
        background.blit(menu_button[0],(center_x-384,center_y))
        background.blit(menu_button[1],(center_x-menu_button[1].get_width()//2,center_y))
        background.blit(menu_button[2],(center_x+268-menu_button[2].get_width()//2,center_y))
        scroll_x-=0.03*deltatime
        scroll_y+=0.03*deltatime
        pygame.display.flip()
    elif sequence=="challenge":
        challenge=False
        scroll_x+=0.03*deltatime
        scroll_y+=0.03*deltatime
        rect_surface.set_alpha(256)
        background.blit(rect_surface, (0, 0))
        background.blit(back,(0,bg_height-64))
        text_draw(f'도전과제 목록',bg_width//2,y_scroll+25,28,0,background,True,True,True)
        for i in range(len(challenge_explanation)):
            background.blit(select_im,(bg_width//2-select_im.get_width()//2,y_scroll+90+i*300))
            if challenge_check[i]:
                text_draw(f'{challenge_name[i]}',bg_width//2,y_scroll+120+i*300,28,0,background,True,True,True)
                text_draw(f'{challenge_explanation[i]}',bg_width//2,y_scroll+200+300*i,24,0,background,True,True,True)
            else:
                text_draw(f'?'*len(challenge_name[i]),bg_width//2,y_scroll+120+i*300,28,0,background,True,True,True)
                text_draw(f'{challenge_condition[i]}',bg_width//2,y_scroll+200+i*300,24,0,background,True,True,True)
        pygame.display.flip()
    elif sequence=="select_map":
        background.blit(rect_surface, (0, 0))
        background.blit(back,(0,bg_height-64))
        background.blit(s_map_im_l[(map_type-1)%4],(center_x-448-s_map_im_l[map_type%4].get_width()//2,center_y+75-s_map_im_l[map_type%4].get_height()//2))
        background.blit(s_map_im_l[(map_type+1)%4],(center_x+448-s_map_im_l[map_type%4].get_width()//2,center_y+75-s_map_im_l[map_type%4].get_height()//2))
        background.blit(logo_im,(center_x-logo_im.get_width()//2,-140))
        background.blit(map_im_l[map_type%4],(center_x-map_im_l[map_type%4].get_width()//2,center_y+55-map_im_l[map_type%4].get_height()//2))
        background.blit(im_d,(center_x-im_d.get_width()//2,center_y+55-im_d.get_height()//2))
        scroll_x+=0.03*deltatime
        scroll_y+=0.03*deltatime
        text_draw(f'STAGE.{(map_type%4)+1} "{explanation[map_type%4]}"',bg_width//2,bg_height-100,28,0,background,True,True,True)
        text_draw(f"Enter키로 플레이",bg_width//2,bg_height-60,24,0,background,True,True,True)
        text_draw(f"화살표키나 A 또는 D로 맵 변경",bg_width//2,bg_height-25,18,0,background,True,True,True)
        pygame.display.flip()
    elif sequence=="game":

        for attack in boss_attack:
            attack.drawing(background)

        for obj in drop_obj_l:
            obj.updat()
            obj.drawing(background)

        for attack in attackeffect_l:
            attack.drawing(background)

        for enemy1 in enemy_l:
            enemy1.select_speed(character1.hitbox.centerx,character1.hitbox.centery)
            if screen_rect.colliderect(enemy1.hitbox):
                enemy1.drawing(background)
            enemy1.updat()
            enemy1.flip_im()
            enemy_hitbox.append(enemy1.hitbox)
        for dh in draw_l:
            dh.drawing(background)
            if dh.move(deltatime):
                draw_l=[i for i in draw_l if not i==dh]

        background.blit(rect2,(0,bg_height-138))            
        background.blit(pos_im,(0,bg_height-138))
        character1.drawing(background)
        character1.draw_health(background)

        background.blit(rect4,(bg_width//2-40,0))
        text_draw(f"{int(time//60)} : {int(time)%60}",bg_width//2,10,24,0,background,True,True,True)
        for weapon_data in skill_data_l:
            if weapon_data.level!=0:
                try:
                    if weapon_data.name == "Dagger":
                        background.blit(ui_l[0],(133+order.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name == "Staff":
                        background.blit(ui_l[1],(133+order.index(weapon_data.name)*73,bg_height-130)) 
                    elif weapon_data.name == "Star":
                        background.blit(ui_l[2],(133+order.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name == "Missile":
                        background.blit(ui_l[3],(133+order.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name == "Mine":
                        background.blit(ui_l[4],(133+order.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name == "Sword":
                        background.blit(ui_l[5],(133+order.index(weapon_data.name)*73,bg_height-130))
                    if weapon_data.name=="Damage":
                        background.blit(ui_l[6],(717+order1.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name=="defense":
                        background.blit(ui_l[7],(717+order1.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name=="magnet":
                        background.blit(ui_l[8],(717+order1.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name=="vampirism":
                        background.blit(ui_l[9],(717+order1.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name=="execute":
                        background.blit(ui_l[10],(717+order1.index(weapon_data.name)*73,bg_height-130))
                    elif weapon_data.name=="luck":
                        background.blit(ui_l[11],(717+order1.index(weapon_data.name)*73,bg_height-130))
                    if not weapon_data.name in available_buff:
                        ratio = weapon_data.cooltime / weapon_data.get_cooltime_limit()
                        index_value = int(ratio * 17)
                        background.blit(cooltime_frame[index_value],(133+order.index(weapon_data.name)*73,bg_height-130))
                        if weapon_data.get_cooltime_limit()-weapon_data.cooltime<=1.25:
                            text_draw(f"{(weapon_data.get_cooltime_limit()-weapon_data.cooltime):.1f}",148+order.index(weapon_data.name)*73,bg_height-108,28,0,background,True,True)
                except ValueError:
                    if weapon_data.name in available_buff:
                        order1.append(weapon_data.name)
                    else:
                        order.append(weapon_data.name)
                except IndexError:
                    pass
        if challenge:
            text_draw("도전과제 달성!",bg_width-150,0,28,0,background,True,True)
        if show_stat:
            rect3 = pygame.Surface((186, 465), pygame.SRCALPHA)
            rect3.fill((0, 0, 0, 128))
            rect3.set_alpha(220)
            background.blit(rect3,(0,130))
            text_draw(f"상태창  lv.{character1.level}", 25, 140, 28, 0, background, True, True)
            text_draw(f"체력: {character1.max_health}.0/{character1.health:.1f}", 30, 188, 18, 0, background, True, True)
            text_draw(f"공격력 : {damage_multiplier:.1f}", 30, 236, 18, 0, background, True, True)
            text_draw(f"방어력 : {defense_multiplier:.1f}", 30, 284, 18, 0, background, True, True)
            text_draw(f"자력범위 : {magnet_multiplier:.1f}", 30, 332, 18, 0, background, True, True)
            text_draw(f"흡혈확률 : {vampirism_probability:.1f}%", 30, 380, 18, 0, background, True, True)
            text_draw(f"흡혈량 : {vampirism:.1f}%", 30, 428, 18, 0, background, True, True)
            text_draw(f"처형확률 : {execute:.1f}%", 30, 476, 18, 0, background, True, True)
            text_draw(f"행운 : {luck:.1f}%", 30, 524, 18, 0, background, True, True)
            text_draw(f"죽인 적의 수 : {monster_kill_count}", 30, 572, 18, 0, background, True, True)
            background.blit(show_stat1,(0,0))
        else:
            background.blit(show_stat2,(0,0)) 
            rect3_hitbox=pygame.rect.Rect(0,0,186,392)


        try:
            ratio = wave_time / 45
            index_value = int(ratio * 243)
            background.blit(wave_frame[index_value],(center_x-wave_frame[0].get_size()[0]//2,bg_height-115))
            if len(enemy_l)<enemy_mount:
                enemy_type = random.choice(map_l[map_type%4])
                if enemy_type == 'zombie':
                    enemy_l.append(enemy.Zombie())
                elif enemy_type == 'skeleton':
                    enemy_l.append(enemy.Skeleton())
                elif enemy_type == 'mushroom':
                    enemy_l.append(enemy.Mushroom())
                elif enemy_type == 'pumkin':
                    enemy_l.append(enemy.Pumkin())
                elif enemy_type == 'slime':
                    enemy_l.append(enemy.Slime())
                elif enemy_type == 'ghost':
                    enemy_l.append(enemy.Ghost())
                elif enemy_type == 'goblin':
                    enemy_l.append(enemy.Goblin())
                elif enemy_type == 'jellyfish':
                    enemy_l.append(enemy.Jellyfish())
                elif enemy_type == 'cactus':
                    enemy_l.append(enemy.Cactus())
                elif enemy_type == 'shellfish':
                    enemy_l.append(enemy.Shellfish())
                elif enemy_type == 'turtle':
                    enemy_l.append(enemy.Turtle())
                elif enemy_type == 'pharaoh':
                    enemy_l.append(enemy.Pharaoh())
        except IndexError:
            wave_time=100
            enemy_type = map_l[map_type%4][(boss_wave-1)%4]
            if enemy_type == 'zombie':
                enemy_l.append(boss.Zombie_Boss())
            elif enemy_type == 'skeleton':
                enemy_l.append(boss.Skeleton_Boss())
            elif enemy_type == 'mushroom':
                enemy_l.append(boss.Mushroom_Boss())
            elif enemy_type == 'pumkin':
                enemy_l.append(boss.Pumkin_Boss())
            elif enemy_type == 'slime':
                enemy_l.append(boss.Slime_Boss())
            elif enemy_type == 'ghost':
                enemy_l.append(boss.Ghost_Boss())
            elif enemy_type == 'goblin':
                enemy_l.append(boss.Goblin_Boss())
            elif enemy_type == 'jellyfish':
                enemy_l.append(boss.Jellyfish_Boss())
            elif enemy_type == 'cactus':
                enemy_l.append(boss.Cactus_Boss())
            elif enemy_type == 'shellfish':
                enemy_l.append(boss.Shellfish_Boss())
            elif enemy_type == 'turtle':
                enemy_l.append(boss.Turtle_Boss())
            elif enemy_type == 'pharaoh':
                enemy_l.append(boss.Pharaoh_Boss())

            background.blit(wave_frame[0],(center_x-wave_frame[0].get_size()[0]//2,bg_height-115))
            boss_wave+=1
            enemy_mount+=1
            wave_time=0
            wave=0
        ratio = exp_mount / level_limit
        pygame.draw.rect(background, (0,0,0), (0, bg_height-20,bg_width,20))
        pygame.draw.rect(background,(0,230, 255), (0, bg_height-20,bg_width * ratio,20))
        # 레벨업 및 스킬 선택
        if not gameover:
            if select_skill:
                background.blit(rect_surface, (0, 0))
                if not buttons:
                    buttons = []
                    buttons.append(button.Button(center_x, 100, 540, 0, image3, image3, (False, 0)))
                    random_type = random.sample(available_weapons, 3)
                    for i in range(3):
                        value = (random_type[i], skill_data_l[available_weapons.index(random_type[i])].level)
                        buttons.append(button.Button(center_x, 285 + 120 * i, 512, 104, image1, image5, value))
                    buttons.append(button.Button(center_x, 645, 512, 104, image2, image6, ("re", 0)))

                for button1 in buttons:
                    button1.draw(background, m_x, m_y)
                    if button1.button_type[0] == "re" and re_count <= 0:
                        button1.image1 = image4
                        button1.image2 = image4

                    for weapon_level in skill_data_l:
                        if button1.button_type[0] == weapon_level.name:
                            background.blit(ui_l[available_weapons.index(str(button1.button_type[0]))], 
                                            (button1.rect.left + 75, button1.rect.top + 28))
                            text_draw(get_text(button1.button_type[0], button1.button_type[1]), 
                                        button1.rect.centerx - 110, button1.rect.centery + 8, 18, 0, background)
                            text_draw((korean_weapon_name[available_weapons.index(button1.button_type[0])] + 
                                        f".lv{weapon_level.level + 1}"),
                                        button1.rect.centerx - 110, button1.rect.centery - 20, 28, 0, background)
                    if button1.rect.collidepoint((m_x, m_y)):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                if button1.button_type[0] == "re" and re_count > 0:
                                    buttons = []
                                    buttons.append(button.Button(center_x, 100, 540, 0, image3, image3, (False, 0)))
                                    random_type = random.sample(available_weapons, 3)
                                    for i in range(3):
                                        value = (random_type[i], skill_data_l[available_weapons.index(random_type[i])].level)
                                        buttons.append(button.Button(center_x, 285 + 120 * i, 512, 104, image1, image5, value))
                                    buttons.append(button.Button(center_x, 645, 512, 104, image2, image6, ("re", 0)))
                                    re_count -= 1
                                elif button1.button_type[0] == "re" and re_count < 0:
                                    button1.button_type[0] = 4
                                elif button1.button_type[0] == -1:
                                    pass
                                elif button1.button_type[0] != "re":
                                    if len(available_weapons) == 6:
                                        available_weapons += available_buff
                                    for skill in skill_data_l:
                                        if skill.name == button1.button_type[0]:
                                            skill.level += 1
                                            break
                                    select_skill = False
                                    buttons = []
                background.blit(levelup_l[int(level_animation)], 
                                (center_x - levelup_l[0].get_size()[0] // 2, 115))
                if first_iteration:
                    pygame.display.flip()
                    first_iteration = False
                else:
                    pygame.display.update(rect1)

                if level_animation >= 3.8:
                    level_animation = 0
                else:
                    level_animation += 0.1
            else:
                if exp_mount>=level_limit:
                    exp_mount-=level_limit
                    character1.level+=1
                    level_limit=character1.level**2//3+30
                    select_skill=True
                time+=0.001*deltatime
                wave_time+=0.001*deltatime
                first_iteration = True
                wave += 0.001 * deltatime
                if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_UP] or key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_d] or key_pressed[pygame.K_a] or key_pressed[pygame.K_w]or key_pressed[pygame.K_s]:
                    move=True
                    move_len+=character1.speed*deltatime
                else:
                    move=False
                if character1.change_frame(move,deltatime) and character1.health<=0:
                    gameover=True
                scroll_x,scroll_y=character1.screen_move_check(key_pressed,deltatime,scroll_x,scroll_y)
                # 무기 쿨타임 관리 및 생성
                for attack in boss_attack:
                    attack.screen_move_check(key_pressed,character1.speed,deltatime)
                    attack.update()
                    attack.move(deltatime)
                    if character1.hitbox.colliderect(attack.hitbox):
                        character1.health-=attack.damage
                    if attack.change_frame(deltatime) or (not screen_rect.colliderect(attack.hitbox) and attack.y>attack.target_y):
                        boss_attack=[i for i in boss_attack if not i==attack]

                for weapon_data in skill_data_l:
                    if weapon_data.name in available_buff:
                        if weapon_data.name=="Damage":
                            damage_multiplier=weapon_data.get_data()
                        elif weapon_data.name=="defense":
                            defense_multiplier=weapon_data.get_data()
                        elif weapon_data.name=="magnet":
                            magnet_multiplier=weapon_data.get_data()
                        elif weapon_data.name=="vampirism":
                            vampirism_probability,vampirism=weapon_data.get_data()
                        elif weapon_data.name=="execute":
                            execute=weapon_data.get_data()
                        elif weapon_data.name=="luck":
                            luck=weapon_data.get_data()
                    else:
                        weapon_data.cooltime += 0.001*deltatime
                        if weapon_data.cooltime >= weapon_data.get_cooltime_limit() and weapon_data.level!=0:
                            weapon_data.cooltime = 0
                            if weapon_data.name == "Dagger":
                                random_angle = random.randint(0, 179)
                                for i in range(int(weapon_data.get_repeat())):
                                    data = weapon_data.get_data(random_angle,weapon_data.get_repeat(),i, m_x, m_y)
                                    attackeffect_l.append(weapon.Dagger(*data))
                            
                            
                            elif weapon_data.name == "Staff":
                                for i in range(-1,int(weapon_data.get_repeat()-1)):
                                    data = weapon_data.get_data(0,weapon_data.get_repeat(), m_x, m_y)
                                    attackeffect_l.append(weapon.Staff(*data))
                            
                            
                            
                            elif weapon_data.name == "Star":
                                # Star 생성 코드
                                base_angle = random.uniform(0, 2 * math.pi)
                                for i in range(int(weapon_data.get_repeat())):
                                    data = weapon_data.get_data(base_angle,weapon_data.get_repeat(),i, m_x, m_y)
                                    attackeffect_l.append(weapon.Star(*data))
                        
                        
                            elif weapon_data.name == "Missile":
                                # Missile 생성 코드
                                for i in range(int(weapon_data.get_repeat())):
                                    data = weapon_data.get_data(0,weapon_data.get_repeat(), m_x, m_y)
                                    attackeffect_l.append(weapon.Missile(*data))
                            
                            
                            elif weapon_data.name == "Mine":
                                for i in range(int(weapon_data.get_repeat())):
                                    data = weapon_data.get_data(0,weapon_data.get_repeat(), m_x, m_y)
                                    attackeffect_l.append(weapon.Mine(*data))
                                    
                            
                            elif weapon_data.name == "Sword":
                                data = weapon_data.get_data(int(weapon_data.get_repeat()), m_x, m_y)
                                attackeffect_l.append(weapon.Sword(*data))
                for obj in drop_obj_l:
                    distance_obj = ((character1.hitbox.centerx - obj.hitbox.centerx)**2 + (character1.hitbox.centery - obj.hitbox.centery)**2)**0.5
                    if distance_obj<=100*magnet_multiplier:
                        obj.situ=True
                    if obj.situ:
                        try:
                            obj.magnetic(deltatime,character1.hitbox.centerx,character1.hitbox.centery)
                        except:
                            pass
                    obj.screen_move_check(key_pressed,deltatime,character1.speed)
                    if obj.hitbox.colliderect(character1.hitbox):
                        if obj.type=="exp":
                            exp_mount+=5
                        if obj.type=="meet":
                            character1.health=60
                        if obj.type=="magnetic":
                            for obj in drop_obj_l:
                                if obj:
                                    obj.situ=True
                        drop_obj_l=[i for i in drop_obj_l if not i==obj]

                for attack in attackeffect_l:     
                    try:
                        attack.move(deltatime,character1.hitbox.left,character1.hitbox.top)
                    except:
                        pass
                    attack.change_frame(deltatime,enemy_hitbox)
                    attack.update()
                    attack.screen_move_check(key_pressed,deltatime,character1.speed)

                    if attack.extinction_condition(screen_rect,character1.hitbox) :
                        attackeffect_l=[ i for i in attackeffect_l if not i==attack]
                enemy_hitbox=[]
                for enemy1 in enemy_l:
                    try:
                        if enemy1.health==0:
                            enemy1.health-=1
                        enemy1.screen_move_check(key_pressed,character1.speed,deltatime)
                        if enemy1.name=="boss":
                            if enemy1.pattern_time>=enemy1.pattern_limit:
                                enemy1.pattern_time=0
                                enemy1.pattern_limit=random.randint(5,10)
                                if random.randint(0,1)==0:
                                    for i in range(random.randint(2,5)):
                                        if enemy1.type=="pumkin" and map_type%4==0:
                                            boss_attack.append(boss_pattern.pumkin_pattern1())
                                        elif enemy1.type=="zombie":
                                            boss_attack.append(boss_pattern.zombie_pattern1())
                                        elif enemy1.type=="pharaoh":
                                            boss_attack.append(boss_pattern.pharaoh_pattern1())
                                        elif enemy1.type=="jellyfish":
                                            boss_attack.append(boss_pattern.jellyfish_pattern1())
                                else:
                                    for i in range(random.randint(2,4)):
                                        if enemy1.type=="pumkin" and map_type%4==0:
                                            boss_attack.append(boss_pattern.pumkin_pattern2())
                                        if enemy1.type=="zombie":
                                            boss_attack.append(boss_pattern.zombie_pattern2())
                                        if enemy1.type=="pharaoh":
                                            boss_attack.append(boss_pattern.pharaoh_pattern2())
                                        elif enemy1.type=="jellyfish":
                                            boss_attack.append(boss_pattern.jellyfish_pattern2())
                                    
                            else:
                                enemy1.pattern_time+=0.001*deltatime
                        for enemy2 in enemy_l:
                            if enemy1.hitbox != enemy2.hitbox:
                                if enemy2.hitbox.colliderect(enemy1.hitbox):
                                    distance_enemy1 = ((character1.hitbox.left - enemy1.x)**2 + (character1.hitbox.top - enemy1.y)**2)**0.5
                                    distance_enemy2 = ((character1.hitbox.left - enemy2.x)**2 + (character1.hitbox.top - enemy2.y)**2)**0.5
                                    if enemy1.move_check and distance_enemy1 < distance_enemy2:
                                        enemy1.move_check = True
                                    else:
                                        enemy1.move_check = False
                                    collision_vector = pygame.Vector2(enemy1.x - enemy2.x, enemy1.y - enemy2.y).normalize()
                                    enemy1.x += collision_vector.x * enemy1.speed * deltatime*2
                                    enemy1.y += collision_vector.y * enemy1.speed * deltatime*2
                                    #벡터 nomalize해서 즉석으로 밀어내기
                        if character1.hitbox.colliderect(enemy1.hitbox):
                            character1.health-=enemy1.damage*defense_multiplier
                            damaged_mount+=enemy1.damage*defense_multiplier
                            enemy1.move_check = False
                            collision_vector = pygame.Vector2(enemy1.hitbox.left - character1.hitbox.left, enemy1.hitbox.top - character1.hitbox.top).normalize()
                            enemy1.x += collision_vector.x * enemy1.speed * deltatime*20 *character1.speed
                            enemy1.y += collision_vector.y * enemy1.speed * deltatime*20 *character1.speed
                        enemy1.damage_tick+=deltatime*0.05
                        if enemy1.extinction(deltatime):
                            monster_kill_count+=1
                            enemy_l=[ i for i in enemy_l if not i==enemy1]
                            if enemy1.name=="boss":
                                drop_obj_l.append(drop_obj.Meet(meet_im,enemy1.hitbox.centerx-32,enemy1.hitbox.centery,pygame.Rect(enemy1.x,enemy1.y,48,48)))
                                drop_obj_l.append(drop_obj.Magnetic(magnetic_im,enemy1.hitbox.centerx,enemy1.hitbox.centery,pygame.Rect(enemy1.x,enemy1.y,48,48)))
                                if 3==map_l[map_type%4].index(enemy1.type):
                                    gameover=True
                                    game="win"
                            else:
                                if probability(luck):
                                    for i in range(4):
                                        drop_obj_l.append(drop_obj.Exp(exp_im,enemy1.x-32,enemy1.y,pygame.Rect(enemy1.x,enemy1.y,25,25)))
                                else:
                                    for i in range(2):
                                        drop_obj_l.append(drop_obj.Exp(exp_im,enemy1.x-32,enemy1.y,pygame.Rect(enemy1.x,enemy1.y,25,25)))
                        for attack in attackeffect_l:
                            enemy1.exploded=True
                            if attack.hitbox.colliderect(enemy1.hitbox):
                                if enemy1.damage_tick >= enemy1.damage_tick_limit:
                                    enemy1.damage_tick = 0
                                    enemy1.health -= attack.damage * damage_multiplier
                                    damage_mount+=attack.damage * damage_multiplier
                                    # 확률 함수는 한 번만 호출
                                    if probability(execute) and enemy1.name != "boss":
                                        execute_count+=1
                                        draw_l.append(effect.Draw_dh(enemy1.hitbox.x + r_ps, enemy1.hitbox.top, 9999))
                                        enemy1.health -= 9999

                                    # 흡혈 효과
                                    if probability(vampirism_probability):
                                        if character1.health < character1.max_health-attack.damage * damage_multiplier * vampirism * 0.01:
                                            heal_mount+=attack.damage * damage_multiplier * vampirism * 0.01
                                            character1.health += attack.damage * damage_multiplier * vampirism * 0.01

                                    # 필요할 때만 랜덤 값을 생성
                                    r_ps = random.randint(-50, 50)
                                    draw_l.append(effect.Draw_dh(enemy1.hitbox.x + r_ps, enemy1.hitbox.top, int(attack.damage * damage_multiplier)))    
                        if enemy1.move_check  and enemy1.health>0:
                            enemy1.move(deltatime)
                        else:
                            enemy1.move_check = True
                    except Exception as e:
                        print(f"오류가 발생했습니다: {e}")
                        traceback.print_exc()
                pygame.display.flip()
        else:
            show_stat=False
            rect_surface.set_alpha(256)
            background.blit(rect_surface,(0,0))
            if not int(frame+deltatime*0.07)>=11:
                frame+=deltatime*0.07
                if game=="win":
                    clear_map.append(f'{map_type}')
                    background.blit(clear_frame[int(frame)],(bg_width-192-clear_frame[int(frame)].get_width()//2,160-clear_frame[int(frame)].get_height()//2))
                else:
                    background.blit(fail_frame[int(frame)],(bg_width-192-fail_frame[int(frame)].get_width()//2,160-fail_frame[int(frame)].get_height()//2))
            else:
                if game=="win":
                    background.blit(clear_frame[-1],(bg_width-192-clear_frame[-1].get_width()//2,160-clear_frame[-1].get_height()//2))
                else:
                    background.blit(fail_frame[-1],(bg_width-192-fail_frame[-1].get_width()//2,160-fail_frame[-1].get_height()//2))
                frame+=deltatime*0.07
                character1.drawing(background)
                if frame > 12:
                    text_draw(f"레벨 : {character1.level}", 256, 160, 28, 0, background, True, True)
                if frame > 18:
                    text_draw(f"넣은 대미지 : {damage_mount:.1f}", 256, 220, 28, 0, background, True, True)
                if frame > 24:
                    text_draw(f"처치한 적의 수 : {monster_kill_count}", 256, 280, 28, 0, background, True, True)
                if frame > 30:
                    text_draw(f"받은 대미지 : {damaged_mount:.1f}", 256, 340, 28, 0, background, True, True)
                if frame > 36:
                    text_draw(f"회복한 체력 : {heal_mount:.1f}", 256, 400, 28, 0, background, True, True)
                if frame > 42:
                    text_draw(f"이동 거리 : {move_len:.1f}", 256, 460, 28, 0, background, True, True)
                if frame > 48:
                    text_draw(f"처형한 적의 수 : {execute_count}", 256, 520, 28, 0, background, True, True)
                if frame > 72:
                    try:
                        text_draw(f"최종평가 : {tear[int(character1.level/10+damage_mount/1000+monster_kill_count/10+damaged_mount/100+heal_mount/100+execute_count/50)]}", 256, 580, 28, 0, background, True, True)
                    except:
                        if int(character1.level/10+damage_mount/1000+monster_kill_count/100+damaged_mount/100+heal_mount/100+execute_count/50)>20:
                            text_draw(f"최종평가 : S+", 256, 580, 28, 0, background, True, True)
                        else:
                            text_draw(f"최종평가 : F-", 256, 580, 28, 0, background, True, True)
                if frame>92:
                    text_draw(f"- space를 눌러 메뉴화면으로 이동 -", bg_width//2, 640, 28, 0, background, True, True,True)
            pygame.display.flip()
pygame.quit()