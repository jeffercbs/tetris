from consts import PIECE_SHAPES, PIECE_COLORS
import pygame
import random


class Piece(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image

    def generate_piece(self, ):
        shape = random.choice(PIECE_SHAPES)
        color = random.choice(PIECE_COLORS)

        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] == 1:
                    x = col * 20
                    y = row * 20

                    pygame.draw.rect(self.image, color, (x, y, 20, 20), 0)

        return shape
