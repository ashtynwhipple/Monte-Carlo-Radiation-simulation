import numpy as np
from materials import layers

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
