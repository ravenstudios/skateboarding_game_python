
import pygame
from constants import *
import main_entity



class SkaterAvatar(main_entity.Main_entity):
    def __init__(self, x, y, player):
        super().__init__(x, y)
        self.player = player
        self.y_sprite_sheet_index = self.player.y_sprite_sheet_index - 1


    def update(self):
        self.y_sprite_sheet_index = self.player.y_sprite_sheet_index - 1
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y - 20


        self.animate()
