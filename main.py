from simulation import Simulation
from environment import Environment
from visualization import plot_heatmap

import matplotlib.pyplot as plt

def run():
    sim = Simulation()
    env = Environment()

    plt.figure()

    for step in range(200):
        sim.step()
        env.update_density(sim.pythons)

        plot_heatmap(env, step, sim.get_population())

    plt.show()

if __name__ == "__main__":
    run()
    print(f"Step {step} | Population: {sim.get_population()}")