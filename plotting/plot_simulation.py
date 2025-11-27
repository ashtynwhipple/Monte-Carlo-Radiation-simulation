# type: ignore
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import position_in_layer_simulation as sim
from materials import layers  # now 'layers' is the list
# type: ignore

# Assign colors to layers
colors = ["peachpuff", "lightyellow", "lightcoral", "lightgray"]
for layer, color in zip(layers, colors):
    layer["color"] = color

n = 10000
num_protons = int(n / 10)  # adjust if needed

# Simulate proton positions
proton_positions= sim.simulate_all_positions(num_protons)

# 2D Plot: X vs Depth (Z)
fig, ax = plt.subplots(figsize=(6, 8))

# Draw layers as filled rectangles
z_start = 0
for layer in layers:
    thickness = layer["thickness"]
    color = layer["color"]
    ax.fill_between([-0.5, 0.5], z_start, z_start + thickness,
                    color=color, alpha=0.6)
    # Label layer in the middle
    ax.text(0.55, z_start + thickness / 2, layer["name"],
            va='center', ha='left', fontsize=10)
    z_start += thickness

# Scatter proton positions (ignore Y)
ax.scatter(proton_positions[:,0], proton_positions[:,2],
           color='red', s=1)

ax.set_xlabel('X')
ax.set_ylabel('Depth')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0, z_start + 0.5)
ax.set_title('Proton Position Distribution Through Body Layers (2D)')

plt.savefig("Proton_Position_Distribution_Through_Body_Layers.png")

plt.show()
