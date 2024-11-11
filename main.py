from constants import *
import pygame

import state_manager

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
pygame.mixer.init()

state_manager = state_manager.State_manager()



def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((100, 100, 100))#background

    state_manager.draw(surface)
    pygame.display.flip()




def update():
    state_manager.update()


if __name__ == "__main__":
    main()
