import streamlit as st

st.title("Operations Center")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Population",
        "0"
    )

with col2:
    st.metric(
        "Hotspots",
        "0"
    )

with col3:
    st.metric(
        "Hunters",
        "0"
    )

with col4:
    st.metric(
        "Removals",
        "0"
    )

st.info(
    "Live simulation integration will be added in Dashboard Sprint 2."
)