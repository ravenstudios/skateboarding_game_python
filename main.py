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
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update(events)
        clock.tick(TICK_RATE)

    pygame.quit()



def draw():
    surface.fill((100, 100, 100))#background

    state_manager.draw(surface)
    pygame.display.flip()




def update(events):
    state_manager.update(events)
    fps = clock.get_fps()
    pygame.display.set_caption(f"Pygame - FPS: {fps:.2f}")

if __name__ == "__main__":
    main()
