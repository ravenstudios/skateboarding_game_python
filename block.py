# push -> w key for giving the skateboard a small push using physics
# jump -> space for jump. Must have physics to use velocity
# duck -> down arrow to make player half size to go under objects
# Player must use the pygame.sprite.Sprite class. this dosnt have to be done first but must be refractored in.
# Must have draw and update functions.
# A camera system will be used to side scroll, we will add that later.
import pygame, random
from constants import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = BLOCK_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0 ,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)





    def update(self, cam_offset):
        self.rect.x += cam_offset
