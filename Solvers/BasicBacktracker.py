from Grid import *
from typing import Tuple
from Solvers.ISolver import ISolver


def findNextFreeSpot(grid: Grid) -> Tuple[int, int]:
    for i in range(9):
        for j in range(9):
            if grid.get(i, j) == 0:
                return i, j
    return -1, -1


class BasicBacktracker(ISolver):

    def Init(self):
        return

    def Compute(self, grid: Grid) -> Grid:
        x, y = findNextFreeSpot(grid)
        if x == -1 & y == -1:
            return grid

        for value in range(1, 10):
            grid.set(x, y, value)
            if not valid_position(grid, x, y):
                continue
            res = self.Compute(grid)
            if res != None:
                return res

        grid.set(x, y, 0)
        return None

    def Clean(self):
        return
