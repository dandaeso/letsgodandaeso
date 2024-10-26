from boss import *
from enemy import *
from character import *
from weapon import *
class Object_Controler:
    def __init__(self,center_x,center_y):
        self.ui_l=[]
        for i in range(6):
            im=pygame.image.load(f"assets/ui/sprite_{i}.png").convert_alpha()
            self.ui_l.append(pygame.transform.scale(im,(64,64)))
        for i in range(6):
            im=pygame.image.load(f"assets/ui/sprites_{i}.png").convert_alpha()
            self.ui_l.append(pygame.transform.scale(im,(64,64)))
        self.drop_obj_l=[]
        self.enemy_l=[]
        self.drop_obj=[]
        self.attackeffect_l=[]
        self.draw_l=[]
        self.skill_data_l=[]
        character1=Character(0.09,center_x,center_y)

        self.screen_image =[ pygame.image.load(f'assets/ground{i}.png').convert_alpha() for i in range(4)]
        self.screen_image =[pygame.transform.scale(self.screen_image[i], (1280,810)) for i in self.screen_image]
        self.bg_width, self.bg_height = self.screen_image[0].get_size()
        self.scroll_x = 0
        self.scroll_y = 0
        self.screen_rect=pygame.Rect(0,0,self.bg_width,self.bg_height)
        
        self.available_weapons = ["Dagger", "Staff", "Star", "Missile", "Mine", "Sword"]
        self.available_buff=["Damage","defense","magnet","vampirism","execute","luck"] # 선택 가능한 무기 리스트
        self.korean_weapon_name=["암살용 단검","불의 지팡이","유성우","대공미사일","대형지뢰","카타나","대미지 증가","방어력 증가","자력범위증가","흡혈","처형","행운"]

        self.skill_data_l.append(Dagger_Data(character1,[self.bg_width,self.bg_height],"Dagger"))
        self.skill_data_l.append(Staff_Data(character1,[self.bg_width,self.bg_height],"Staff"))
        self.skill_data_l.append(Star_Data(character1,[self.bg_width,self.bg_height],"Star"))
        self.skill_data_l.append(Missile_Data(character1,[self.bg_width,self.bg_height],"Missile"))
        self.skill_data_l.append(Mine_Data(character1,[self.bg_width,self.bg_height],"Mine"))
        self.skill_data_l.append(Sword_Data(character1,[self.bg_width,self.bg_height],"Sword"))
        for i in range(6):
            self.skill_data_l.append(Buff_data(self.available_buff[i]))
            for i in range(6):
                im=pygame.image.load(f"assets/ui/sprite_{i}.png").convert_alpha()
                self.ui_l.append(pygame.transform.scale(im,(64,64)))
            for i in range(6):
                im=pygame.image.load(f"assets/ui/sprites_{i}.png").convert_alpha()
                self.ui_l.append(pygame.transform.scale(im,(64,64)))

        self.desert_enemies = ['cactus', 'desert_goblin', 'skeleton', 'pharaoh']
        self.sea_enemies = ['skeleton', 'shellfish', 'slime','jellyfish']
        self.meadow_enemies = ['mushroom', 'goblin', 'slime', 'pumkin']
        self.graveyard_enemies = ['ghost', 'skeleton', 'pumkin', 'zombie']

        self.order=[]
        self.order1=[]

        self.frame_counter = 0
        self.damage_multiplier=1
        self.defense_multiplier=1
        self.magnet_multiplier=1
        self.vampirism_probability=0
        self.vampirism=0
        self.execute=0
        self.luck=0

        self.enemy_mount=12
        self.monster_kill_count=0
        self.enemy_mount=7
        self.wave=0
        self.boss_wave=1

        self.exp_im=pygame.image.load("assets/drop_obj/exp.png").convert_alpha()
        self.magnetic_im=pygame.image.load("assets/drop_obj/magnetic.png").convert_alpha()
        self.meet_im=pygame.image.load("assets/drop_obj/meet.png").convert_alpha()

        self.level_limit=30
        self.exp_mount=0
    def drawing(self,background):
        background.fill((255,255,255))

        for x in range(-self.bg_width, self.bg_width + self.bg_width, self.bg_width):
            for y in range(-self.bg_height, self.bg_height + self.bg_height, self.bg_height):
                background.blit(self.screen_image, (x + self.scroll_x, y + self.scroll_y))
                
        for obj in self.drop_obj_l:
            if obj:
                obj.updat()
                obj.drawing(background)

        for attack in self.attackeffect_l:
            if attack:
                attack.drawing(background)

        for enemy1 in self.enemy_l:
            if enemy1:
                enemy1.select_speed(background.get_size()[0],background.get_size()[1])
                enemy1.drawing()
                enemy1.updat()
                enemy1.flip_im()

        for dh in self.draw_l:
            if dh:
                dh.drawing(background)
                # if dh.move(deltatime):
                #     self.draw_l=[i for i in self.draw_l if not i==dh]

        for weapon_data in self.skill_data_l:

            if weapon_data.level!=0:
                try:
                    if weapon_data.name == "Dagger":
                        background.blit(self.ui_l[0],(self.order.index(weapon_data.name)*64,0))
                    elif weapon_data.name == "Staff":
                        background.blit(self.ui_l[1],(self.order.index(weapon_data.name)*64,0))   
                    elif weapon_data.name == "Star":
                        background.blit(self.ui_l[2],(self.order.index(weapon_data.name)*64,0))
                    elif weapon_data.name == "Missile":
                        background.blit(self.ui_l[3],(self.order.index(weapon_data.name)*64,0))    
                    elif weapon_data.name == "Mine":
                        background.blit(self.ui_l[4],(self.order.index(weapon_data.name)*64,0))
                    elif weapon_data.name == "Sword":
                        background.blit(self.ui_l[5],(self.order.index(weapon_data.name)*64,0))

                    elif weapon_data.name=="Damage":
                        background.blit(self.ui_l[6],(self.order1.index(weapon_data.name)*64,64))
                    elif weapon_data.name=="defense":
                        background.blit(self.ui_l[7],(self.order1.index(weapon_data.name)*64,64))
                    elif weapon_data.name=="magnet":
                        background.blit(self.ui_l[8],(self.order1.index(weapon_data.name)*64,64))
                    elif weapon_data.name=="vampirism":
                        background.blit(self.ui_l[9],(self.order1.index(weapon_data.name)*64,64))
                    elif weapon_data.name=="execute":
                        background.blit(self.ui_l[10],(self.order1.index(weapon_data.name)*64,64))
                    elif weapon_data.name=="luck":
                        background.blit(self.ui_l[11],(self.order1.index(weapon_data.name)*64,64))
                except ValueError:
                    if weapon_data.name in self.available_buff:
                        self.order1.append(weapon_data.name)
                    else:
                        self.order.append(weapon_data.name)

        try:
            background.blit(self.wave_frame[int(self.wave)],(self.center_x-self.wave_frame[0].get_size()[0]//2,self.bg_height-115))
        except IndexError:
            background.blit(self.wave_frame[0],(self.center_x-self.wave_frame[0].get_size()[0]//2,self.bg_height-115))
            self.boss_wave+=1
            self.enemy_mount+=3
            self.wave=0

        self.character1.drawing(background)
        self.character1.draw_health(background)

        ratio = self.exp_mount / self.level_limit
        pygame.draw.rect(background, (0,0,0), (0, self.bg_height-20,self.bg_width,20))
        pygame.draw.rect(background,(0,230, 255), (0, self.bg_height-20,self.bg_width * ratio,20))
    def update(self,deltatime):
        first_iteration = True
        self.wave += 0.01 * deltatime
        self.scroll_x %= self.bg_width
        self.scroll_y %= self.bg_height
    def weapon_data_control(self,deltatime,m_x,m_y):
        for weapon_data in self.skill_data_l:
            if weapon_data.name in self.available_buff:
                if weapon_data.name=="Damage":
                    self.damage_multiplier=weapon_data.get_data()
                elif weapon_data.name=="defense":
                    self.defense_multiplier=weapon_data.get_data()
                elif weapon_data.name=="magnet":
                    self.magnet_multiplier=weapon_data.get_data()
                elif weapon_data.name=="vampirism":
                    self.vampirism,vampirism_probability=weapon_data.get_data()
                elif weapon_data.name=="execute":
                    self.execute=weapon_data.get_data()
                elif weapon_data.name=="luck":
                    self.luck=weapon_data.get_data()
            else:
                weapon_data.cooltime += 0.1*deltatime
                if weapon_data.cooltime >= weapon_data.get_cooltime_limit() and weapon_data.level!=0:
                    weapon_data.cooltime = 0
                    if weapon_data.name == "Dagger":
                        random_angle = random.randint(0, 179)
                        for i in range(weapon_data.get_repeat()):
                            data = weapon_data.get_data(random_angle,weapon_data.get_repeat(),i, m_x, m_y)
                            self.attackeffect_l.append(Dagger(*data))
                    
                    
                    elif weapon_data.name == "Staff":
                        for i in range(-1,weapon_data.get_repeat()-1):
                            data = weapon_data.get_data(0,weapon_data.get_repeat(), m_x, m_y)
                            self.attackeffect_l.append(Staff(*data))
                    
                    
                    
                    elif weapon_data.name == "Star":
                        # Star 생성 코드
                        base_angle = random.uniform(0, 2 * math.pi)
                        for i in range(weapon_data.get_repeat()):
                            data = weapon_data.get_data(base_angle,weapon_data.get_repeat(),i, m_x, m_y)
                            self.attackeffect_l.append(Star(*data))
                
                
                    elif weapon_data.name == "Missile":
                        # Missile 생성 코드
                        for i in range(weapon_data.get_repeat()):
                            data = weapon_data.get_data(0,weapon_data.get_repeat(), m_x, m_y)
                            self.attackeffect_l.append(Missile(*data))
                    
                    
                    elif weapon_data.name == "Mine":
                        for i in range(weapon_data.get_repeat()):
                            data = weapon_data.get_data(0,weapon_data.get_repeat(), m_x, m_y)
                            self.attackeffect_l.append(Mine(*data))
                            
                    
                    elif weapon_data.name == "Sword":
                        data = weapon_data.get_data(weapon_data.get_repeat(), m_x, m_y)
                        self.attackeffect_l.append(Sword(*data))

    def character_control(self,deltatime,key_pressed):
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_UP] or key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_d] or key_pressed[pygame.K_a] or key_pressed[pygame.K_w]or key_pressed[pygame.K_s]:
            self.character1.change_frame(True, deltatime)
        else:
            self.character1.change_frame(False, deltatime)
            self.scroll_x,self.scroll_y=self.character1.screen_move_check(key_pressed,deltatime,self.scroll_x,self.scroll_y)

    def attack_effect_control(self,deltatime,key_pressed):
        for attack in self.attackeffect_l:
            if attack:             
                try:
                    attack.move(deltatime,self.character1.hitbox.left,self.character1.hitbox.top)
                except:
                    pass
                attack.change_frame(deltatime,self.enemy_l)
                attack.update()
                attack.screen_move_check(key_pressed,deltatime,self.character1.speed)
    def attack_effect_extinction(self):
        for attack in self.attackeffect_l:
            if attack.extinction_condition(self.screen_rect,self.character1.hitbox):
                attackeffect_l=[ i for i in attackeffect_l if not i==attack]

    def drop_obj_control(self,key_pressed,deltatime):
        for obj in self.drop_obj_l:
            if obj:
                distance_obj = ((self.character1.hitbox.centerx - obj.hitbox.centerx)**2 + (self.character1.hitbox.centery - obj.hitbox.centery)**2)**0.5
                if distance_obj<=100*self.magnet_multiplier:
                    obj.situ=True
                if obj.situ:
                    try:
                        obj.magnetic(deltatime,self.character1.hitbox.centerx,self.character1.hitbox.centery)
                    except:
                        pass
                obj.screen_move_check(key_pressed,deltatime,self.character1.speed)

    def drop_obj_extinction(self):
        for obj in self.drop_obj_l:
            if obj.hitbox.colliderect(self.character1.hitbox):
                if obj.type=="exp":
                    exp_mount+=5
                if obj.type=="meet":
                    self.character1.health=60
                if obj.type=="magnetic":
                    for obj in self.drop_obj_l:
                        if obj:
                            obj.situ=True
                        self.drop_obj_l=[i for i in self.drop_obj_l if not i==obj]

    def enemy_extinction(self,deltatime):
        for enemy1 in self.enemy_l:
            if enemy1:
                if enemy1.extinction(deltatime):
                    monster_kill_count+=1
                    if enemy1.name=="boss":
                        self.drop_obj_l.append(self.drop_obj.Meet(self.meet_im,enemy1.hitbox.centerx-32,enemy1.hitbox.centery,pygame.Rect(enemy1.x,enemy1.y,48,48)))
                        self.drop_obj_l.append(self.drop_obj.Magnetic(self.magnetic_im,enemy1.hitbox.centerx,enemy1.hitbox.centery,pygame.Rect(enemy1.x,enemy1.y,48,48)))
                    else:
                        if u.probability(self.luck):
                            for i in range(4):
                                self.drop_obj_l.append(self.drop_obj.Exp(self.exp_im,enemy1.x-32,enemy1.y,pygame.Rect(enemy1.x,enemy1.y,25,25)))
                        else:
                            for i in range(2):
                                self.drop_obj_l.append(self.drop_obj.Exp(self.exp_im,enemy1.x-32,enemy1.y,pygame.Rect(enemy1.x,enemy1.y,25,25)))
                    self.enemy_l=[ i for i in self.enemy_l if not i==enemy1]

    def enemy_cotrol(self,key_pressed,background,speed,deltatime):
        for enemy1 in self.enemy_l:
            if enemy1:
                try:
                    enemy1.screen_move_check(key_pressed,speed,deltatime)
                    for enemy2 in self.enemy_l:
                        if enemy2:
                            if enemy1.hitbox != enemy2.hitbox:
                                if enemy2.hitbox.colliderect(enemy1.hitbox):
                                    distance_enemy1 = ((background.get_width()//2 - enemy1.hitbox.centerx)**2 + (background.get_height()//2 - enemy1.hitbox.centery)**2)**0.5
                                    distance_enemy2 = ((background.get_width()//2 - enemy2.hitbox.centerx)**2 + (background.get_height()//2 - enemy2.hitbox.centery)**2)**0.5
                                    if move_check and distance_enemy1 < distance_enemy2:
                                        move_check = True
                                    else:
                                        move_check = False
                                    collision_vector = pygame.Vector2(enemy1.x - enemy2.x, enemy1.y - enemy2.y).normalize()
                                    enemy1.x += collision_vector.x * enemy1.speed * deltatime*2
                                    enemy1.y += collision_vector.y * enemy1.speed * deltatime*2
                                    #벡터 nomalize해서 즉석으로 밀어내기
                        move_check = False
                    enemy1.damage_tick+=deltatime*0.05
                except:
                    pass
    def summon_enemy(self, enemy_type):
        if len(self.enemy_l)<self.enemy_mount:
            if enemy_type == "zombie":
                self.enemy_l.append(Zombie())
            elif enemy_type == "skeleton":
                self.enemy_l.append(Skeleton())
            elif enemy_type == "pharaoh":
                self.enemy_l.append(Pharaoh())
            elif enemy_type == "turtle":
                self.enemy_l.append(Turtle())
            elif enemy_type == "goblin":
                self.enemy_l.append(Goblin())
            elif enemy_type == "desert_goblin":
                self.enemy_l.append(Desert_Goblin())
            elif enemy_type == "mushroom":
                self.enemy_l.append(Mushroom())
            elif enemy_type == "pumkin":
                self.enemy_l.append(Pumkin())
            elif enemy_type == "slime":
                self.enemy_l.append(Slime())
            elif enemy_type == "ghost":
                self.enemy_l.append(Ghost())
            elif enemy_type == "jellyfish":
                self.enemy_l.append(Jellyfish())
            elif enemy_type == "shellfish":
                self.enemy_l.append(Shellfish())
            elif enemy_type == "cactus":
                self.enemy_l.append(Cactus())
            
    def summon_boss(self, boss_type):
        if boss_type == "zombie":
            self.enemy_l.append(Zombie_Boss())
        elif boss_type == "skeleton":
            self.enemy_l.append(Skeleton_Boss())
        elif boss_type == "goblin":
            self.enemy_l.append(Goblin_Boss())
        elif boss_type == "mushroom":
            self.enemy_l.append(Mushroom_Boss())
        elif boss_type == "pumkin":
            self.enemy_l.append(Pumkin_Boss())
        elif boss_type == "slime":
            self.enemy_l.append(Slime_Boss())
        elif boss_type == "ghost":
            self.enemy_l.append(Ghost_Boss())
        elif boss_type == "pharaoh":
            self.enemy_l.append(Pharaoh_Boss())
        elif boss_type == "turtle":
            self.enemy_l.append(Turtle_Boss())
        elif boss_type == "desert_goblin":
            self.enemy_l.append(Desert_Goblin_Boss())
        elif boss_type == "jellyfish":
            self.enemy_l.append(Jellyfish_Boss())
        elif boss_type == "shellfish":
            self.enemy_l.append(Shellfish_Boss())

