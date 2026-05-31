from simulation import Simulation

sim = Simulation()

step_history = []
population_history = []
removal_history = []
hotspot_history = []


def record_state():
    step_history.append(sim.step_count)

    population_history.append(
        sim.get_population()
    )

    removal_history.append(
        sim.get_total_removals()
    )

    hotspot_history.append(
        len(sim.hotspots)
    )


def reset_simulation():
    global sim

    sim = Simulation()

    step_history.clear()
    population_history.clear()
    removal_history.clear()
    hotspot_history.clear()

    record_state()


record_state()