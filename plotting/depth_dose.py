# type: ignore
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import position_in_layer_simulation as sim
from materials import layers
# type: ignore

n = 10000  # number of protons

# Simulate proton positions
proton_positions = sim.simulate_all_positions(n)

# Extract depth (z) positions
z_positions = proton_positions[:, 2].astype(float)

# Make histogram for depth-dose curve
num_bins = 200
hist, bin_edges = np.histogram(z_positions, bins=num_bins, range=(0, sum(layer["thickness"] for layer in layers)))

# Exclude last bin (transmitted particles)
hist = hist[:-1]
bin_edges = bin_edges[:-1]

# Normalize remaining bins to get relative dose
dose = hist / hist.sum()
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Plot
plt.figure(figsize=(12, 8))
plt.plot(bin_centers, dose, color='crimson', linewidth=2, label='Relative Dose')

plt.xlabel("Depth (cm)", fontsize=12)
plt.ylabel("Relative Dose", fontsize=12)
plt.title("Proton Depth-Dose Curve (Excluding Transmitted)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)

# --- Add layer boundaries ---
z = 0
for layer in layers:
    thickness = layer["thickness"]
    z_next = z + thickness
    mid = z + thickness / 2

    # Vertical boundary line
    plt.axvline(z, color='black', linewidth=1, alpha=0.4)

    # Label in the middle of the layer
    plt.text(mid, max(dose)*0.9, layer["name"],
             ha='center', va='center', fontsize=10)

    z = z_next

# Last boundary at end of all layers
plt.axvline(z, color='black', linewidth=1, alpha=0.4)

plt.tight_layout()
plt.legend()

plt.savefig("Depth_dose.png", dpi=300)

plt.show()
