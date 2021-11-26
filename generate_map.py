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
    max_size = 10
    for i in range(island_number):
        x_cord = random.randint(0, 199)
        y_cord = random.randint(0, 199)
        base_texture = random.choice(["desert", "grass", "snow", "earth", "stone_texture"])
        if x_cord+max_size > 199:
            x_down = random.randint(0, 199-x_cord)
        else:
            x_down = random.randint(0, max_size)
        if x_cord-max_size < 0:
            x_up = random.randint(0, x_cord)
        else:
            x_up = random.randint(0, max_size)
        for i in range(x_cord-x_up, x_cord+x_down):
            row = map[i]
            y_right = random.randint(0, max_size) if y_cord+max_size<199 else random.randint(0, 199-y_cord)
            y_left = random.randint(0, max_size) if y_cord-max_size>0 else random.randint(0, y_cord)
            for j in range(y_cord-y_left, y_cord+y_right):
                row[j]["base_texture"] = base_texture
    return map





def generate_map():
    map = [[{} for i in range(200)] for i in range(200)]
    base_texture = random.choice(["desert", "grass", "snow", "earth", "stone_texture"])
    for row in map:
        for el in row:
            el["base_texture"] = base_texture
    map_with_islands = generate_islands(map, 20)
    return map_with_islands

def generate_picture():
    img = Image.new('RGB', (6400, 6400), color='red')
    map = generate_map()
    for i in range(200):
        row = map[i]
        for j in range(200):
            el = row[j]
            base_texture = el["base_texture"]
            folder = f"textures/{base_texture}"
            item = random.choice(os.listdir(folder))
            picture = Image.open(f"{folder}/{item}")
            img.paste(picture, (i*32, j*32))

    img.save("full map generated3.jpg")



generate_picture()
#generate_map()
