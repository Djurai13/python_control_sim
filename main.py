from simulation import Simulation
from visualization import plot_maps

import matplotlib.pyplot as plt

def run():

    sim = Simulation()

    plt.figure(figsize=(12, 6))

    for step in range(300):

        sim.step()

        print(
            f"Step {step} | "
            f"Population: {sim.get_population()}"
        )

        plot_maps(
            sim.env,
            step,
            sim.get_population()
        )

    plt.show()

if __name__ == "__main__":
    run()