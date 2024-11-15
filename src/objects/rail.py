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


class Rail(main_entity.Main_entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.y_sprite_sheet_index = 17
        self.frame = 0
        self.animation_speed = 0
