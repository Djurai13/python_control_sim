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
    get_prediction_dataframe,
    sim
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

    current_removals = int(
        df["Removals"].iloc[-1]
    )

    forecast_50 = int(
        slope * (current_step + 50)
        + intercept
    )

    forecast_100 = int(
        slope * (current_step + 100)
        + intercept
    )

    forecast_200 = int(
        slope * (current_step + 200)
        + intercept
    )

    if forecast_200 < 1000:
        risk_level = "LOW"
        recommended_hunters = 4

    elif forecast_200 < 3000:
        risk_level = "MEDIUM"
        recommended_hunters = 8

    else:
        risk_level = "HIGH"
        recommended_hunters = 12

    current_hunters = len(
        sim.hunters
    )

    additional_hunters = max(
        0,
        recommended_hunters -
        current_hunters
    )

    if current_population > 0:

        suppression_ratio = (
            current_removals /
            current_population
        )

    else:

        suppression_ratio = 0

    if suppression_ratio > 0.30:

        suppression_effectiveness = "HIGH"

    elif suppression_ratio > 0.10:

        suppression_effectiveness = "MODERATE"

    else:

        suppression_effectiveness = "LOW"

    st.subheader(
        "Operational Intelligence"
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Current",
            current_population
        )

    with col2:
        st.metric(
            "+50",
            forecast_50
        )

    with col3:
        st.metric(
            "+100",
            forecast_100
        )

    with col4:
        st.metric(
            "+200",
            forecast_200
        )

    with col5:
        st.metric(
            "Risk",
            risk_level
        )

    st.divider()

    col6, col7, col8, col9 = st.columns(4)

    with col6:
        st.metric(
            "Current Hunters",
            current_hunters
        )

    with col7:
        st.metric(
            "Recommended",
            recommended_hunters
        )

    with col8:
        st.metric(
            "Additional Needed",
            additional_hunters
        )

    with col9:
        st.metric(
            "Effectiveness",
            suppression_effectiveness
        )

    future_steps = list(
        range(
            current_step,
            current_step + 201
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
        "Management Recommendation"
    )

    st.write(
        {
            "Risk Level":
                risk_level,
            "Current Hunters":
                current_hunters,
            "Recommended Hunters":
                recommended_hunters,
            "Additional Hunters Required":
                additional_hunters,
            "Suppression Effectiveness":
                suppression_effectiveness
        }
    )