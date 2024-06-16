from abc import ABC, abstractmethod
from Grid import Grid


class ISolver(ABC):
    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def Compute(self, grid: Grid) -> Grid:
        pass

    @abstractmethod
    def Clean(self):
        pass
