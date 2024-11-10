import pygame
from constants import *
import main_entity


class Mob(main_entity.Main_entity):
    """docstring for Mob."""

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
