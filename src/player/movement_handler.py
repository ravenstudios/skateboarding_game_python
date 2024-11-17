from constants import *


class MovementHandler():
    def __init__(self, player):
        self.player = player


    def right(self):
        if self.player.dir == "left":
            self.player.is_stopped = False
            self.player.x_vel = 0
        self.player.dir = "right"




    def left(self):
        if self.player.dir == "right":
            self.player.is_stopped = False
            self.player.x_vel = 0
        self.player.dir = "left"


    def movement(self):
        if not self.player.is_stopped:
            self.player.x_vel += self.player.acceleration

        if self.player.dir == "left":
            self.player.rect.x -= self.player.x_vel
        else:
            self.player.rect.x += self.player.x_vel

        self.player.x_vel = max(self.player.max_speed, self.player.max_vel)


        if self.player.x_vel > 0:
            if self.player.is_grinding:
                self.player.x_vel -=self.player.grind_friction
            else:
                self.player.x_vel -= self.player.friction
            if self.player.x_vel < 0:
                self.player.x_vel = 0

        if not self.player.is_on_ground:
            self.player.vel += self.player.grav
            self.player.rect.y += self.player.vel

        # Cap the downward velocity
        if self.player.vel < self.player.max_vel:
            self.player.vel = self.player.max_vel


    def duck(self):
        pass



    def push(self):
        if self.player.x_vel < self.player.max_speed:
            self.player.x_vel += self.player.acceleration


    def jump(self):
        if not self.player.is_jumping:

            self.player.sound_manager.jump_sound.play()
            self.player.vel = self.player.lift  # Apply lift to velocity
            self.player.is_on_ground = False  # Set on_ground to False since player is now in the air
            self.player.is_jumping = True
            self.player.is_grinding = False
            # self.player.is_grind_btn_held = False
            self.player.can_play_landing_sound = True
