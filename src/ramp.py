# push -> w key for giving the skateboard a small push using physics
# jump -> space for jump. Must have physics to use velocity
# duck -> down arrow to make player half size to go under objects
# Player must use the pygame.sprite.Sprite class. this dosnt have to be done first but must be refractored in.
# Must have draw and update functions.
# A camera system will be used to side scroll, we will add that later.
import pygame, random
from constants import *
import main_entity
import random


class Ramp(main_entity.Main_entity):
    def __init__(self, x, y, dir):
        super().__init__(x, y)
        self.dir = dir

        if dir == "right":
            self.y_sprite_sheet_index = 18
        else:
            self.y_sprite_sheet_index = 19
