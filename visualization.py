import matplotlib.pyplot as plt

def plot_heatmap(env, step, population):
    plt.clf()
    plt.title(f"Python Simulation Step {step} | Population: {population}")

    plt.imshow(env.get_heatmap(), cmap="hot", interpolation="nearest")
    plt.colorbar(label="Python Density")

    plt.pause(0.1)