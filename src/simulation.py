# type: ignore
import numpy as np # type: ignore
from materials import layers

def simulate_particle(mu, slab_thickness):
    """
    Parameters:
    mu - probability distribution
    slab_thickness - thickness of layer that protons are going through

    Returns:
    boolean: true if disance > slab thickness
    i.e. true if the proton made it through the layer
    """
    distance = -np.log(np.random.rand()) / mu # this is sampling from and exponential probability distribution

    return distance > slab_thickness # returns true if the proton made it through

def run_simulation(N, mu, slab_thickness):
    """
    Parameters:
    N - number of protons wishing to simulate
    mu - probability distribution
    slab_thickness - thickness of layer that protons are going through

    Returns:
    count_transmitted: number of protons that went through the material
    """
    count_transmitted = 0
    for _ in range(N):
        if simulate_particle(mu, slab_thickness):
            count_transmitted += 1
    return count_transmitted

def simulate_particle_through_layers(layers):
    """
    Simulates ONE particle traveling through multiple layers.
    Returns the name of the layer where the particle interacts (stops).
    If the particle passes all layers, returns None.
    """

    for layer in layers:
        mu = layer["mu"]
        thickness = layer["thickness"]

        # sample a distance the particle travels before interacting
        distance = -np.log(np.random.rand()) / mu

        if distance < thickness:
            # interaction happens inside this layer
            return layer["name"]

        # otherwise particle passes this layer completely
        # and continues into the next layer with leftover distance
        distance -= thickness
        # but because we are resampling every layer anyway,
        # we do not need to track leftover distance in this simple model

    # particle passed all layers without interacting
    return None

def multiple_layers(N=10000):
    """
    Instead of checking just one slab, simulate the particle moving through all layers in order.

    Start position = 0
    Sample a free path in the current layer
    Move particle forward
    If distance is longer than current layer thickness, subtract layer thickness and go to next layer
    If particle stops inside a layer, record energy deposited in that layer

    Parameters:
    N - number of protons wishing to simulate

    Returns:
    layer_energy - dictionary of each layer and the energy and the amount of protons transmitted {layer_name: count}.

    Simulate N particles and count where they deposit energy (interact).
    """
    # initialize count dictionary
    layer_energy = {layer["name"]: 0 for layer in layers}
    layer_energy["transmitted"] = 0   # particles that escape all layers

    for _ in range(N):
        result = simulate_particle_through_layers(layers)

        if result is None:
            layer_energy["transmitted"] += 1
        else:
            layer_energy[result] += 1

    return layer_energy
