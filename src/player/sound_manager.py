import os
import pygame

class SoundManager():
    def __init__(self):
        kick_sound_path = os.path.join(os.path.dirname(__file__), "..", "..",  "assets/sounds/Kick.mp3")
        landing_sound_path = os.path.join(os.path.dirname(__file__), "..", "..",  "assets/sounds/Land.mp3")
        rail_sound_path = os.path.join(os.path.dirname(__file__), "..", "..",  "assets/sounds/Rail.mp3")
        jump_sound_path = os.path.join(os.path.dirname(__file__), "..", "..",  "assets/sounds/Jump.mp3")
        self.push_sound = pygame.mixer.Sound(kick_sound_path)
        self.landing_sound = pygame.mixer.Sound(landing_sound_path)
        self.rail_sound = pygame.mixer.Sound(rail_sound_path)
        self.jump_sound = pygame.mixer.Sound(jump_sound_path)
