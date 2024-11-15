import pygame
from constants import *
import main_entity
import os

class Title(main_entity.Main_entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Set width and height to 90x61
        self.width = 90 * SCALER * 2
        self.height = 61 * SCALER * 2

        # Recreate the image with the correct dimensions
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha()  # Ensure transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        # Load and scale the spritesheet to fit within 90x61
        path = os.path.join(os.path.dirname(__file__), "..", "assets/imgs/Title-Sheet.png")
        self.spritesheet = pygame.image.load(path).convert_alpha()
        scaled_width, scaled_height = self.spritesheet.get_size()
        self.spritesheet = pygame.transform.scale(self.spritesheet, (scaled_width * SCALER * 2, scaled_height * SCALER * 2))

        # Set animation parameters
        self.max_frame = 27
        self.animation_speed = 10

    def update(self):
        self.animate()
