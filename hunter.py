import random

from config import (
    GRID_SIZE,
    BASE_DETECTION_PROBABILITY,
    REMOVAL_SUCCESS_RATE
)

class HunterTeam:

    def __init__(self):

        self.x = random.randint(0, GRID_SIZE - 1)
        self.y = random.randint(0, GRID_SIZE - 1)

        self.removals = 0

    def move(self):

        self.x += random.randint(-3, 3)
        self.y += random.randint(-3, 3)

        self.x = max(0, min(GRID_SIZE - 1, self.x))
        self.y = max(0, min(GRID_SIZE - 1, self.y))

    def detect_and_remove(self, pythons, env):

        local_density = env.get_local_density(self.x, self.y)

        vegetation_factor = (
            1 - env.vegetation[self.x, self.y]
        )

        detection_probability = (
            BASE_DETECTION_PROBABILITY
            + (local_density * 0.03)
        ) * vegetation_factor

        for p in pythons:

            if p.alive and p.x == self.x and p.y == self.y:

                if random.random() < detection_probability:

                    if random.random() < REMOVAL_SUCCESS_RATE:

                        p.alive = False
                        self.removals += 1