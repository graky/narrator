from PIL import Image
import random
import os
#area = (0, 0, 32, 40)


def cut_pieces(mapfile):
    img = Image.open(mapfile)
    x_step = 32
    y_step = 32
    x_count = 15
    y_count = 11
    for i in range(y_count):
        for j in range(x_count):
            area = (x_step*j, y_step*i, x_step*(j+1), y_step*(i+1))
            cropped_img = img.crop(area)
            cropped_img.save(f"{i, j}.png")

def generate_islands(map, island_number):
    max_size = 20
    for i in range(island_number):
        x_cord = random.randint(0, 399)
        y_cord = random.randint(0, 399)
        base_texture = random.choice(["desert", "grass", "snow", "earth", "stone_texture"])
        if x_cord+max_size*2 > 399:
            x_down = random.randint(0, 399-x_cord)
        else:
            x_down = random.randint(0, max_size*2)
        if x_cord-max_size*2 < 0:
            x_up = random.randint(0, x_cord)
        else:
            x_up = random.randint(0, max_size*2)
        for i in range(x_cord-x_up, x_cord+x_down):
            row = map[i]
            y_right = random.randint(0, int(max_size/2)) if y_cord+int(max_size/2)<399 else random.randint(0, 399-y_cord)
            y_left = random.randint(0, int(max_size/2)) if y_cord-int(max_size/2)>0 else random.randint(0, y_cord)
            for j in range(y_cord-y_left, y_cord+y_right):
                row[j]["base_texture"] = base_texture
    return map

def rand_cord_near_object(x_cord, y_cord, on_range, size):
    on_range_x = on_range
    on_range_x_minus = on_range
    on_range_y = on_range
    on_range_y_minus = on_range
    if x_cord + on_range > size:
        on_range_x = size - x_cord
    if y_cord + on_range > size:
        on_range_y = size - y_cord
    if x_cord-on_range < 0:
        on_range_x_minus = x_cord
    if y_cord-on_range < 0:
        on_range_y_minus = y_cord
    x_plus = random.choice([False, True])
    y_plus = random.choice([False, True])
    if x_plus:
        returned_x = x_cord + random.randint(0, on_range_x)
    else:
        returned_x = x_cord - random.randint(0, on_range_x_minus)
    if y_plus:
        returned_y = y_cord + random.randint(0, on_range_y)
    else:
        returned_y = y_cord - random.randint(0, on_range_y_minus)
    return  returned_x, returned_y


def generate_villagies(map, village_number):
    for i in range(village_number):
        x_cord = random.randint(0, 399)
        y_cord = random.randint(0, 399)
        map[x_cord][y_cord]["building"] = "farming_house"
        for i in range(0, random.randint(0, 5)):
            x_cord, y_cord = rand_cord_near_object(x_cord, y_cord, 5, 400)
            map[x_cord][y_cord]["building"] = "farming_house"
    return map



def generate_base_map():
    map = [[{} for i in range(400)] for i in range(400)]
    base_texture = random.choice(["desert", "grass", "snow", "earth", "stone_texture"])
    for row in map:
        for el in row:
            el["base_texture"] = base_texture
    map_with_islands = generate_islands(map, 20)
    map_with_villagies = generate_villagies(map_with_islands, 4)
    return map_with_villagies


def generate_picture():
    img = Image.new('RGB', (12800, 12800), color='white')
    map = generate_base_map()
    for i in range(0, 400, 2):
        row = map[i]
        for j in range(0, 400, 2):
            el = row[j]
            base_texture = el["base_texture"]
            folder = f"textures/{base_texture}"
            item = random.choice(os.listdir(folder))
            picture = Image.open(f"{folder}/{item}")
            img.paste(picture, (i*32, j*32))
            img.paste(picture, ((i+1)*32, j*32))
            img.paste(picture, (i*32, (j+1)*32))
            img.paste(picture, ((i+1)*32, (j+1)*32))
    for i in range(400):
        row = map[i]
        for j in range(400):
            el = row[j]
            if el.get("building") == "farming_house":
                houses = "textures/houses"
                item = random.choice(os.listdir(houses))
                house = Image.open(f"{houses}/{item}")
                house.resize((64, 64))
                img.paste(house, (i*32, j*32))

    img.save("full map with village.jpg")
    return map


map = generate_picture()

i = 0

for row in map:
    for el in row:
        if el.get("building" ) ==   "farming_house":
            i += 1

print(i)