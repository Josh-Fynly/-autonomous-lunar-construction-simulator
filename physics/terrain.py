import numpy as np


class Terrain:
    def __init__(self, width=200, scale=1.0):
        self.width = width
        self.scale = scale
        self.heights = self.generate_heightmap()

    def generate_heightmap(self):
        x = np.linspace(0, 20, self.width)

        heights = (
            2.5 * np.sin(x * 0.6) +
            1.2 * np.sin(x * 1.3) +
            0.6 * np.sin(x * 2.7)
        )

        heights = heights - np.min(heights)

        return heights * self.scale

    def get_height(self, x_pos):
        index = int(np.clip(x_pos, 0, self.width - 1))
        return self.heights[index]
