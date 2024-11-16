import pygame, random
from constants import *
import main_entity
import random


class Block(main_entity.Main_entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.rect.width = w
        self.rect.height = h
        self.y_sprite_sheet_index = 16
        self.frame = random.randint(0, 3)
        self.animation_speed = 0

        # print(self.rect)

    def update(self, cam_offset):
        self.update_cam_offset(cam_offset)
        self.create_tiled_surface()
