# type: ignore
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import position_in_layer_simulation as sim
# type: ignore

# Define layers
layers = [
    {"name": "skin", "thickness": 0.2, "mu": 0.2, "color": "peachpuff"},
    {"name": "fat", "thickness": 1.0, "mu": 0.15, "color": "lightyellow"},
    {"name": "muscle", "thickness": 3.0, "mu": 0.18, "color": "lightcoral"},
    {"name": "bone", "thickness": 0.5, "mu": 0.5, "color": "lightgray"},
]

num_protons = 500
width = 1.0  # width of the body (x-axis)

# Store proton positions
proton_positions = []

# Simulate protons
for _ in range(num_protons):
    x = np.random.uniform(-0.5, 0.5)
    z = 0
    alive = True

    for layer in layers:
        if not alive:
            break
        prob_survive = np.exp(-layer["mu"] * layer["thickness"])
        if np.random.rand() > prob_survive:
            # stopped in this layer
            z += np.random.uniform(0, layer["thickness"])
            proton_positions.append([x, z])
            alive = False
        else:
            z += layer["thickness"]

    if alive:
        # survived all layers, scatter at end
        x += np.random.normal(0, 0.05)
        proton_positions.append([x, z])

proton_positions = np.array(proton_positions)

# Plot
fig, ax = plt.subplots(figsize=(4, 8))

# Draw layers as filled rectangles
z_start = 0
for layer in layers:
    ax.fill_between([-width/2, width/2], z_start, z_start + layer["thickness"],
                    color=layer["color"], alpha=0.6, label=layer["name"])
    # label layer in the middle
    ax.text(0, z_start + layer["thickness"]/2, layer["name"],
            ha='center', va='center', fontsize=10)
    z_start += layer["thickness"]

# Scatter proton positions
ax.scatter(proton_positions[:,0], proton_positions[:,1], color='red', s=5)

ax.set_xlabel('X')
ax.set_ylabel('Depth')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0, z_start + 0.5)
ax.set_title('Proton Dots Through Body Layers')
plt.show()
