
import pygame
from constants import *
import main_entity
import block
import rail
import ramp


class Player(main_entity.Main_entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.max_speed = 10
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



    def check_keyboard(self, events):
        for event in events:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    if self.dir == "right":
                        self.push_power = 0
                    self.dir = "left"
                    self.push()

                if event.key == pygame.K_RIGHT:
                    if self.dir == "left":
                        self.push_power = 0
                    self.dir = "right"
                    self.push()

                if event.key == pygame.K_SPACE:
                    self.jump()

                if event.key == pygame.K_DOWN:
                    self.duck()

    def update_animations(self):

        if self.dir == "left":
            self.y_sprite_sheet_index = 0

        if self.dir == "right":
            self.y_sprite_sheet_index = 1

        if self.is_jumping == True:
            if self.dir == "right":
                self.y_sprite_sheet_index = 3
            else:
                self.y_sprite_sheet_index = 3



    def movement(self):
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

        self.push_sound.play()
        if self.push_power < self.max_speed:
            self.push_power += self.acceleration






    def duck(self):
        pass



    def check_collisions(self, objects):
        # Get all collisions with objects in the group
        collisions = pygame.sprite.spritecollide(self, objects, False, pygame.sprite.collide_mask)
        if collisions:
            for obj in collisions:
                if isinstance(obj, block.Block):  # Check if the object is a block
                    # Check if colliding from the top
                    if self.rect.bottom > obj.rect.top and self.rect.top < obj.rect.top:
                        # Top collision detected
                        self.vel = 0  # Reset vertical velocity
                        self.on_ground = True
                        self.is_jumping = False  # Player is now on the ground
                        self.rect.bottom = obj.rect.top  # Position the player on top of the block
                        if self.can_play_landing_sound:

                            self.landing_sound.play()
                            self.can_play_landing_sound = False
                        return  # Exit after top collision to prevent side adjustment

                    # Otherwise, check for side collisions only if it's not a top collision
                    elif (self.rect.right > obj.rect.left and self.rect.left < obj.rect.right) or (self.rect.left > obj.rect.right and self.rect.right < obj.rect.left):
                        # Side collision detected
                        self.push_power = 0
                        if self.dir == "left":
                            self.rect.left = obj.rect.right  # Prevent movement into the block from the left
                        else:
                            self.rect.right = obj.rect.left  # Prevent movement into the block from the right
                        return  # Exit after side collision to prevent further adjustments

                if isinstance(obj, rail.Rail):


                    self.rail_sound.play()
                    self.rect.bottom = obj.rect.top
                    self.push_power = self.max_speed * self.grind_speed
                    self.vel = 0  # Reset vertical velocity
                    self.on_ground = True
                    self.is_jumping = False
                    self.is_grinding = True


                if isinstance(obj, ramp.Ramp):
                    self.rect.bottom = obj.rect.top
                    self.push_power = self.max_speed * self.grind_speed
                    self.vel = self.lift * 2  # Reset vertical velocity
                    self.on_ground = False
                    self.is_jumping = False
                    self.is_grinding = False


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
