from consts import Display
from game import Game
import pygame
import sys

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((Display.width.value, Display.height.value))
    game = Game(screen)
    clock = pygame.time.Clock()
    running = True

    while (running):
        clock.tick(60)
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.init()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
