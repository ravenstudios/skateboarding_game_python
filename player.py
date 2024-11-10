# push -> w key for giving the skateboard a small push using physics
# jump -> space for jump. Must have physics to use velocity
# duck -> down arrow to make player half size to go under objects
# Player must use the pygame.sprite.Sprite class. this dosnt have to be done first but must be refractored in.
# Must have draw and update functions.
# A camera system will be used to side scroll, we will add that later.
import pygame
from constants import *
import main_entity




class Player(main_entity.Main_entity):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.max_speed = 10
        self.acceleration = 0.5
        self.deceleration = 0.2
        self.push_power = 0

        self.height = height
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT - self.height - 64  # Start position 64 pixels above the game height
        self.width = width

        self.speed = 5
        self.lift = -10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.grav = 0.3
        self.vel = 0
        self.max_vel = -10
        self.started = False
        self.on_ground = True  # Track if player is on the ground

        self.ground_level = GAME_HEIGHT - 64  # New ground level, 64 pixels above GAME_HEIGHT
        self.y_sprite_sheet_index = 0



    def update(self, cam_offset):
        print(self.y_sprite_sheet_index)
        keys = pygame.key.get_pressed()

        # Check if space key is pressed and player is on the ground to jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.flap()



        self.push()

        self.gravity()
        self.check_ground_collision()

        self.rect.x += cam_offset
        self.animate()

    def gravity(self):
        # Apply gravity only if the player is in the air
        if not self.on_ground:
            self.vel += self.grav
            self.rect.y += self.vel

        # Cap the downward velocity
        if self.vel < self.max_vel:
            self.vel = self.max_vel

    def push(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y_sprite_sheet_index = 1
            if self.push_power < self.max_speed:
                self.push_power += self.acceleration
        else:
            if self.push_power > 0:
                self.push_power -= self.deceleration
                if self.push_power < 0:
                    self.push_power = 0
        self.rect.x += self.push_power

    def check_ground_collision(self):
        # Check if the player has hit the new ground level
        if self.rect.bottom >= self.ground_level:
            self.rect.bottom = self.ground_level
            self.vel = 0  # Reset vertical velocity when hitting the ground
            self.on_ground = True  # Player is now on the ground
            self.y_sprite_sheet_index = 1
        else:
            # If player is not on the ground, set on_ground to False
            self.on_ground = False

    def flap(self):
        self.y_sprite_sheet_index = 3
        # Allow jumping only if the player is on the ground
        if not self.started:
            self.started = True
        if self.on_ground:
            self.vel = self.lift  # Apply lift to velocity
            self.on_ground = False  # Set on_ground to False since player is now in the air
