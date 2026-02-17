
import numpy as np

# Lunar gravity (m/s^2)
LUNAR_GRAVITY = 1.62


class LunarPhysicsEngine:
    def __init__(self, dt=0.1):
        self.dt = dt  # time step (seconds)

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

        # Update position
        position = position + velocity * self.dt

        # Simple ground collision
        if position[1] < 0:
            position[1] = 0
            velocity[1] = 0

        return position, velocity
