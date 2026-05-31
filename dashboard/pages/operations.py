import streamlit as st

from dashboard.simulation_manager import sim

# Advance simulation one step each refresh
sim.step()

population = sim.get_population()

removals = sim.get_total_removals()

hotspots = len(sim.hotspots)

hunters = len(sim.hunters)

st.title("Operations Center")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Population",
        population
    )

with col2:
    st.metric(
        "Hotspots",
        hotspots
    )

with col3:
    st.metric(
        "Hunters",
        hunters
    )

with col4:
    st.metric(
        "Removals",
        removals
    )

st.success(
    f"Simulation Step: {sim.step_count}"
)