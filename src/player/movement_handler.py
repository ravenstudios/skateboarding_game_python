from constants import *


class MovementHandler():
    def __init__(self, player):
        self.player = player


    def right(self):
        if self.player.dir == "left":
            self.player.is_stopped = False
            self.player.push_power = 0
        self.player.dir = "right"




    def left(self):
        if self.player.dir == "right":
            self.player.is_stopped = False
            self.player.push_power = 0
        self.player.dir = "left"


    def movement(self):
        if self.player.is_on_ground and not self.player.is_stopped:
            self.push()
        if self.player.dir == "left":
            self.player.rect.x -= self.player.push_power
        else:
            self.player.rect.x += self.player.push_power


        if self.player.rect.y > GAME_HEIGHT:
            self.player.rect.y = 0
            self.player.rect.x = 0



        if self.player.push_power > 0:
            if self.player.is_grinding:
                self.player.push_power -=self.player.grind_friction
            else:
                self.player.push_power -= self.player.friction
            if self.player.push_power < 0:
                self.player.push_power = 0

        if not self.player.is_on_ground:
            self.player.vel += self.player.grav
            self.player.rect.y += self.player.vel

        # Cap the downward velocity
        if self.player.vel < self.player.max_vel:
            self.player.vel = self.player.max_vel


    def duck(self):
        pass



    def push(self):
        if self.player.push_power < self.player.max_speed:
            self.player.push_power += self.player.acceleration


    def jump(self):
        if not self.player.is_jumping:

            self.player.sound_manager.jump_sound.play()
            self.player.vel = self.player.lift  # Apply lift to velocity
            self.player.is_on_ground = False  # Set on_ground to False since player is now in the air
            self.player.is_jumping = True
            self.player.is_grinding = False
            # self.player.is_grind_btn_held = False
            self.player.can_play_landing_sound = True
