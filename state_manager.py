from constants import *
import pygame
import player
import block
import camera
import rail
import map
import ramp
import title


class State_manager():
    def __init__(self):



        self.state = 0
        self.is_paused = False
        self.camera = camera.Camera()
        self.map = map.Map()
        self.blocks = self.map.load("stage1.map")


        self.player_group = pygame.sprite.Group()
        self.title_group = pygame.sprite.Group()
        self.title_group.add(title.Title(50, 50))


        self.player = player.Player(GAME_WIDTH // 2, GAME_HEIGHT - BLOCK_SIZE * 2)
        self.player_group.add(self.player)
        self.is_title_music_playing = False
        self.is_stage_music_playing = False

    def update(self):
        self.check_keyboard()
        # Title Screen
        if self.state == 0:
            self.title_group.update()
            if not self.is_title_music_playing:

                pygame.mixer.music.load("sounds/Skate Game Title.mp3")
                pygame.mixer.music.play(-1)

                self.is_title_music_playing = True
                self.is_stage_music_playing = False
        # Main Game Loop
        if self.state == 1:

            if self.is_stage_music_playing == False:
                pygame.mixer.music.stop()
                self.is_title_music_playing = False
                self.is_stage_music_playing = True

                pygame.mixer.music.load("sounds/Stage 1.mp3")
                pygame.mixer.music.play(-1)


            cam_offset = self.camera.update_offset(self.player)
            self.blocks.update(cam_offset)
            self.player_group.update(cam_offset, self.blocks)

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
            pygame.time.delay(500)


    def draw(self, surface):
        if self.state == 0:
            self.title_group.draw(surface)

        if self.state == 1:
            self.blocks.draw(surface)
            self.player_group.draw(surface)

        if self.state == 2:
            pass
