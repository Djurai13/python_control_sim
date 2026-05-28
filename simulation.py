from python_agent import PythonAgent
from environment import Environment
from config import INITIAL_PYTHONS

class Simulation:

    def __init__(self):

        self.env = Environment()

        self.pythons = [
            PythonAgent()
            for _ in range(INITIAL_PYTHONS)
        ]

        self.step_count = 0

    def step(self):

        self.env.update_density(self.pythons)

        new_pythons = []

        for p in self.pythons:

            p.move(self.env)

            p.maybe_die()

            if p.alive:

                baby = p.maybe_reproduce(self.env)

                if baby:
                    new_pythons.append(baby)

        self.pythons = [
            p for p in self.pythons
            if p.alive
        ]

        self.pythons.extend(new_pythons)

        self.step_count += 1

    def get_population(self):
        return len(self.pythons)