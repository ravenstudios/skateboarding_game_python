import os
import csv
import pygame

from constants import *

from objects import (block, rail, ramp)


class Map(object):
    def __init__(self):
        self.blocks = pygame.sprite.Group()
        self.player_location = (BLOCK_SIZE, 0)

    def load(self, map_file):
        map_path = os.path.join(os.path.dirname(__file__), "..", map_file)
        with open(map_path, newline='') as csvfile:

            reader = csv.reader(csvfile)
            rows = list(reader)

        for r, row in enumerate(rows):
            for c, tile in enumerate(row):
                # print(f"R:{r}  C:{c}  Tile:{tile}")
                if tile == "1":
                    self.blocks.add(rail.Rail(c * BLOCK_SIZE, r * BLOCK_SIZE))
                elif tile == "0":
                    self.blocks.add(block.Block(c * BLOCK_SIZE, r * BLOCK_SIZE))
                elif tile == "3":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "left"))
                elif tile == "2":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "right"))
                elif tile == "P":
                    self.player_location = (c * BLOCK_SIZE, r * BLOCK_SIZE)

        return self.blocks
