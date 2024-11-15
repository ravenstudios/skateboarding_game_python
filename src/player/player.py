import pygame
from constants import *
import main_entity

import os
from player import sound_manager, input_handler, movement_handler, collision_handler, animation_handler

class Player(main_entity.Main_entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.max_speed = 5
        self.acceleration = 5
        self.friction = 0.02
        self.push_power = 0
        self.lift = -10
        self.grav = 0.3
        self.vel = 0
        self.max_vel = -10
        self.grind_speed = 1.5
        self.grind_friction = 0.1
        self.is_jumping = False
        self.is_grinding = False
        self.is_on_ground = False  # Track if player is on the ground
        self.is_stopped = False
        self.dir = "right"
        self.cam_offset = 0
        self.is_grind_btn_held = False

        self.y_sprite_sheet_index = 0
        self.can_play_landing_sound = False

        self.sound_manager = sound_manager.SoundManager()
        self.input_handler = input_handler.InputHandler(self)
        self.movement_handler = movement_handler.MovementHandler(self)
        self.collision_handler = collision_handler.CollisionHandler(self)
        self.animation_handler = animation_handler.AnimationHandler(self)


    def update(self, events, cam_offset, objects):
        self.input_handler.check_keyboard(events)
        self.movement_handler.movement()
        self.animation_handler.update_animations()
        self.collision_handler.check_collisions(objects)
        self.update_cam_offset(cam_offset)
        self.animate()
        self.cam_offset = cam_offset



    def reset(self):
        self.rect.x = 200
        self.rect.y = 0
