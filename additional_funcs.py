import random
from additional_lists import *

def with_probability(percents):
    random_number = random.randint(1, 100)
    if random_number < percents:
        return True
    return False


def start_list():
    start_list = []
    start_list.append(random.choice(rus_D_list))
    start_list.append(random.choice(rus_G_list))
    start_list.append(random.choice(Z_list))
    return start_list

def generateD_G_Z():
    dgz_list = []
    dgz_list.append(random.choice(rus_D_list))
    dgz_list.append(random.choice(rus_G_list))
    dgz_list.append(random.choice(Z_list))
    return dgz_list

def generateABC():
    abc_list = []
    abc_list.append(random.choice(rus_D_list+a_list))
    abc_list.append(random.choice(rus_V_list))
    abc_list.append(random.choice(C))
    return abc_list

def generate_B_or_Z():
    rus_B_list.append(rus_Z)
    return random.choice(rus_B_list)

