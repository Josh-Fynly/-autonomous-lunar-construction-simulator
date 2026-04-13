import numpy as np

LUNAR_GRAVITY = 1.62


class LunarPhysicsEngine:
    def __init__(self, terrain, dt=0.1):
        self.dt = dt
        self.terrain = terrain

    def get_slope(self, x, dx=1.0):
        """
        Approximate terrain slope using finite difference.
        """
        h1 = self.terrain.get_height(x - dx)
        h2 = self.terrain.get_height(x + dx)

        return (h2 - h1) / (2 * dx)

    def step(self, position, velocity):
        """
        Physics step with slope-aware motion.
        """

        x, y = position

        # Gravity
        gravity = np.array([0, -LUNAR_GRAVITY])

        # Update velocity (gravity)
        velocity = velocity + gravity * self.dt

        # Horizontal damping (minimal surface resistance)
        velocity[0] *= 0.995

        # Terrain height
        ground_height = self.terrain.get_height(x)

        # Slope at position
        slope = self.get_slope(x)

        # If on ground or below ground
        if y <= ground_height:

            # Project gravity along slope (simplified physics)
            slope_force = slope * LUNAR_GRAVITY

            velocity[0] += slope_force * self.dt

            # Energy loss on contact
            velocity[1] *= -0.15

            # Strong ground friction (prevents infinite sliding)
            velocity[0] *= 0.90

            # Lock to surface
            y = ground_height

        else:
            # In air
            y = y + velocity[1] * self.dt

        x = x + velocity[0] * self.dt

        return np.array([x, y]), velocity
