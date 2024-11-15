
import pygame
from constants import *
import player
import os
class Main_entity(pygame.sprite.Sprite):

    spritesheet = None


    def __init__(self, x, y):
        super().__init__()

        if Main_entity.spritesheet is None:
             path = os.path.join(os.path.dirname(__file__), "..", "assets/imgs/Char-Sheet.png")
             Main_entity.spritesheet = pygame.image.load(path).convert_alpha()
             scaled_width, scaled_height = Main_entity.spritesheet.get_size()
             Main_entity.spritesheet = pygame.transform.scale(Main_entity.spritesheet, (scaled_width * SCALER, scaled_height * SCALER))
        self.x = x
        self.y = y
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)




        self.spritesheet = Main_entity.spritesheet
        self.y_sprite_sheet_index = 0
        self.frame = 0
        self.max_frame = (self.spritesheet.get_width() // BLOCK_SIZE) - 1
        self.animation_speed = 10
        self.ticks_till_frame_change = self.animation_speed

        self.mask = pygame.mask.from_surface(self.image)
        self.mask_img = self.mask.to_surface()



    def update(self, cam_offset):
        self.update_cam_offset(cam_offset)
        # only in on screen
        if self.rect.x > -BLOCK_SIZE and self.rect.x < GAME_WIDTH:
            self.animate()


    def draw(self, surface):
        image = pygame.Surface([self.rect.width, self.rect.height])
        image.fill((200, 0, 200))
        surface.blit(image, (0, 50))
        surface.blit(self.mask_img, (50, 50))

    def update_cam_offset(self, cam_offset):
        self.rect.x += cam_offset



    def get_image_from_sprite_sheet(self, row, col):
        if row < 0 or row > self.spritesheet.get_width():
            raise ValueError("row is either below 0 or larger than spritesheet")
        if col < 0 or col > self.spritesheet.get_height():
            raise ValueError("col is either below 0 or larger than spritesheet")

        # image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])

        image = pygame.Surface([self.rect.width, self.rect.height], pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), (row * (self.rect.width), col  * (self.rect.height) , self.rect.width, self.rect.height))
        return image



    def animate(self):
        if self.animation_speed != 0:
            self.ticks_till_frame_change -= 1

            if self.ticks_till_frame_change <= 0:
                self.frame += 1
                self.ticks_till_frame_change = self.animation_speed  # Reset the countdown (or change as needed)


            if self.frame > self.max_frame:
                self.frame = 0

        self.image = self.get_image_from_sprite_sheet(self.frame, self.y_sprite_sheet_index)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_img = self.mask.to_surface()
