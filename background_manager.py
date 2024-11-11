import pygame
from constants import *



class Background_manager():
    def __init__(self):
        self.bg = Background("imgs/background.png", 3)
        self.mg = Background("imgs/midground.png", 30)
        self.fg = Background("imgs/foreground.png", 60)
        self.objs = [self.bg, self.mg, self.fg]

    def update(self, cam_offset):
        for obj in self.objs:
            obj.update(cam_offset)


    def draw_bg(self, surface):
        self.bg.draw(surface)

    def draw_mg(self, surface):
        self.mg.draw(surface)

    def draw_fg(self, surface):
        self.fg.draw(surface)

class Background():
    def __init__(self, file, scroll_speed):
        self.scroll_speed = scroll_speed
        self.img = pygame.image.load(file).convert_alpha()
        scaled_width, scaled_height = self.img.get_size()
        self.img1 = pygame.transform.scale(self.img, (scaled_width * SCALER, scaled_height * SCALER))
        self.img2 = self.img1
        self.x1 = 0
        self.x2 = GAME_WIDTH



    def draw(self, surface):
        surface.blit(self.img1, (self.x1, 0))
        surface.blit(self.img2, (self.x2, 0))



    def update(self, cam_offset):
        self.x1 += (cam_offset * self.scroll_speed) / 100
        self.x2 += (cam_offset * self.scroll_speed) / 100


        if self.x1 > GAME_WIDTH:
            self.x1 = -GAME_WIDTH
        if self.x2 > GAME_WIDTH:
            self.x2 = -GAME_WIDTH


        if self.x1 < -GAME_WIDTH:
            self.x1 = GAME_WIDTH
        if self.x2 < -GAME_WIDTH:
            self.x2 = GAME_WIDTH
