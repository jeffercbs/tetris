from consts import Movements, pieces


def rotate(x: int, y: int) -> (int, int):
    return (x, y + 1) if (x == 0 and y == 0) else (x - 1, y + 1)


def move_piece(m: Movements, squares: list[list[str]]) -> list[list[str]]:
    new_squares = [[pieces.box.value] * 10 for _ in range(10)]
    r = [(0, 0), (0, 0), (0, 0), (0, 0)]
    ri = 0

    for i_row, row in enumerate(squares):
        for i_col, col in enumerate(row):

            if col == pieces.piece.value:
                new_row = 0
                new_col = 0

                match m:
                    case Movements.LEFT:
                        new_row = i_row
                        new_col = i_col - 1
                    case Movements.RIGHT:
                        new_row = i_row
                        new_col = i_col + 1
                    case Movements.DOWN:
                        new_row = i_row + 1
                        new_col = i_col
                    case Movements.ROTATE:
                        rotation = r[ri] = rotate(i_row, i_col)
                        ri += 1

                        new_row = rotation[0]
                        new_col = rotation[1]
                    case _:
                        pass

                if (new_row < 0 or new_row > 9) or (new_col < 0 or new_col > 9):
                    return squares

                new_squares[new_row][new_col] = pieces.piece.value

    return new_squares


class KeyListener:
    def __init__(self, squares: list[list[str]], rotation: int):
        self.squares = squares
        self.rotation = rotation

    def _move(self, m: Movements):
        (self.squares, self.rotation) = move_piece(m, self.squares)

    def _left(self):
        self._move(Movements.LEFT)

    def _right(self):
        self._move(Movements.RIGHT)

    def _down(self):
        self._move(Movements.DOWN)

    def _rotate(self):
        self._move(Movements.ROTATE)
