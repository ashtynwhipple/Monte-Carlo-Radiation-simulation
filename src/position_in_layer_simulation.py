# type: ignore
import numpy as np
from materials import layers
# type: ignore

def simulate_proton_position(layers):
    """
    Returns (layer_name, z_position) of where proton stops.
    If proton transmits, returns ('transmitted', total_depth)
    """
    z_start = 0
    for layer in layers:
        mu = layer["mu"]
        thickness = layer["thickness"]
        # sample free path in this layer
        distance = -np.log(np.random.rand()) / mu
        if distance < thickness:
            # stops inside this layer
            return layer["name"], z_start + distance
        else:
            # proton passes this layer
            z_start += thickness
    # proton made it through all layers
    return "transmitted", z_start

def simulate_all_positions(N=10000):
    positions = []
    for _ in range(N):
        layer_name, z = simulate_proton_position(layers)
        # assign random x, y inside body width/depth
        x = np.random.uniform(-0.5, 0.5)
        y = np.random.uniform(-0.5, 0.5)
        positions.append([x, y, z, layer_name])
    return np.array(positions, dtype=object)  # keep layer_name
