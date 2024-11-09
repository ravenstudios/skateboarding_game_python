# push -> w key for giving the skateboard a small push using physics
# jump -> space for jump. Must have physics to use velocity
# duck -> down arrow to make player half size to go under objects
# Player must use the pygame.sprite.Sprite class. this dosnt have to be done first but must be refractored in.
# Must have draw and update functions.
# A camera system will be used to side scroll, we will add that later.
import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.height = BLOCK_SIZE
        self.x = 0 + 64
        self.y = GAME_HEIGHT - self.height
        self.width = BLOCK_SIZE

        self.max_speed = 10
        self.acceleration = 0.5
        self.deceleration = 0.2
        self.push_power = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.push()

    def push(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_w]:
            if self.push_power < self.max_speed:
                self.push_power += self.acceleration


        else:
            if self.push_power > 0:
                self.push_power -= self.deceleration
                if self.push_power < 0:
                    self.push_power = 0
        self.rect.x += self.push_power
