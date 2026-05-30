from python_agent import PythonAgent
from environment import Environment
from hunter import HunterTeam
from optimizer import Optimizer

from config import (
    INITIAL_PYTHONS,
    NUM_HUNTERS,
    REDEPLOYMENT_INTERVAL
)

class Simulation:

    def __init__(self):

        self.env = Environment()

        self.optimizer = Optimizer()

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

        self.hotspots = []

    def step(self):

        # update density
        self.env.update_density(self.pythons)

        # analyze hotspots
        self.hotspots = self.optimizer.find_hotspots(
            self.env
        )

        # redeploy hunters periodically
        if (
            self.step_count %
            REDEPLOYMENT_INTERVAL == 0
        ):

            self.optimizer.assign_hunters(
                self.hunters,
                self.hotspots
            )

        # hunter operations
        for hunter in self.hunters:

            hunter.move()

            previous_removals = hunter.removals

            hunter.detect_and_remove(
                self.pythons,
                self.env
            )

            self.total_removals += (
                hunter.removals -
                previous_removals
            )

        # python dynamics
        new_pythons = []

        for p in self.pythons:

            if not p.alive:
                continue

            p.move(self.env)

            p.maybe_die()

            if p.alive:

                baby = p.maybe_reproduce(
                    self.env
                )

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