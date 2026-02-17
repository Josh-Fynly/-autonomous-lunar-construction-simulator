import numpy as np
import matplotlib.pyplot as plt

from physics.lunar_physics import LunarPhysicsEngine

engine = LunarPhysicsEngine(dt=0.05)

position = np.array([0.0, 10.0])
velocity = np.array([2.0, 0.0])

positions = []

for _ in range(200):
    position, velocity = engine.step(position, velocity)
    positions.append(position.copy())

positions = np.array(positions)

plt.plot(positions[:, 0], positions[:, 1])
plt.title("Lunar Gravity Simulation")
plt.xlabel("X position")
plt.ylabel("Y position")
plt.show()
