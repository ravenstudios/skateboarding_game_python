from constants import *

class Camera(object):


    def __init__(self):
        pass

    def update_offset(self, player):
        return (-player.rect.x + GAME_WIDTH // 2, -player.rect.y + GAME_HEIGHT // 2)
