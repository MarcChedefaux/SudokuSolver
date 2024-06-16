from typing import Tuple
import numpy as np
from tabulate import tabulate


def parse_grid(grid: str) -> np.ndarray:
    res = np.zeros((9, 9), dtype=np.uint8)
    for i in range(81):
        if grid[i] != ".":
            res[i // 9][i % 9] = grid[i]
    return res


class Grid:
    def __init__(self) -> None:
        self.sudoku = np.zeros((9, 9), dtype=np.uint8)

    def __init__(self, grid: str):
        self.sudoku = parse_grid(grid)

    def to_string(self) -> str:
        res = ""
        for i in range(9):
            for j in range(9):
                if self.get(i, j) == 0:
                    res += "."
                else:
                    res += str(self.get(i, j))
        return res

    def get(self, x: int, y: int) -> int:
        return self.sudoku[x][y]

    def set(self, x: int, y: int, value: int) -> None:
        self.sudoku[x][y] = value

    def print(self):
        print(tabulate(self.sudoku, tablefmt="fancy_grid"))


def valid_vertical_line(grid: Grid, index: int) -> bool:
    values = set()
    for i in range(9):
        val = grid.get(index, i)
        if val != 0:
            if val in values:
                return False
            values.add(val)
    return True


def valid_horizontal_line(grid: Grid, index: int) -> bool:
    values = set()
    for i in range(9):
        val = grid.get(i, index)
        if val != 0:
            if val in values:
                return False
            values.add(val)
    return True


def get_pos_square(x: int, y: int) -> Tuple[int, int]:
    return (x - x % 3, y - y % 3)


def valid_square(grid: Grid, x: int, y: int) -> bool:
    values = set()
    sx, sy = get_pos_square(x, y)
    for i in range(3):
        for j in range(3):
            val = grid.get(sx + i, sy + j)
            if val != 0:
                if val in values:
                    return False
                values.add(val)
    return True


def valid_position(grid: Grid, x: int, y: int) -> bool:
    return (
        valid_vertical_line(grid, x)
        & valid_horizontal_line(grid, y)
        & valid_square(grid, x, y)
    )


def valid_sudoku(grid: Grid) -> bool:
    res = True
    for i in range(9):
        res &= valid_horizontal_line(grid, i)
        res &= valid_vertical_line(grid, i)
        res &= valid_square(grid, (i // 3) * 3, (i % 3) * 3)

    return res


if __name__ == "__main__":
    g = Grid(
        ".98543726643278591527619843914735268876192435235486179462351987381927654759864312"
    )
    g.print()
    print(valid_square(g, 0, 0))
