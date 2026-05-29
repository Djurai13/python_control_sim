from simulation import Simulation
from visualization import plot_maps

import matplotlib.pyplot as plt

def run():

    sim = Simulation()

    plt.figure(figsize=(14, 6))

    for step in range(300):

        sim.step()

        print(
            f"Step {step} | "
            f"Population: {sim.get_population()} | "
            f"Total Removals: {sim.get_total_removals()}"
        )

        plot_maps(sim, step)

    plt.show()

if __name__ == "__main__":
    run()