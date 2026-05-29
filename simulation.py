from python_agent import PythonAgent
from environment import Environment
from hunter import HunterTeam

from config import (
    INITIAL_PYTHONS,
    NUM_HUNTERS
)

class Simulation:

    def __init__(self):

        self.env = Environment()

        self.pythons = [
            PythonAgent()
            for _ in range(INITIAL_PYTHONS)
        ]

        self.hunters = [
            HunterTeam()
            for _ in range(NUM_HUNTERS)
        ]

        self.step_count = 0

        self.total_removals = 0

    def step(self):

        # update spatial density
        self.env.update_density(self.pythons)

        # hunters operate
        for hunter in self.hunters:

            hunter.move()

            previous_removals = hunter.removals

            hunter.detect_and_remove(
                self.pythons,
                self.env
            )

            self.total_removals += (
                hunter.removals - previous_removals
            )

        # python population dynamics
        new_pythons = []

        for p in self.pythons:

            if not p.alive:
                continue

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

    def get_total_removals(self):
        return self.total_removals