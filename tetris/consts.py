from enum import Enum

width, height = 500, 700
fill_color = (0, 0, 0)

# Board with 10 columns and 20 rows
BOARD_WIDTH = 10
BOARD_HEIGHT = 30
BOARD = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

PIECE_COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
]

PIECE_SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]


class Movements(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    ROTATE = 4
