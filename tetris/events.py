from piece import Piece
from consts import Movements


class Evens(Piece):
    def __init__(self):
        pass

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def move(self, movement):
        if movement == Movements.LEFT and self.x > 0 and not self.y == 560:
            self.x -= 20
        elif movement == Movements.RIGHT and self.x < 340 and not self.y == 560:
            self.x += 20
        elif movement == Movements.DOWN and self.y < 560 and not self.y == 560:
            self.y += 20
        elif movement == Movements.ROTATE and self.y < 560:
            self.rotate()