import pygame
import enemy
import weapon
import character
import spritesheet
import drop_obj
import random
import button
import boss
import math
import util as u
import effect
import traceback
import boss_pattern  
if True:
    pygame.init()

    background = pygame.display.set_mode((1280,810)) # 화면 생성
    pygame.display.set_caption("Mobmania")
    b_size=background.get_size()
    background.get_width
    play=1
    fps=pygame.time.Clock()
    clock = pygame.time.Clock()

    logo_im=pygame.image.load("assets/logo.png")
    logo_im=pygame.transform.scale(logo_im,(960,540))

    ui_l=[]
    for i in range(6):
        im=pygame.image.load(f"assets/ui/sprite_{i}.png").convert_alpha()
        ui_l.append(pygame.transform.scale(im,(64,64)))
    for i in range(6):
        im=pygame.image.load(f"assets/ui/sprites_{i}.png").convert_alpha()
        ui_l.append(pygame.transform.scale(im,(64,64)))
    im7 = pygame.image.load("assets/ui/sprite.png").convert_alpha()
    im7=pygame.transform.scale(im7,(288,64))

    pos_im=pygame.image.load("assets/pos.png").convert_alpha()

    exp_im=pygame.image.load("assets/drop_obj/exp.png").convert_alpha()
    magnetic_im=pygame.image.load("assets/drop_obj/magnetic.png").convert_alpha()
    meet_im=pygame.image.load("assets/drop_obj/meet.png").convert_alpha()
    show_stat1=pygame.image.load("assets/show_stat1.png").convert_alpha()
    show_stat2=pygame.image.load("assets/show_stat2.png").convert_alpha()

    weapon_0=pygame.image.load("assets/weapon/dagger.png").convert_alpha()
    weapon_1=pygame.image.load("assets/weapon/star.png").convert_alpha()
    weapon_2=pygame.image.load("assets/weapon/staff.png").convert_alpha()
    wave_frame=[]
    for i in range(1,236):
        if i<10:
            wave_im=pygame.image.load(f"assets/boss_wave_f/sprite_00{i}.png").convert_alpha()
        elif i<100:
            wave_im=pygame.image.load(f"assets/boss_wave_f/sprite_0{i}.png").convert_alpha()
        else:
            wave_im=pygame.image.load(f"assets/boss_wave_f/sprite_{i}.png").convert_alpha()
        wave_frame.append(wave_im)

    sword_im=pygame.image.load("assets/weapon/sword.png").convert_alpha()
    sword_sheet = spritesheet.SpriteSheet(sword_im)
    sword_frame=[]
    for i in range(2):
        for j in range(8):
            sword_frame.append(sword_sheet.get_image(j,i,64,64, 1,(0,0,0)))

    
    cooltime_frame=[]
    for i in range(17):
        im=pygame.image.load(f"assets/cooltime/cooltime{i}.png").convert_alpha()
        im.set_alpha(200)
        cooltime_frame.append(im)
    missile_im=pygame.image.load("assets/weapon/missile.png").convert_alpha()
    missile_sheet = spritesheet.SpriteSheet(missile_im)
    missile_frame=[]
    for i in range(2):
        for j in range(8):
            im=missile_sheet.get_image(j,i,64,64, 3,(0,0,0))
            missile_frame.append(im.convert_alpha())

    mine_im=pygame.image.load("assets/weapon/mine.png").convert_alpha()
    mine_sheet = spritesheet.SpriteSheet(mine_im)
    mine_frame=[]
    for i in range(2):
        for j in range(8):
            im=mine_sheet.get_image(j,i,64,64, 3,(0,0,0))
            mine_frame.append(im.convert_alpha())

    attackeffect_l=[]

    map_type=0
    screen_image = pygame.image.load(f'assets/ground{map_type+1}.png').convert_alpha().convert_alpha() # 배경설정
    screen_image = pygame.transform.scale(screen_image, (1280,810))

    bg_width, bg_height = screen_image.get_size()
    scroll_x = 0
    scroll_y = 0
    level_limit=30
    screen_rect=pygame.Rect(0,0,bg_width,bg_height)

    rect2 = pygame.Surface((1280, 80), pygame.SRCALPHA)
    rect2.fill((0, 0, 0, 128))

    rect4=pygame.Surface((80, 24), pygame.SRCALPHA)
    rect4.fill((0, 0, 0, 128))
    rect4.set_alpha(220)
    boss_attack=[]
    drop_obj_l=[]
    exp_mount=0
    select_skill=True
    center_x,center_y = bg_width // 2 ,  bg_height // 2

    image1 = pygame.image.load("assets/buttons/button0_0.png").convert_alpha()
    image2 = pygame.image.load("assets/buttons/button1_0.png").convert_alpha()
    image3 = pygame.image.load("assets/buttons/button3.png").convert_alpha()
    image3=pygame.transform.scale(image3,(537.6,806.4))
    image4 = pygame.image.load("assets/buttons/button2.png").convert_alpha()
    image5 = pygame.image.load("assets/buttons/button0_1.png").convert_alpha()
    image6 = pygame.image.load("assets/buttons/button1_1.png").convert_alpha()

    levelup_l=[pygame.image.load(f"assets/LEVEL_UP/sprite_{i}.png").convert_alpha() for i in range(4)]
    level_animation=0

    buttons=[]

    rect_surface = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
    rect_surface.fill((0,0,0,128))
    rect_surface.set_alpha(164)

    menu_button=[]
    menu_button_rect=[]
    for i in range(4):
        menu_button.append(pygame.image.load(f"assets/menu_button/button{i}.png").convert_alpha())
    menu_button_rect.append(pygame.rect.Rect(center_x-512,center_y,232,192))
    menu_button_rect.append(pygame.rect.Rect(center_x-256,center_y,232,192))
    menu_button_rect.append(pygame.rect.Rect(center_x+24,center_y,232,192))
    menu_button_rect.append(pygame.rect.Rect(center_x+280,center_y,232,192))

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
    available_weapons = ["Dagger", "Staff", "Star", "Missile", "Mine", "Sword"]
    available_buff=["Damage","defense","magnet","vampirism","execute","luck"] # 선택 가능한 무기 리스트
    korean_weapon_name=["암살용 단검","불의 지팡이","유성우","대공미사일","대형지뢰","카타나","대미지 증가","방어력 증가","자력범위증가","흡혈","처형","행운"]
    skill_data_l=[]
    show=True
    skill_data_l.append(weapon.Dagger_Data(character1,[bg_width,bg_height],"Dagger"))
    skill_data_l.append(weapon.Staff_Data(character1,[bg_width,bg_height],"Staff"))
    skill_data_l.append(weapon.Star_Data(character1,[bg_width,bg_height],"Star"))
    skill_data_l.append(weapon.Missile_Data(character1,[bg_width,bg_height],"Missile"))
    skill_data_l.append(weapon.Mine_Data(character1,[bg_width,bg_height],"Mine"))
    skill_data_l.append(weapon.Sword_Data(character1,[bg_width,bg_height],"Sword"))
    map_l=[['mushroom', 'goblin', 'slime', 'pumkin'],
           ['ghost', 'skeleton', 'pumkin', 'zombie'],
           ['turtle', 'shellfish', 'slime','jellyfish'],
           ['cactus', 'desert_goblin', 'skeleton', 'pharaoh']]
    map_l=[['pumkin','mushroom', 'goblin', 'slime' ],
           ['ghost', 'skeleton', 'pumkin', 'zombie'],
           ['turtle', 'shellfish', 'slime','jellyfish'],
           ['cactus', 'desert_goblin', 'skeleton', 'pharaoh']]

    for i in range(6):
        skill_data_l.append(weapon.Buff_data(available_buff[i]))
    show_stat=False
    frame_counter = 0
    damage_multiplier=1
    defense_multiplier=1
    magnet_multiplier=1
    vampirism_probability=0
    vampirism=0
    execute=0
    luck=0
    order=[]
    order1=[]
    rect1=[]
    rect1.append(pygame.Rect(center_x-image3.get_size()[0]//2,
                            center_y-image3.get_size()[1]//2,
                            image3.get_size()[0],
                            image3.get_size()[1]))
    
    first_iteration = True
    menu=False
    while play:

        clock.tick(60)
        m_x, m_y = pygame.mouse.get_pos()
        deltatime = fps.tick(60)
        key_pressed=pygame.key.get_pressed()
        background.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play=False
        if menu:
            for x in range(-bg_width, bg_width + bg_width, bg_width):
                for y in range(-bg_height, bg_height + bg_height, bg_height):
                    background.blit(screen_image, (x + scroll_x, y + scroll_y))
            background.blit(rect_surface,(0,0))
            background.blit(logo_im,(center_x-logo_im.get_width()//2,center_y-450))
            background.blit(menu_button[0],(center_x-512,center_y))
            background.blit(menu_button[1],(center_x-256,center_y))
            background.blit(menu_button[2],(center_x+24,center_y))
            background.blit(menu_button[3],(center_x+280,center_y))
            scroll_x+=0.03*deltatime
            scroll_y+=0.03*deltatime
            scroll_x %= bg_width
            scroll_y %= bg_height
            pygame.display.flip()
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if rect3_hitbox.collidepoint((m_x,m_y)):
                        if show_stat:
                            show_stat=False
                        else:
                            show_stat=True

            for x in range(-bg_width, bg_width + bg_width, bg_width):
                for y in range(-bg_height, bg_height + bg_height, bg_height):
                    background.blit(screen_image, (x + scroll_x, y + scroll_y))
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
            for dh in draw_l:
                dh.drawing(background)
                if dh.move(deltatime):
                    draw_l=[i for i in draw_l if not i==dh]

            background.blit(rect2,(0,bg_height-138))            
            background.blit(pos_im,(0,bg_height-138))
            character1.drawing(background)
            character1.draw_health(background)

            background.blit(rect4,(bg_width//2-40,0))
            u.text_draw(f"{int(time//60)} : {int(time)%60}",bg_width//2,10,24,0,background,True,True,True)
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
                                u.text_draw(f"{(weapon_data.get_cooltime_limit()-weapon_data.cooltime):.1f}",148+order.index(weapon_data.name)*73,bg_height-108,28,0,background,True,True)
                    except ValueError:
                        if weapon_data.name in available_buff:
                            order1.append(weapon_data.name)
                        else:
                            order.append(weapon_data.name)
                    except IndexError:
                        pass
            if show_stat:
                rect3 = pygame.Surface((186, 465), pygame.SRCALPHA)
                rect3.fill((0, 0, 0, 128))
                rect3.set_alpha(220)
                background.blit(rect3,(0,130))
                u.text_draw(f"상태창  lv.{character1.level}", 25, 140, 28, 0, background, True, True)
                u.text_draw(f"체력: {character1.max_health}.0/{character1.health:.1f}", 30, 188, 18, 0, background, True, True)
                u.text_draw(f"공격력 : {damage_multiplier:.1f}", 30, 236, 18, 0, background, True, True)
                u.text_draw(f"방어력 : {defense_multiplier:.1f}", 30, 284, 18, 0, background, True, True)
                u.text_draw(f"자력범위 : {magnet_multiplier:.1f}", 30, 332, 18, 0, background, True, True)
                u.text_draw(f"흡혈확률 : {vampirism_probability:.1f}%", 30, 380, 18, 0, background, True, True)
                u.text_draw(f"흡혈량 : {vampirism:.1f}%", 30, 428, 18, 0, background, True, True)
                u.text_draw(f"처형확률 : {execute:.1f}%", 30, 476, 18, 0, background, True, True)
                u.text_draw(f"행운 : {luck:.1f}%", 30, 524, 18, 0, background, True, True)
                u.text_draw(f"죽인 적의 수 : {monster_kill_count}", 30, 572, 18, 0, background, True, True)
                background.blit(show_stat1,(0,0))
            else:
                background.blit(show_stat2,(0,0)) 
                rect3_hitbox=pygame.rect.Rect(0,0,186,392)


            try:
                ratio = wave_time / 45
                index_value = int(ratio * 243)
                background.blit(wave_frame[index_value],(center_x-wave_frame[0].get_size()[0]//2,bg_height-115))
                if len(enemy_l)<enemy_mount:
                    enemy_type = random.choice(map_l[map_type])
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
                enemy_type = map_l[map_type][(boss_wave-1)%4]
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
                enemy_mount+=3
                wave_time=0
                wave=0


            ratio = exp_mount / level_limit
            pygame.draw.rect(background, (0,0,0), (0, bg_height-20,bg_width,20))
            pygame.draw.rect(background,(0,230, 255), (0, bg_height-20,bg_width * ratio,20))

            # 레벨업 및 스킬 선택

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
                            u.text_draw(u.get_text(button1.button_type[0], button1.button_type[1]), 
                                        button1.rect.centerx - 110, button1.rect.centery + 8, 18, 0, background)
                            u.text_draw((korean_weapon_name[available_weapons.index(button1.button_type[0])] + 
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
                scroll_x %= bg_width
                scroll_y %= bg_height
                if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_UP] or key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_d] or key_pressed[pygame.K_a] or key_pressed[pygame.K_w]or key_pressed[pygame.K_s]:
                    character1.change_frame(True, deltatime)
                else:
                    character1.change_frame(False, deltatime)
                scroll_x,scroll_y=character1.screen_move_check(key_pressed,deltatime,scroll_x,scroll_y)
                # 무기 쿨타임 관리 및 생성
                for attack in boss_attack:
                    attack.screen_move_check(key_pressed,character1.speed,deltatime)
                    attack.update()
                    attack.move(deltatime)
                    print(len(boss_attack))
                    if attack.change_frame(deltatime) or (not screen_rect.colliderect(attack.hitbox) and attack.y>attack.target_y):
                        boss_attack=[i for i in boss_attack if not i==attack]
                    print(len(boss_attack))

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
                    attack.change_frame(deltatime,enemy_l)
                    attack.update()
                    attack.screen_move_check(key_pressed,deltatime,character1.speed)

                    if attack.extinction_condition(screen_rect,character1.hitbox):
                        attackeffect_l=[ i for i in attackeffect_l if not i==attack]

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
                                        if enemy1.type=="pumkin":
                                            boss_attack.append(boss_pattern.pumkin_pattern1())
                                        elif enemy1.type=="zombie":
                                            boss_attack.append(boss_pattern.zombie_pattern1())
                                        elif enemy1.type=="pharaoh":
                                            boss_attack.append(boss_pattern.pharaoh_pattern1())
                                        elif enemy1.type=="jellyfish":
                                            boss_attack.append(boss_pattern.jellyfish_pattern1())
                                else:
                                    for i in range(random.randint(2,4)):
                                        if enemy1.type=="pumkin":
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
                            enemy1.move_check = False
                            collision_vector = pygame.Vector2(enemy1.hitbox.left - character1.hitbox.left, enemy1.hitbox.top - character1.hitbox.top).normalize()
                            enemy1.x += collision_vector.x * enemy1.speed * deltatime*20 *character1.speed
                            enemy1.y += collision_vector.y * enemy1.speed * deltatime*20 *character1.speed
                        enemy1.damage_tick+=deltatime*0.05
                        if enemy1.extinction(deltatime):
                            monster_kill_count+=1
                            if enemy1.name=="boss":
                                drop_obj_l.append(drop_obj.Meet(meet_im,enemy1.hitbox.centerx-32,enemy1.hitbox.centery,pygame.Rect(enemy1.x,enemy1.y,48,48)))
                                drop_obj_l.append(drop_obj.Magnetic(magnetic_im,enemy1.hitbox.centerx,enemy1.hitbox.centery,pygame.Rect(enemy1.x,enemy1.y,48,48)))
                            else:
                                if u.probability(luck):
                                    for i in range(4):
                                        drop_obj_l.append(drop_obj.Exp(exp_im,enemy1.x-32,enemy1.y,pygame.Rect(enemy1.x,enemy1.y,25,25)))
                                else:
                                    for i in range(2):
                                        drop_obj_l.append(drop_obj.Exp(exp_im,enemy1.x-32,enemy1.y,pygame.Rect(enemy1.x,enemy1.y,25,25)))
                            enemy_l=[ i for i in enemy_l if not i==enemy1]
                        for attack in attackeffect_l:
                            enemy1.exploded=True
                            # 충돌 체크를 매 프레임마다 수행 (간격 없이)
                            if attack.hitbox.colliderect(enemy1.hitbox):
                                if enemy1.damage_tick >= enemy1.damage_tick_limit:
                                    enemy1.damage_tick = 0
                                    enemy1.health -= attack.damage * damage_multiplier

                                    # 확률 함수는 한 번만 호출
                                    if u.probability(execute) and enemy1.name != "boss":
                                        draw_l.append(effect.Draw_dh(enemy1.hitbox.x + r_ps, enemy1.hitbox.top, 9999))
                                        enemy1.health -= 9999

                                    # 흡혈 효과
                                    if u.probability(vampirism_probability):
                                        if character1.health < character1.max_health-attack.damage * damage_multiplier * vampirism * 0.01:
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
    pygame.quit()