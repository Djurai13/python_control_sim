import streamlit as st

st.title("Operations Center")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Population",
        "1245"
    )

with col2:
    st.metric(
        "Hotspots",
        "17"
    )

with col3:
    st.metric(
        "Hunters",
        "8"
    )

with col4:
    st.metric(
        "Removals",
        "562"
    )

st.info(
    "Live simulation integration comes next."
)