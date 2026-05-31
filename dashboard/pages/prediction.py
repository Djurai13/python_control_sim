import streamlit as st

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from simulation_manager import (
    get_prediction_dataframe
)

st.title("Prediction Engine")

df = get_prediction_dataframe()

if len(df) < 5:

    st.warning(
        "Run the simulation from the Operations page "
        "to generate prediction data."
    )

else:

    x = np.array(
        df["Step"]
    )

    y = np.array(
        df["Population"]
    )

    slope, intercept = np.polyfit(
        x,
        y,
        1
    )

    current_step = int(
        df["Step"].iloc[-1]
    )

    current_population = int(
        df["Population"].iloc[-1]
    )

    future_step = current_step + 50

    predicted_population = int(
        slope * future_step + intercept
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current Population",
            current_population
        )

    with col2:

        st.metric(
            "Predicted Population (+50 Steps)",
            predicted_population
        )

    future_steps = list(
        range(
            current_step,
            future_step + 1
        )
    )

    forecast_values = [
        slope * s + intercept
        for s in future_steps
    ]

    forecast_df = pd.DataFrame(
        {
            "Step": future_steps,
            "Forecast Population":
            forecast_values
        }
    )

    st.subheader(
        "Population Forecast"
    )

    fig = px.line(
        forecast_df,
        x="Step",
        y="Forecast Population",
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Forecast Summary"
    )

    st.write(
        {
            "Current Step":
                current_step,
            "Forecast Horizon":
                50,
            "Current Population":
                current_population,
            "Predicted Population":
                predicted_population
        }
    )