from enum import Enum


class pieces(Enum):
    box = "⏹️"
    piece = "🔳"


class Display(Enum):
    width = 650
    height = 500


class Movements(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    ROTATE = 4
