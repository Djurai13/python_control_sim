import matplotlib.pyplot as plt

def plot_maps(env, step, population):

    plt.clf()

    plt.suptitle(
        f"Step {step} | Population: {population}"
    )

    # python density
    plt.subplot(1, 2, 1)

    plt.title("Python Density")

    plt.imshow(
        env.get_heatmap(),
        cmap="hot",
        interpolation="nearest"
    )

    plt.colorbar()

    # habitat suitability
    plt.subplot(1, 2, 2)

    plt.title("Habitat Suitability")

    plt.imshow(
        env.get_suitability_map(),
        cmap="Greens",
        interpolation="nearest"
    )

    plt.colorbar()

    plt.pause(0.05)