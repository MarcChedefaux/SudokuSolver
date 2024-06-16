from types import UnionType
from typing import Any
from Grid import Grid
from Solvers.ISolver import ISolver
from Grid import *


def get_first_element(tuple: Tuple[int, int, int]) -> int:
    return tuple[0]


class OrderedBacktracker(ISolver):
    def __init__(self):
        self.order = list()

    def Init(self):
        return

    def PreCompute(self, grid: Grid) -> None:
        for i in range(9):
            for j in range(9):
                if grid.get(i, j) == 0:
                    count = 0
                    for val in range(1, 10):
                        grid.set(i, j, val)
                        if valid_position(grid, i, j):
                            count += 1
                    grid.set(i, j, 0)
                    self.order.append((count, i, j))
        self.order.sort(key=get_first_element)

    def OrderedCompute(self, grid: Grid) -> Grid:
        if len(self.order) == 0:
            return grid

        c, x, y = self.order.pop(0)

        for value in range(1, 10):
            grid.set(x, y, value)
            if not valid_position(grid, x, y):
                continue
            res = self.OrderedCompute(grid)
            if res != None:
                return res

        grid.set(x, y, 0)
        self.order.insert(0, (c, x, y))
        return None

    def Compute(self, grid: Grid) -> Grid:
        self.PreCompute(grid)
        return self.OrderedCompute(grid)

    def Clean(self):
        return
