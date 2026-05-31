from simulation import Simulation
from visualization import plot_maps
from gis import GISMap

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

    print("\nGenerating GIS map...")

    gis_map = GISMap()

    gis_map.add_hotspots(
        sim.hotspots
    )

    gis_map.add_hunters(
        sim.hunters
    )

    gis_map.save()

    print(
        "GIS map saved to maps/everglades_map.html"
    )

    plt.show()


if __name__ == "__main__":
    run()