import pygame


class AnimationHandler(object):
    """docstring for AnimationHandler."""

    def __init__(self, player):
        self.player = player


    def update_animations(self):

        if self.player.dir == "left":
            self.player.y_sprite_sheet_index = 11

        if self.player.dir == "right":
            self.player.y_sprite_sheet_index = 3

        if self.player.is_jumping == True:
            if self.player.dir == "right":
                self.player.y_sprite_sheet_index = 5
            else:
                self.player.y_sprite_sheet_index = 13

        if self.player.is_grinding == True:
            if self.player.dir == "right":
                self.player.y_sprite_sheet_index = 7
            else:
                self.player.y_sprite_sheet_index = 15


    def draw_stats(self, surface):

        stats = [
            f"X: {self.player.rect.x}   Y: {self.player.rect.y}",
            f"VEL: {self.player.vel:.2f}   PP: {self.player.push_power:.2f}",
            f"JUMPING: {self.player.is_jumping}",
            f"GRINDING: {self.player.is_grinding}",
            f"ON GROUND: {self.player.is_on_ground}",
            f"CAM_OFFSET: {self.player.cam_offset}",
            f"GRND_BTN: {self.player.is_grind_btn_held}",
        ]
        font_size = 36
        font = pygame.font.Font(None, font_size)
        image = pygame.Surface([300, font_size * len(stats)], pygame.SRCALPHA)
        image.fill((100, 100, 100, 100))

        # Render each line and blit it with an offset for each new line
        y_offset = 0
        for line in stats:
            text_surface = font.render(line, True, (255, 255, 255))
            image.blit(text_surface, (0, y_offset))
            y_offset += font.get_linesize()  # Move down for the next line
        surface.blit(image, (0, 0))
