import numpy as np

# Lunar gravity (m/s^2)
LUNAR_GRAVITY = 1.62


class LunarPhysicsEngine:
    def __init__(self, terrain, dt=0.1):
        self.dt = dt
        self.terrain = terrain  # terrain dependency

    def step(self, position, velocity):
        """
        Advance physics by one time step.

        position: np.array([x, y])
        velocity: np.array([vx, vy])

        Returns updated (position, velocity)
        """

        # Gravity acts downward in y-direction
        gravity = np.array([0, -LUNAR_GRAVITY])

        # Update velocity
        velocity = velocity + gravity * self.dt

        # Simple horizontal damping (simulated friction)
        velocity[0] *= 0.99

        # Update position
        position = position + velocity * self.dt

        # Terrain collision
        ground_height = self.terrain.get_height(position[0])

        if position[1] < ground_height:
            position[1] = ground_height
            velocity[1] *= -0.2  # small bounce with energy loss

        return position, velocity
