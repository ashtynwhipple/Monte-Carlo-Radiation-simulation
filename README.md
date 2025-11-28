# Monte-Carlo-Radiation-simulation
A small educational project demonstrating the core ideas behind radiation transport in medical physics. Photons are simulated as they pass through layered tissue, undergoing scattering, absorption, and energy loss based on probabilistic rules. The goal is to visualize how particles interact with different materials and how energy deposition (dose) builds up with depth. This kind of simulation reflects the core ideas used in medical physics and radiation therapy.

The model uses a simple body composed of four layers (skin, fat, muscle, bone). Each proton travels through the layers, where its interaction point is sampled from an exponential probability distribution. The project includes scripts that generate histograms, depth–dose curves, and 2D/3D visualizations of stopping points.

This project is intended for learning and demonstration purposes only.

# Physics Overview

Exponential Free-Path Sampling

The distance a proton travels before interacting is sampled using:

d = -ln(R) / mu

where
R = random number in (0,1)
mu = linear attenuation coefficient of the current layer

If this distance is shorter than the layer thickness, the proton stops in that layer. Otherwise, it passes through to the next layer.

# Layer-by-Layer Transport

Particles start at the surface and move through each layer in order. For each layer:
Sample a free path distance.

If the distance is less than the layer's thickness, the proton interacts there. If not, it moves to the next layer. If it passes all layers, it is counted as transmitted.

# Depth–Dose Curve

By collecting all stopping depths, we build a depth–dose curve showing where energy is deposited inside the tissue. This curve is a simplified version of what is used in radiation therapy planning.

# Project Structure
```
Monte-Carlo-Radiation-simulation/
│
├── src/
│   materials.py
│   layer_only_simulation.py
│   position_in_layer_simulation.py
│   simulation.py
│
├── plotting/
│   plot_hist.py
│   plot_depth_dose.py
│   plot_2d_view.py
│   plot_3d_tracks.py
│
README.md
requirements.txt
```

# Key Components
## materials.py

Defines all tissue layers:

```
layers = [
    {'name': 'skin',   'thickness': 0.2, 'mu': 0.2},
    {'name': 'fat',    'thickness': 1.0, 'mu': 0.15},
    {'name': 'muscle', 'thickness': 3.0, 'mu': 0.18},
    {'name': 'bone',   'thickness': 0.5, 'mu': 0.5},
]
```

## layer_only_simulation.py

Simulates where each proton stops and produces a dictionary like:

```
{
  'skin': 388,
  'fat': 1327,
  'muscle': 3480,
  'bone': 1110,
  'transmitted': 3695
}
```

## position_in_layer_simulation.py

Simulates full 3D stopping positions for visualization.

## Plotting Scripts

plot_hist.py: Interaction counts per layer

plot_depth_dose.py: Depth–dose curve with layer boundaries

plot_2d_view.py: 2D scatter of stopping points

plot_3d_tracks.py: 3D block model of layers with proton stops

# Running the Code

## Run simulations:

python src/layer_only_simulation.py

## Generate visualizations:
```
python plotting/plot_hist.py
python plotting/plot_depth_dose.py
python plotting/plot_2d_view.py
python plotting/plot_3d_tracks.py
```

### If Python cannot find the src folder, the plotting scripts include:
```
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
```


# Educational Goals

This project illustrates:
Monte Carlo sampling
Exponential attenuation
Proton stopping distributions
How dose varies with depth
How tissue composition affects interaction rates
Basic scientific visualization in Python

This makes it useful for coursework or independent study in:
Medical Physics
Nuclear Engineering
Radiation Therapy
Computational Physics
Applied Mathematics

# Future Improvements
Possible extensions:
Proton energy loss using Bethe–Bloch
Scattering angle simulation
Realistic beam width and divergence
Voxel-based body instead of layers
Bragg peak modeling
GPU acceleration

