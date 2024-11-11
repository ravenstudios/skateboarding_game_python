import pygame
from constants import *
import main_entity


class Mob(main_entity.Main_entity):
    """docstring for Mob."""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.y_sprite_sheet_index = 0
        self.animation_speed = 10


    def update(self, cam_offset):

        self.update_cam_offset(cam_offset)
        print(f"mob.x:{self.rect.x}")
