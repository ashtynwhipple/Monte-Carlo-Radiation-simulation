# type: ignore
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import layer_only_simulation as sim  # type: ignore

from matplotlib import pyplot as plt
import numpy as np

results = sim.multiple_layers()

layers = list(results.keys())
counts = np.array(list(results.values()), dtype=float)

total = counts.sum()
percent = (counts / total) * 100  # convert to %

plt.figure(figsize=(8, 5))
bars = plt.bar(layers, percent)

plt.xlabel("Layer")
plt.ylabel("Percentage of Photons (%)")
plt.title("Photon Interactions by Layer (Percentage)")
plt.xticks(rotation=45)
plt.tight_layout()

# Add labels on top of each bar
for bar, p in zip(bars, percent):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{p:.1f}%",
        ha="center",
        va="bottom"
    )

plt.savefig("histogram_layers_protons_absorbed_percent.png")
plt.show()
