import random
from config import GRID_SIZE, MOVE_RANGE, REPRODUCTION_RATE, DEATH_RATE

class PythonAgent:
    def __init__(self):
        self.x = random.randint(0, GRID_SIZE - 1)
        self.y = random.randint(0, GRID_SIZE - 1)
        self.alive = True

    def move(self):
        self.x += random.randint(-MOVE_RANGE, MOVE_RANGE)
        self.y += random.randint(-MOVE_RANGE, MOVE_RANGE)

        self.x = max(0, min(GRID_SIZE - 1, self.x))
        self.y = max(0, min(GRID_SIZE - 1, self.y))

    def maybe_reproduce(self):
        import random
        if random.random() < REPRODUCTION_RATE:
            return PythonAgent()
        return None

    def maybe_die(self):
        import random
        if random.random() < DEATH_RATE:
            self.alive = False