import streamlit as st

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from simulation_manager import sim, reset_simulation

st.title("Operations Center")

col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    if st.button("Run 1 Step"):
        sim.step()

with col_b:
    if st.button("Run 10 Steps"):
        for _ in range(10):
            sim.step()

with col_c:
    if st.button("Run 100 Steps"):
        for _ in range(100):
            sim.step()

with col_d:
    if st.button("Reset Simulation"):
        reset_simulation()
        st.rerun()

population = sim.get_population()
removals = sim.get_total_removals()
hotspots = len(sim.hotspots)
hunters = len(sim.hunters)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Population", population)

with col2:
    st.metric("Hotspots", hotspots)

with col3:
    st.metric("Hunters", hunters)

with col4:
    st.metric("Removals", removals)

st.divider()

st.subheader("Simulation Status")

st.write(
    {
        "Step": sim.step_count,
        "Population": population,
        "Hotspots": hotspots,
        "Hunters": hunters,
        "Removals": removals
    }
)

st.write("Simulation Step:", sim.step_count)

st.info("Sprint 2: Live simulation connected to dashboard")