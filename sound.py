from util import *
sound_dict = {}


sound_dict['mushroom'] = get_sound('assets/enemy_sound/plant.MP3')
sound_dict['pumkin'] = get_sound('assets/enemy_sound/plant.MP3')
sound_dict['cactus'] = get_sound('assets/enemy_sound/plant.MP3')
sound_dict['ghost'] = get_sound('assets/enemy_sound/ghost.MP3')
sound_dict['goblin'] = get_sound('assets/enemy_sound/goblin.MP3')
sound_dict['pharaoh'] = get_sound('assets/enemy_sound/pharaoh.MP3')
sound_dict['slime'] = get_sound('assets/enemy_sound/bubble.MP3')
sound_dict['shellfish'] = get_sound('assets/enemy_sound/bubble.MP3')
sound_dict['skeleton'] = get_sound('assets/enemy_sound/skeleton.MP3')
sound_dict['jellyfish'] = get_sound('assets/enemy_sound/squid.MP3')
sound_dict['turtle'] = get_sound('assets/enemy_sound/turtle.MP3')
sound_dict['zombie'] = get_sound('assets/enemy_sound/zombie.MP3')

sound_dict['music'] = [get_sound(f"assets/music/music{i}.MP3") for i in range(1, 5)]


sound_dict['explosion_sound'] = get_sound('assets/weapon_sound/explosion.MP3')
sound_dict['dagger_sound'] = get_sound('assets/weapon_sound/dagger.MP3')
sound_dict['fireball_sound'] = get_sound('assets/weapon_sound/fireball.MP3')
sound_dict['sword_sound'] = get_sound('assets/weapon_sound/sword.MP3')
sound_dict['star_sound'] = get_sound('assets/weapon_sound/star.MP3')

sound_dict['victory_sound'] = get_sound('assets/sound/victory.MP3')
sound_dict['levelup_sound'] = get_sound('assets/sound/levelup.MP3')
sound_dict['gameover_sound'] = get_sound('assets/sound/gameover.MP3')
sound_dict['button_sound'] = get_sound('assets/sound/button.MP3')
sound_dict['walk_sound'] = get_sound('assets/sound/walk.MP3')
sound_dict['stamp_sound'] = get_sound('assets/sound/stamp.MP3')