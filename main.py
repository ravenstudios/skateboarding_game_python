from constants import *
import pygame
import player
import block
import camera
import rail
import map
import ramp

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


camera = camera.Camera()
map = map.Map()
blocks = map.load("stage1.map")


player_group = pygame.sprite.Group()


player = player.Player(GAME_WIDTH // 2, 0)
player_group.add(player)


# for i in range(100):
#     blocks.add(block.Block(i * BLOCK_SIZE, GAME_HEIGHT - BLOCK_SIZE))
#
# for i in range(10):
#
#     blocks.add(rail.Rail(i * BLOCK_SIZE + (BLOCK_SIZE * 10), GAME_HEIGHT - BLOCK_SIZE * 3))
#
# for i in range(10):
#     blocks.add(block.Block(i * BLOCK_SIZE, GAME_HEIGHT - BLOCK_SIZE))
#     blocks.add(block.Block(i * BLOCK_SIZE + (BLOCK_SIZE * 2), GAME_HEIGHT - BLOCK_SIZE * 2))
#
# blocks.add(ramp.Ramp(32 * BLOCK_SIZE, GAME_HEIGHT - BLOCK_SIZE * 2, "right"))
#
# blocks.add(ramp.Ramp(35 * BLOCK_SIZE, GAME_HEIGHT - BLOCK_SIZE * 2, "left"))

# blocks = map.load_map()

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
