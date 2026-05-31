import streamlit as st

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

st.title("GIS Intelligence")

map_file = ROOT / "maps" / "everglades_map.html"

if map_file.exists():

    with open(
        map_file,
        "r",
        encoding="utf-8"
    ) as f:

        map_html = f.read()

    st.components.v1.html(
        map_html,
        height=700,
        scrolling=True
    )

else:

    st.error(
        f"Map not found: {map_file}"
    )