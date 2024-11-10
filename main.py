from constants import *
import pygame
import player
import block
import camera



clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


camera = camera.Camera()

player_group = pygame.sprite.Group()

blocks = pygame.sprite.Group()

player = player.Player(GAME_WIDTH // 2, 0)
player_group.add(player)


for i in range(100):
    blocks.add(block.Block(i * BLOCK_SIZE, GAME_HEIGHT - BLOCK_SIZE))
blocks.add(block.Block(400, GAME_HEIGHT - BLOCK_SIZE * 2))



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

    blocks.draw(surface)
    player_group.draw(surface)

    pygame.display.flip()




def update():
    cam_offset = camera.update_offset(player)

    blocks.update(cam_offset)
    player_group.update(cam_offset, blocks)



if __name__ == "__main__":
    main()
