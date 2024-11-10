
import pygame
from constants import *
import main_entity
import block

class Player(main_entity.Main_entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.max_speed = 10
        self.acceleration = 0.5
        self.friction = 0.2
        self.push_power = 0
        self.lift = -10
        self.grav = 0.3
        self.vel = 0
        self.max_vel = -10

        self.started = False
        self.on_ground = False  # Track if player is on the ground

        self.dir = "left"

        self.ground_level = GAME_HEIGHT + 200  # New ground level, 64 pixels above GAME_HEIGHT
        self.y_sprite_sheet_index = 0



    def update(self, cam_offset, objects):
        self.check_keyboard()
        self.movement()
        self.update_animations()
        self.check_collisions(objects)
        self.update_cam_offset(cam_offset)
        self.animate()



    def check_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jump()

        if keys[pygame.K_w]:
            self.push()

        if keys[pygame.K_LEFT]:
            self.dir = "left"
            self.push()

        if keys[pygame.K_RIGHT]:
            self.dir = "right"
            self.push()

        if keys[pygame.K_DOWN]:
            self.duck()


    def update_animations(self):

        if self.dir == "left":
            self.y_sprite_sheet_index = 0

        if self.dir == "right":
            self.y_sprite_sheet_index = 1

        if self.on_ground == False:
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
        if self.push_power < self.max_speed:
            self.push_power += self.acceleration






    def duck(self):
        pass



    def check_collisions(self, objects):
        collisions = pygame.sprite.spritecollide(self, objects, False)

        for obj in collisions:
            if type(obj) == block.Block:
                if self.rect.bottom > obj.rect.top and self.rect.top > obj.rect.top and not self.on_ground:
                    self.vel = 0  # Reset vertical velocity when hitting the ground
                    self.on_ground = True  # Player is now on the ground
                    self.rect.bottom = obj.rect.top
                    return

                elif self.rect.right > obj.rect.left or self.rect.left > obj.rect.right:
                    self.push_power = 0
                    if self.dir == "left":
                        self.rect.left = obj.rect.right
                    else:
                        self.rect.right = obj.rect.left
                    return


    def jump(self):
        if self.on_ground:


            # Allow jumping only if the player is on the ground
            if not self.started:
                self.started = True
            if self.on_ground:
                self.vel = self.lift  # Apply lift to velocity
                self.on_ground = False  # Set on_ground to False since player is now in the air
