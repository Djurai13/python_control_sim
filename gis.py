import folium

from config import (
    GRID_SIZE,
    MIN_LAT,
    MAX_LAT,
    MIN_LON,
    MAX_LON
)


def grid_to_geo(x, y):
    """
    Convert simulation coordinates
    into geographic coordinates.
    """

    lat = MIN_LAT + (
        x / GRID_SIZE
    ) * (
        MAX_LAT - MIN_LAT
    )

    lon = MIN_LON + (
        y / GRID_SIZE
    ) * (
        MAX_LON - MIN_LON
    )

    return lat, lon


class GISMap:

    def __init__(self):

        self.map = folium.Map(
            location=[25.45, -80.70],
            zoom_start=10,
            tiles="OpenStreetMap"
        )

    def add_hotspots(self, hotspots):

        for hotspot in hotspots[:20]:

            _, x, y = hotspot

            lat, lon = grid_to_geo(x, y)

            folium.CircleMarker(
                location=[lat, lon],
                radius=8,
                color="red",
                fill=True,
                fill_opacity=0.8,
                popup=f"Hotspot ({x}, {y})"
            ).add_to(self.map)

    def add_hunters(self, hunters):

        for hunter in hunters:

            lat, lon = grid_to_geo(
                hunter.x,
                hunter.y
            )

            folium.Marker(
                location=[lat, lon],
                popup="Hunter Team",
                icon=folium.Icon(
                    color="blue"
                )
            ).add_to(self.map)

    def save(self):

        self.map.save(
            "maps/everglades_map.html"
        )