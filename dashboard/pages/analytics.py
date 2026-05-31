import streamlit as st

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from simulation_manager import (
    step_history,
    population_history,
    removal_history,
    hotspot_history
)

st.title("Analytics")

if len(step_history) <= 1:

    st.warning(
        "No analytics data available yet. "
        "Run the simulation from the Operations page."
    )

else:

    df = pd.DataFrame(
        {
            "Step": step_history,
            "Population": population_history,
            "Removals": removal_history,
            "Hotspots": hotspot_history
        }
    )

    st.subheader("Population Trend")

    fig_population = px.line(
        df,
        x="Step",
        y="Population",
        markers=True
    )

    st.plotly_chart(
        fig_population,
        use_container_width=True
    )

    st.subheader("Removal Trend")

    fig_removals = px.line(
        df,
        x="Step",
        y="Removals",
        markers=True
    )

    st.plotly_chart(
        fig_removals,
        use_container_width=True
    )

    st.subheader("Hotspot Trend")

    fig_hotspots = px.line(
        df,
        x="Step",
        y="Hotspots",
        markers=True
    )

    st.plotly_chart(
        fig_hotspots,
        use_container_width=True
    )

    st.subheader("Analytics Data")

    st.dataframe(
        df,
        use_container_width=True
    )