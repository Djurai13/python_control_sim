from python_agent import PythonAgent
from config import INITIAL_PYTHONS

class Simulation:
    def __init__(self):
        self.pythons = [PythonAgent() for _ in range(INITIAL_PYTHONS)]
        self.step_count = 0

    def step(self):
        new_pythons = []

        for p in self.pythons:
            p.move()
            p.maybe_die()

            if p.alive:
                baby = p.maybe_reproduce()
                if baby:
                    new_pythons.append(baby)

        # remove dead
        self.pythons = [p for p in self.pythons if p.alive]

        # add newborns
        self.pythons.extend(new_pythons)

        self.step_count += 1

    def get_population(self):
        return len(self.pythons)