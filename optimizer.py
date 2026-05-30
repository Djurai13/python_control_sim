from config import (
    GRID_SIZE,
    HOTSPOT_THRESHOLD
)

class Optimizer:

    def __init__(self):
        pass

    def find_hotspots(self, env):

        hotspots = []

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):

                density = env.grid[x, y]

                if density >= HOTSPOT_THRESHOLD:

                    suitability = env.get_suitability(x, y)

                    score = density * suitability

                    hotspots.append(
                        (score, x, y)
                    )

        hotspots.sort(reverse=True)

        return hotspots

    def assign_hunters(
        self,
        hunters,
        hotspots
    ):

        if not hotspots:
            return

        for i, hunter in enumerate(hunters):

            hotspot_index = i % len(hotspots)

            _, target_x, target_y = hotspots[hotspot_index]

            hunter.target_x = target_x
            hunter.target_y = target_y