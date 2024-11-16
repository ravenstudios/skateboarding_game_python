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

        # Process blocks as horizontal runs
        for r, row in enumerate(rows):
            start_col = None
            for c, tile in enumerate(row):
                if tile == "0":  # Block tile
                    if start_col is None:
                        start_col = c  # Start a new block run
                else:
                    if start_col is not None:  # End the block run
                        self._add_block(start_col, c - 1, r)
                        start_col = None
                # Handle end of row
                if start_col is not None and c == len(row) - 1:
                    self._add_block(start_col, c, r)

                if tile == "1":
                    self.blocks.add(rail.Rail(c * BLOCK_SIZE, r * BLOCK_SIZE))
                elif tile == "3":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "left"))
                elif tile == "2":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "right"))
                elif tile == "P":
                    self.player_location = (c * BLOCK_SIZE, r * BLOCK_SIZE)

        return self.blocks

    def _add_block(self, start_col, end_col, row):
        """Create a single block for a run of contiguous block tiles."""
        x = start_col * BLOCK_SIZE
        y = row * BLOCK_SIZE
        width = (end_col - start_col + 1) * BLOCK_SIZE
        height = BLOCK_SIZE  # Assuming one-row-high blocks for now
        self.blocks.add(block.Block(x, y, width, height))
