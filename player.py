
import pygame
from constants import *
import main_entity
import block
import rail
import ramp


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
        self.on_ground = False  # Track if player is on the ground

        self.dir = "right"

        self.ground_level = GAME_HEIGHT + 200  # New ground level, 64 pixels above GAME_HEIGHT
        self.y_sprite_sheet_index = 0
        self.can_play_landing_sound = False

        self.push_sound = pygame.mixer.Sound("sounds/Kick.mp3")
        self.landing_sound = pygame.mixer.Sound("sounds/Land.mp3")
        self.rail_sound = pygame.mixer.Sound("sounds/Rail.mp3")
        self.jump_sound = pygame.mixer.Sound("sounds/Jump.mp3")

    def update(self, events, cam_offset, objects):
        self.check_keyboard(events)
        self.movement()
        self.update_animations()
        self.check_collisions(objects)
        self.update_cam_offset(cam_offset)
        self.animate()

    def reset(self):
        self.rect.x = 200
        self.rect.y = 0

    def check_keyboard(self, events):
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                    button = event.button

                    if button == 12:
                        self.duck()

                    if button == 13:
                        self.left()

                    if button == 14:
                        self.right()

                    if button == 0:
                        self.jump()

                    if button == 1:
                        self.push()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left()

                if event.key == pygame.K_RIGHT:
                    self.right()

                if event.key == pygame.K_SPACE:
                    self.jump()

                if event.key == pygame.K_DOWN:
                    self.duck()

                if event.key == pygame.K_v:
                    self.push()


    def right(self):
        if self.dir == "left":
            self.push_power = 0
        self.dir = "right"




    def left(self):
        if self.dir == "right":
            self.push_power = 0
        self.dir = "left"




    def update_animations(self):

        if self.dir == "left":
            self.y_sprite_sheet_index = 11

        if self.dir == "right":
            self.y_sprite_sheet_index = 3

        if self.is_jumping == True:
            if self.dir == "right":
                self.y_sprite_sheet_index = 5
            else:
                self.y_sprite_sheet_index = 13

        if self.is_grinding == True:
            if self.dir == "right":
                self.y_sprite_sheet_index = 7
            else:
                self.y_sprite_sheet_index = 13



    def movement(self):
        if self.on_ground:
            self.push()
        if self.dir == "left":
            self.rect.x -= self.push_power
        else:
            self.rect.x += self.push_power


        if self.rect.y > GAME_HEIGHT:
            self.rect.y = 0
            self.rect.x = 0



        if self.push_power > 0:
            if self.is_grinding:
                self.push_power -=self.grind_friction
            else:
                self.push_power -= self.friction
            if self.push_power < 0:
                self.push_power = 0

        if not self.on_ground:
            self.vel += self.grav
            self.rect.y += self.vel

        # Cap the downward velocity
        if self.vel < self.max_vel:
            self.vel = self.max_vel



    def push(self):

        # self.push_sound.play()
        if self.push_power < self.max_speed:
            self.push_power += self.acceleration






    def duck(self):
        pass



    def check_collisions(self, objects):
        # Get all collisions with objects in the group
        if self.is_jumping:
            surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)
            surface.fill((255, 255, 255, 255))  # Fill with white, fully opaque
            self.mask = pygame.mask.from_surface(surface)


        collisions = pygame.sprite.spritecollide(self, objects, False, pygame.sprite.collide_mask)
        if collisions:
            for obj in collisions:
                if isinstance(obj, block.Block):  # Check if the object is a block
                    # Top collision (falling onto a block)
                    if self.vel > 0 and self.rect.bottom > obj.rect.top and self.rect.top < obj.rect.top:

                        # Position player on top of the block
                        self.rect.bottom = obj.rect.top
                        self.vel = 0  # Reset vertical velocity
                        self.on_ground = True
                        self.is_jumping = False  # Player is now on the ground
                        if self.can_play_landing_sound:
                            self.landing_sound.play()
                            self.can_play_landing_sound = False
                        return  # Exit after top collision



                    # Bottom collision (hitting head on a block)
                    if self.rect.top < obj.rect.bottom and self.vel < 0:

                        self.rect.top = obj.rect.bottom
                        self.vel = 0
                        return  # Exit after bottom collision



                    # Side collisions
                    if self.rect.right > obj.rect.left and self.rect.left < obj.rect.right:

                        if self.dir == "left" and self.rect.left < obj.rect.right:  # Colliding from left
                            self.rect.left = obj.rect.right
                        elif self.dir == "right" and self.rect.right > obj.rect.left:  # Colliding from right
                            self.rect.right = obj.rect.left
                        self.push_power = 0  # Reset push power on side collision
                        return  # Exit after side collision




                if isinstance(obj, rail.Rail):

                    if self.rect.y < obj.rect.y:
                        self.rail_sound.play()
                        self.rect.bottom = obj.rect.top
                        self.push_power = self.max_speed * self.grind_speed
                        self.vel = 0  # Reset vertical velocity
                        self.on_ground = True
                        self.is_jumping = False
                        self.is_grinding = True
                        return


                if isinstance(obj, ramp.Ramp):
                    if self.dir == obj.dir:
                        self.rect.bottom = obj.rect.top
                        self.push_power = self.max_speed * self.grind_speed
                        self.vel = self.lift * 2  # Reset vertical velocity
                        self.on_ground = False
                        self.is_jumping = False
                        self.is_grinding = False
                        return


        else:
            self.on_ground = False
            self.is_grinding = False

    def jump(self):
        if not self.is_jumping:

            self.jump_sound.play()
            self.vel = self.lift  # Apply lift to velocity
            self.on_ground = False  # Set on_ground to False since player is now in the air
            self.is_jumping = True
            self.can_play_landing_sound = True
