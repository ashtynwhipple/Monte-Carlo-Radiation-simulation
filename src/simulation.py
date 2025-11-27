import numpy as np

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
