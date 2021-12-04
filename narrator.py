import random
from characters import generate_characters
from additional_lists import *
from characters import generate_characters

character_list = generate_characters(100)


evil = random.choice(evils)

evil_to_object = random.choice(character_list+weapon_list+jewelry_list+world_elements+animal_species+flora)

def kill_steal_destroy(evil_to_object):
    if evil_to_object in character_list:
        kill_steal_destroy_result = ["kill", "steal"]
    elif evil_to_object in world_elements+animal_species+flora:
        kill_steal_destroy_result = ["steal"]
    else:
        kill_steal_destroy_result = ["destroy"]
    return random.choice(kill_steal_destroy_result)



start_list = [evil, kill_steal_destroy(evil_to_object), evil_to_object]
print(start_list)