import pygame
import os
import sys

BASE_IMG_PATH = 'data/images'


def load_image(name, colorkey=None):
    fullname = os.path.join(BASE_IMG_PATH, name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


def load_images(name):
    fullpath = os.path.join(BASE_IMG_PATH, name)
    return [load_image(os.path.join(name, i)) for i in os.listdir(fullpath)]
