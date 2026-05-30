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

        self.target_x = self.x
        self.target_y = self.y

        self.removals = 0

    def move(self):

        # move toward target

        if self.x < self.target_x:
            self.x += 1

        elif self.x > self.target_x:
            self.x -= 1

        if self.y < self.target_y:
            self.y += 1

        elif self.y > self.target_y:
            self.y -= 1

    def detect_and_remove(
        self,
        pythons,
        env
    ):

        local_density = env.get_local_density(
            self.x,
            self.y
        )

        vegetation_factor = (
            1 - env.vegetation[self.x, self.y]
        )

        detection_probability = (
            BASE_DETECTION_PROBABILITY
            + (local_density * 0.03)
        ) * vegetation_factor

        detection_probability = min(
            detection_probability,
            0.95
        )

        for p in pythons:

            if (
                p.alive and
                p.x == self.x and
                p.y == self.y
            ):

                if random.random() < detection_probability:

                    if random.random() < REMOVAL_SUCCESS_RATE:

                        p.alive = False
                        self.removals += 1