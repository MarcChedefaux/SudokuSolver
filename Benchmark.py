from Solvers.ISolver import ISolver
from Solvers.BasicBacktracker import BasicBacktracker
from Solvers.OrderedBacktracker import OrderedBacktracker
from Solvers.CachedBacktracker import CachedBacktracker
from Grid import Grid
from tqdm import tqdm
import pandas as pd
import numpy as np
import time

if __name__ == "__main__":
    df = pd.read_csv("data/sudoku-3m.csv")

    solver = CachedBacktracker()
    solver.Init()

    times = []

    benchmark_start = time.perf_counter()
    for index, rows in tqdm(df.iterrows(), total=df.shape[0]):
        grid = Grid(rows.puzzle)
        start_time = time.perf_counter()
        result = solver.Compute(grid)
        stop_time = time.perf_counter()

        times.append(stop_time - start_time)

        if time.perf_counter() - benchmark_start >= 15 * 60:
            break

        assert result.to_string() == rows.solution

    solver.Clean()

    times = np.array(times)
    times = pd.DataFrame(times, columns=["times"])
    times.to_csv("output_benchmark/cached_backtracker.csv")
