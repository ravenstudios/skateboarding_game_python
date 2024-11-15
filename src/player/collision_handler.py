import pygame
from constants import *
import block
import rail
import ramp



class CollisionHandler():
    def __init__(self, player):
        self.player = player


    def check_collisions(self, objects):
        collisions = pygame.sprite.spritecollide(self.player, objects, False, )
        if collisions:
            for obj in collisions:
                if isinstance(obj, block.Block):  # Check if the object is a block
                    # Top collision (falling onto a block)
                    if self.player.vel > 0 and self.player.rect.bottom > obj.rect.top and self.player.rect.top < obj.rect.top:

                        # Position player on top of the block
                        self.player.rect.bottom = obj.rect.top
                        self.player.vel = 0  # Reset vertical velocity
                        self.player.is_on_ground = True
                        self.player.is_jumping = False  # Player is now on the ground
                        self.player.is_grinding = False
                        # self.player.is_grind_btn_held = False
                        if self.player.can_play_landing_sound:
                            self.player.sound_manager.landing_sound.play()
                            self.player.can_play_landing_sound = False
                        return  # Exit after top collision

                    # Side collisions
                    if self.player.rect.right > obj.rect.left and self.player.rect.left < obj.rect.right:
                            self.player.is_stopped = True
                            if self.player.dir == "left" and self.player.rect.left < obj.rect.right:  # Colliding from left
                                self.player.rect.left = obj.rect.right
                            elif self.player.dir == "right" and self.player.rect.right > obj.rect.left:  # Colliding from right
                                self.player.rect.right = obj.rect.left
                            self.player.push_power = 0  # Reset push power on side collision
                            return  # Exit after side collision
                        # Bottom collision (hitting head on a block)


                    # if self.player.rect.top < obj.rect.bottom and self.player.vel < 0:
                    #         if abs(self.player.rect.midtop[0] - obj.rect.midbottom[0]) < BLOCK_SIZE // 2:
                    #             self.player.rect.top = obj.rect.bottom
                    #             self.player.vel = 0
                    #             return  # Exit after bottom collision
                    #
                    #


                if isinstance(obj, rail.Rail):
                    if self.player.is_grind_btn_held:
                        if self.player.rect.y < obj.rect.y:
                            self.player.sound_manager.rail_sound.play()
                            self.player.rect.bottom = obj.rect.top
                            self.player.push_power = self.player.max_speed * self.player.grind_speed
                            self.player.vel = 0  # Reset vertical velocity
                            self.player.is_on_ground = True
                            self.player.is_jumping = False
                            self.player.is_grinding = True
                            return


                if isinstance(obj, ramp.Ramp):
                    if self.player.dir == obj.dir:
                        self.player.rect.bottom = obj.rect.top
                        self.player.push_power = self.player.max_speed * self.player.grind_speed
                        self.player.vel = self.player.lift * 2  # Reset vertical velocity
                        self.player.is_on_ground = False
                        self.player.is_jumping = False
                        self.player.is_grinding = False
                        return


        else:
            self.player.is_on_ground = False
            # self.player.is_grinding = False
