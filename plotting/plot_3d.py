# type: ignore
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import position_in_layer_simulation as sim
from materials import layers  # now 'layers' is the list
# type: ignore

colors = ["peachpuff", "lightyellow", "lightcoral", "lightgray"]

for layer, color in zip(layers, colors):
    layer["color"] = color

n = 500

body_width = 1.0  # x-axis
body_depth = 1.0  # y-axis

# Store proton positions
proton_positions = sim.simulate_all_positions(n)

# Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Draw layers as filled boxes
z_start = 0
for layer in layers:
    thickness = layer["thickness"]
    color = layer["color"]
    # Create 3D box
    xx, yy = np.meshgrid([-0.5, 0.5], [-0.5, 0.5])
    zz = np.full_like(xx, z_start)
    ax.plot_surface(xx, yy, zz, color=color, alpha=0.6)           # bottom
    ax.plot_surface(xx, yy, zz + thickness, color=color, alpha=0.6)  # top
    # vertical sides
    for xi in [-0.5, 0.5]:
        ax.plot_surface(np.full_like(yy, xi), yy, np.array([z_start, z_start+thickness]).reshape(2,1), color=color, alpha=0.6)
    for yi in [-0.5, 0.5]:
        ax.plot_surface(xx, np.full_like(xx, yi), np.array([z_start, z_start+thickness]).reshape(2,1), color=color, alpha=0.6)
    # Label in the middle
    ax.text(0.6, 0, z_start + thickness/2, layer["name"], fontsize=10)
    z_start += thickness

# Scatter proton positions
ax.scatter(proton_positions[:,0], proton_positions[:,1], proton_positions[:,2],
           color='red', s=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Depth')
ax.set_title('Proton Dots Through Body Layers (3D)')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.6, 0.6)
ax.set_zlim(0, z_start + 0.5)
plt.show()
