import numpy as np
import matplotlib.pyplot as plt

from physics.lunar_physics import LunarPhysicsEngine
from physics.terrain import Terrain

# Initialize terrain and physics engine
terrain = Terrain(width=200, scale=2.0)
engine = LunarPhysicsEngine(terrain=terrain, dt=0.05)

# Initial conditions
position = np.array([0.0, 10.0])
velocity = np.array([2.0, 0.0])

positions = []

# Simulation loop
for _ in range(300):
    position, velocity = engine.step(position, velocity)
    positions.append(position.copy())

positions = np.array(positions)

# Plot terrain
terrain_x = np.arange(len(terrain.heights))
terrain_y = terrain.heights

plt.plot(terrain_x, terrain_y, label="Terrain")

# Plot trajectory
plt.plot(positions[:, 0], positions[:, 1], label="Trajectory")

plt.title("Slope-Aware Lunar Physics Simulation")
plt.xlabel("X position")
plt.ylabel("Y position")
plt.legend()
plt.show()
