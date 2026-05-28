import numpy as np
from config import GRID_SIZE

class Environment:
    def __init__(self):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE))

    def update_density(self, pythons):
        self.grid[:, :] = 0

        for p in pythons:
            x, y = p.x, p.y
            self.grid[x, y] += 1

    def get_heatmap(self):
        return self.grid