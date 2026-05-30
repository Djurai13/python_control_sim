import matplotlib.pyplot as plt

def plot_maps(sim, step):

    plt.clf()

    plt.suptitle(
        f"Step {step} | "
        f"Population: {sim.get_population()} | "
        f"Removals: {sim.get_total_removals()}"
    )

    # DENSITY MAP
    plt.subplot(1, 2, 1)

    plt.title("Optimized Suppression")

    plt.imshow(
        sim.env.get_heatmap(),
        cmap="hot",
        interpolation="nearest"
    )

    # plot hunters
    hunter_x = [h.y for h in sim.hunters]
    hunter_y = [h.x for h in sim.hunters]

    plt.scatter(
        hunter_x,
        hunter_y,
        c="cyan",
        marker="X",
        s=100,
        label="Hunters"
    )

    # plot hotspots
    if sim.hotspots:

        hotspot_x = [
            h[2]
            for h in sim.hotspots[:10]
        ]

        hotspot_y = [
            h[1]
            for h in sim.hotspots[:10]
        ]

        plt.scatter(
            hotspot_x,
            hotspot_y,
            c="lime",
            marker="o",
            s=50,
            label="Hotspots"
        )

    plt.legend()

    # HABITAT MAP
    plt.subplot(1, 2, 2)

    plt.title("Habitat Suitability")

    plt.imshow(
        sim.env.get_suitability_map(),
        cmap="Greens",
        interpolation="nearest"
    )

    plt.pause(0.05)