from Solvers.ISolver import ISolver
from Solvers.BasicBacktracker import BasicBacktracker
from Grid import Grid
from tqdm import tqdm
import pandas as pd
import numpy as np
import time

if __name__ == "__main__":
    df = pd.read_csv("data/sudoku-3m.csv")

    solver = BasicBacktracker()
    solver.Init()

    df_sample = df.sample(frac=0.000001)

    times = []

    for index, rows in tqdm(df_sample.iterrows(), total=df_sample.shape[0]):
        grid = Grid(rows.puzzle)
        start_time = time.perf_counter()
        result = solver.Compute(grid)
        stop_time = time.perf_counter()

        times.append(stop_time - start_time)

        assert result.to_string() == rows.solution

    solver.Clean()

    times = np.array(times)
    times = pd.DataFrame(times, columns=["times"])
    times.to_csv("output_benchmark/basicbacktracker.csv")