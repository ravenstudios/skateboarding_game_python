import pygame


class InputHandler():

    def __init__(self, player):
        self.player = player


    def check_keyboard(self, events):
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                    button = event.button

                    if button == 12:
                        self.player.duck()

                    if button == 13:
                        self.player.movement_handler.left()

                    if button == 14:
                        self.player.movement_handler.right()

                    if button == 0:
                        self.player.movement_handler.jump()

                    if button == 1:
                        self.player.movement_handler.push()

                    if button == 3:
                        self.player.is_grind_btn_held = True


            if event.type == pygame.JOYBUTTONUP:
                    button = event.button

                    if button == 3:
                        # if not self.player.is_grinding:
                        self.player.is_grind_btn_held = False
                        self.player.is_grinding = False



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.movement_handler.left()

                if event.key == pygame.K_RIGHT:
                    self.player.movement_handler.right()

                if event.key == pygame.K_SPACE:
                    self.player.movement_handler.jump()

                if event.key == pygame.K_DOWN:
                    self.player.movement_handler.duck()

                if event.key == pygame.K_v:
                    self.player.movement_handler.push()
