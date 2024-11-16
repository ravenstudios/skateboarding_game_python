from constants import *
import pygame

import state_manager

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
pygame.mixer.init()
pygame.font.init()

state_manager_obj = state_manager.State_manager()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

def main():
    running = True
    mute = False
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False



            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_m:

                    if mute:
                        mute = False
                        pygame.mixer.music.set_volume(1)
                    else:
                        mute = True
                        pygame.mixer.music.set_volume(0)

                if event.key == pygame.K_r:
                    state_manager_obj.player.reset()
        draw()
        update(events)
        clock.tick(TICK_RATE)

    pygame.quit()



def draw():
    surface.fill((100, 100, 100))#background

    state_manager_obj.draw(surface)
    pygame.display.flip()




def update(events):
    state_manager_obj.update(events)
    fps = clock.get_fps()
    pygame.display.set_caption(f"Pygame - FPS: {fps:.2f}")

if __name__ == "__main__":
    main()
