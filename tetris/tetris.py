from consts import Movements
import pygame
from piece import Piece


class Tetris(pygame.sprite.Sprite):
    def __init__(self, font, screen):
        super().__init__()
        self.switch = None
        self.shape = Piece.generate_piece(screen)
        self.image = pygame.display.get_surface().copy()
        self.image.fill((0, 0, 0))
        font.render_to(self.image, (10, 30), 'Score: 0', fgcolor=pygame.Color('orange'))
        self.rect = self.image.get_rect()

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.switch:
                    self.switch()
