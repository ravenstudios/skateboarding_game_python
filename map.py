import csv
import pygame
import block
import rail
import ramp
from constants import *

class Map(object):
    def __init__(self):
        self.blocks = pygame.sprite.Group()
        self.player_location = (0, 0)

    def load(self, map_file):
        with open(map_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        for r, row in enumerate(rows):
            for c, tile in enumerate(row):
                # print(f"R:{r}  C:{c}  Tile:{tile}")
                if tile == "68":
                    self.blocks.add(rail.Rail(c * BLOCK_SIZE, r * BLOCK_SIZE))
                elif tile == "64" or tile == "65":
                    self.blocks.add(block.Block(c * BLOCK_SIZE, r * BLOCK_SIZE))
                elif tile == ">":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "left"))
                elif tile == "<":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "right"))
                elif tile == "P":
                    self.player_location = (c * BLOCK_SIZE, r * BLOCK_SIZE)

        return self.blocks
