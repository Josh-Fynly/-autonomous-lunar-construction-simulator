import numpy as np


class Terrain:
    def __init__(self, width=100, scale=1.0):
        self.width = width
        self.scale = scale
        self.heights = self.generate_heightmap()

    def generate_heightmap(self):
        x = np.linspace(0, 10, self.width)

        # Smooth structured terrain (not random)
        heights = (
            2 * np.sin(x) +
            1.5 * np.sin(0.5 * x) +
            0.5 * np.sin(2 * x)
        )

        # Normalize so minimum is 0
        heights = heights - np.min(heights)

        return heights * self.scale

    def get_height(self, x_pos):
        index = int(np.clip(x_pos, 0, self.width - 1))
        return self.heights[index]
