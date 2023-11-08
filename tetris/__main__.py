from tetris import Tetris
from scene import Scene
import pygame


def main():
    font = pygame.freetype.SysFont(None, 20)
    font.origin = True

    screen = pygame.display.set_mode((300, 600))
    clock = pygame.time.Clock()
    scene = pygame.sprite.GroupSingle()

    ame = Tetris(font, screen)
    start = Scene()
    game.switch = lambda: scene.add(start)
    start.switch = lambda: scene.add(game)
    scene.add(start)
    dt = 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        screen.fill((200, 200, 200))
        scene.draw(screen)

        pygame.display.update()
        scene.update(events, dt)
        dt = clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    main()
