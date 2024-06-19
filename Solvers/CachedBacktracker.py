from types import UnionType
from typing import Any
from Grid import Grid
from Solvers.ISolver import ISolver
from Grid import *


def get_first_element(tuple: Tuple[int, int, int]) -> int:
    return tuple[0]


def to_square_number(x: int, y: int) -> int:
    return (x // 3) * 3 + y // 3


class CachedBacktracker(ISolver):
    def __init__(self):
        self.order = list()
        self.vertical_cache = []
        self.horizontal_cache = []
        self.square_cache = []

    def Init(self):
        return

    def PreCompute(self, grid: Grid) -> None:
        for i in range(9):
            self.vertical_cache.append(set(range(1, 10)))
            self.horizontal_cache.append(set(range(1, 10)))
            self.square_cache.append(set(range(1, 10)))

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
                else:
                    val = grid.get(i, j)
                    self.vertical_cache[i].remove(val)
                    self.horizontal_cache[j].remove(val)
                    self.square_cache[to_square_number(i, j)].remove(val)
        self.order.sort(key=get_first_element)

    def intersection_cached(self, x: int, y: int) -> set:
        return self.vertical_cache[x].intersection(
            self.horizontal_cache[y].intersection(
                self.square_cache[to_square_number(x, y)]
            )
        )

    def OrderedCompute(self, grid: Grid) -> Grid:
        if len(self.order) == 0:
            return grid

        c, x, y = self.order.pop(0)

        for value in self.intersection_cached(x, y):
            grid.set(x, y, value)
            self.vertical_cache[x].remove(value)
            self.horizontal_cache[y].remove(value)
            self.square_cache[to_square_number(x, y)].remove(value)
            res = self.OrderedCompute(grid)
            if res != None:
                return res
            else:
                self.vertical_cache[x].add(value)
                self.horizontal_cache[y].add(value)
                self.square_cache[to_square_number(x, y)].add(value)

        grid.set(x, y, 0)
        self.order.insert(0, (c, x, y))
        return None

    def Compute(self, grid: Grid) -> Grid:
        self.PreCompute(grid)
        solution = self.OrderedCompute(grid)
        self.horizontal_cache.clear()
        self.vertical_cache.clear()
        self.square_cache.clear()
        return solution

    def Clean(self):
        return
