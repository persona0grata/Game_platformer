import pygame as pg 
import os

from  Sprite import Sprite


class Platform(Sprite):
    def __init__(self, image_path, img, startx, starty):
        super().__init__(os.path.join(image_path, img), startx, starty)
