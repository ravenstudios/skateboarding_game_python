import os
import pygame

from constants import *

from player import (player, skater_avatar)
from objects import (block, rail, ramp)

import map
import camera
import title
import background_manager



class State_manager():
    def __init__(self):
        self.state = 0
        self.is_paused = False
        self.camera = camera.Camera()
        self.map = map.Map()
        self.blocks = self.map.load("maps/lvl1.csv")
        print(f"Blokcs:{self.blocks}")
        self.player_group = pygame.sprite.Group()
        self.title_group = pygame.sprite.Group()
        self.title_group.add(title.Title(50, 50))

        self.player = player.Player(self.map.player_location[0], self.map.player_location[1])
        self.skater_avatar = skater_avatar.SkaterAvatar(self.map.player_location[0], self.map.player_location[1], self.player)
        self.player_group.add(self.player, self.skater_avatar)

        self.background_manager = background_manager.BackgroundManager()

        self.is_title_music_playing = False
        self.is_stage_music_playing = False

        self.visible_blocks = pygame.sprite.Group()  # Add a visible blocks group

    def update(self, events):
        self.check_keyboard()

        # Title Screen
        if self.state == 0:
            self.title_group.update()
            if not self.is_title_music_playing:
                path = os.path.join(os.path.dirname(__file__), "..", "assets/sounds/Skate Game Title.mp3")
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(-1)

                self.is_title_music_playing = True
                self.is_stage_music_playing = False

        # Main Game Loop
        if self.state == 1:
            if not self.is_stage_music_playing:
                pygame.mixer.music.stop()
                self.is_title_music_playing = False
                self.is_stage_music_playing = True

                path = os.path.join(os.path.dirname(__file__), "..", "assets/sounds/Stage 1.mp3")
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(-1)

            cam_offset = self.camera.update_offset(self.player)
            self.background_manager.update(cam_offset)

            # Update the visible blocks only once
            self.visible_blocks = self.reduce_objects(self.blocks)
            self.blocks.update(cam_offset)
            self.player.update(events, cam_offset, self.visible_blocks)
            self.skater_avatar.update()

        # Pause
        if self.state == 2:
            pass

    def check_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            pygame.time.delay(500)
            self.state = 1

        if keys[pygame.K_p]:
            if not self.is_paused:
                self.state = 2
                self.is_paused = True

            else:
                self.is_paused = False
                self.state = 1



    def draw(self, surface):
        if self.state == 0:
            self.title_group.draw(surface)

        if self.state == 1:
            # Only draw the visible blocks group
            self.background_manager.draw_bg(surface)
            self.background_manager.draw_mg(surface)
            self.background_manager.draw_fg(surface)
            self.visible_blocks.draw(surface)
            self.player_group.draw(surface)

            # FOR TESTING
            self.player.animation_handler.draw_stats(surface)

        if self.state == 2:
            pass

    def reduce_objects(self, group):
        return group
        # Compute and return only the visible objects
        return pygame.sprite.Group(
            obj for obj in group if -GAME_WIDTH <= obj.rect.left < GAME_WIDTH * 2 and 0 <= obj.rect.y < GAME_HEIGHT + BLOCK_SIZE
        )
