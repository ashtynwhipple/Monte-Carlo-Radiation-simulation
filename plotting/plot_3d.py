# type: ignore
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import layer_only_simulation as sim
from materials import layers  # now 'layers' is the list
# type: ignore

colors = ["peachpuff", "lightyellow", "lightcoral", "lightgray"]

for layer, color in zip(layers, colors):
    layer["color"] = color

n = 10000

results = sim.multiple_layers(n)

num_protons = int(n) # I want to use all of them so maybe make the plot bigger? idk... come back to this
body_width = 1.0  # x-axis
body_depth = 1.0  # y-axis

# Store proton positions
proton_positions = []

# Simulate protons
# for _ in range(num_protons):
#     x = np.random.uniform(-0.5, 0.5)
#     y = np.random.uniform(-0.5, 0.5)
#     z = 0
#     alive = True

#     for layer in layers:
#         if not alive:
#             break
#         prob_survive = np.exp(-layer["mu"] * layer["thickness"])
#         if np.random.rand() > prob_survive:
#             # stopped in this layer
#             z += np.random.uniform(0, layer["thickness"])
#             proton_positions.append([x, y, z])
#             alive = False
#         else:
#             z += layer["thickness"]

#     if alive:
#         # survived all layers, scatter slightly at exit
#         x += np.random.normal(0, 0.05)
#         y += np.random.normal(0, 0.05)
#         proton_positions.append([x, y, z])

# proton_positions = np.array(proton_positions)

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
# ax.scatter(proton_positions[:,0], proton_positions[:,1], proton_positions[:,2],
#            color='red', s=5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Depth')
ax.set_title('Proton Dots Through Body Layers (3D)')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.6, 0.6)
ax.set_zlim(0, z_start + 0.5)
plt.show()
