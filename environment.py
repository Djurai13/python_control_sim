import numpy as np
from config import GRID_SIZE

class Environment:
    def __init__(self):

        # python density layer
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE))

        # environmental layers
        self.temperature = np.random.uniform(0.4, 1.0, (GRID_SIZE, GRID_SIZE))
        self.vegetation = np.random.uniform(0.3, 1.0, (GRID_SIZE, GRID_SIZE))
        self.water = np.random.uniform(0.2, 1.0, (GRID_SIZE, GRID_SIZE))

        # habitat suitability
        self.suitability = (
            0.4 * self.temperature +
            0.4 * self.vegetation +
            0.2 * self.water
        )

    def update_density(self, pythons):

        self.grid[:, :] = 0

        for p in pythons:
            self.grid[p.x, p.y] += 1

    def get_local_density(self, x, y):
        return self.grid[x, y]

    def get_suitability(self, x, y):
        return self.suitability[x, y]

    def get_heatmap(self):
        return self.grid

    def get_suitability_map(self):
        return self.suitability