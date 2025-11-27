# type: ignore
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import src.simulation as sim  # type: ignore


from matplotlib import pyplot as plt

results = sim.multiple_layers()

layers = list(results.keys())
counts = list(results.values())

plt.figure(figsize=(8, 5))
plt.bar(layers, counts)
plt.xlabel("Layer")
plt.ylabel("Photons")
plt.title("Photon Interactions by Layer")
plt.xticks(rotation=45)
plt.tight_layout()

# save *before* showing
plt.savefig("histogram_layers_protons_absorbed.png")

plt.show()
