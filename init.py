
import numpy as np
import time
import os

def create_grid(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(" ".join(['□' if cell == 0 else '■' for cell in row]))

def count_neighbors(grid, row, col):
    rows, cols = grid.shape
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    count = 0
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            count += grid[r, c]
    return count

def next_generation(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)

    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_neighbors(grid, row, col)

            if grid[row, col] == 1 :
                if live_neighbors in [2, 3]:
                    new_grid[row, col] = 1
            else:  # Dead cell
                if live_neighbors == 3:
                    new_grid[row, col] = 1

    return new_grid

if __name__ == "__main__":

    rows, cols = 40, 40
    grid = create_grid(rows, cols)

    try:
        while True:
            display_grid(grid)
            grid = next_generation(grid)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
