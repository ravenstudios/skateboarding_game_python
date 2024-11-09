# push -> w key for giving the skateboard a small push using physics
# jump -> space for jump. Must have physics to use velocity
# duck -> down arrow to make player half size to go under objects
# Player must use the pygame.sprite.Sprite class. this dosnt have to be done first but must be refractored in.
# Must have draw and update functions.
# A camera system will be used to side scroll, we will add that later.
import pygame, random
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT
        self.width = width
        self.height = height
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)





    def update(self):
        self.key_input()


    def key_input(self):

        keys = pygame.key.get_pressed()

        # if keys[pygame.K_LEFT]:
        #
        #     if self.rect.x > 0:
        #         self.rect.x += -self.speed
        #
        # if keys[pygame.K_RIGHT]:
        #     if self.rect.left < GAME_WIDTH:
        #         self.rect.x += self.speed
