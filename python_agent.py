import random
from config import (
    GRID_SIZE,
    MOVE_RANGE,
    BASE_REPRODUCTION_RATE,
    DEATH_RATE,
    MAX_LOCAL_DENSITY
)

class PythonAgent:

    def __init__(self):

        self.x = random.randint(0, GRID_SIZE - 1)
        self.y = random.randint(0, GRID_SIZE - 1)
        self.alive = True

    def move(self, env):

        best_x = self.x
        best_y = self.y

        best_score = env.get_suitability(self.x, self.y)

        # examine nearby cells
        for dx in range(-MOVE_RANGE, MOVE_RANGE + 1):
            for dy in range(-MOVE_RANGE, MOVE_RANGE + 1):

                nx = self.x + dx
                ny = self.y + dy

                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:

                    score = env.get_suitability(nx, ny)

                    if score > best_score:
                        best_score = score
                        best_x = nx
                        best_y = ny

        self.x = best_x
        self.y = best_y

    def maybe_reproduce(self, env):

        local_density = env.get_local_density(self.x, self.y)

        density_factor = max(
            0,
            1 - (local_density / MAX_LOCAL_DENSITY)
        )

        reproduction_probability = (
            BASE_REPRODUCTION_RATE * density_factor
        )

        if random.random() < reproduction_probability:
            return PythonAgent()

        return None

    def maybe_die(self):

        if random.random() < DEATH_RATE:
            self.alive = False