PyRandomLoop is a Python package designed for simulating and visualizing a random loop model on a 2d grid. 
The core of the simulation is the class `RPM`. It provides methods for initializing the grid, running the simulation, visualization, saving and loading the state of the simulation, and calculating various statistics.

## Features

- Initialize the grid with a specified number of colors, grid size, and boundary conditions.
- Run the simulation and sample observables.
- Save and load the state of the simulation to/from a file.
- Calculate and visualize various statistics about the loops formed by each color.

## Examples

### Initializing the Grid and Running the Simulation

To initiate the grid and run the simulation, you can use the following code:
```python
from PyRandomLoop import RPM

# Initialize the grid with 3 colors, a grid size of 64 by 64, and a beta value of 1.7
sim = RPM(num_colors=3, grid_size=64, beta=2.7)

# Run the simulation for 1000 steps, showing a progress bar
sim.step(10_000, progress_bar=True)

# Save the state of the simulation to a file
sim.save_data('example.json')

# Load the state of the simulation from a file later
sim.load_data('example.json')
```
### Visualizing the Grid Using the Plot Functions
To visualize the grid using the plot functions, you can use the following code:

```python
# Plot the grid for all colors
sim.plot_grid()

# Plot the overlap of all colors in the grid
sim.plot_overlap()
```

### Creating an Animation Using the Animate Method
To create an animation using the animate method first you need to sample the grid during the simulation:

```python
# sample grid state every 1000 steps
sim.step(100_000, sample_rate=1_000, observables=[sim.get_grid], progress_bar=True)

# Create an animation using the animate method
animation = sim.animate()

# Save the animation
animation.save('example.gif')
```

### Studying Observables During the Simulation
To study observables during the simulation, you can define a list or a dictionary of callable objects, which will be called every sample_rate steps:

```python
import numpy as np 

# Define custom observables using built-in methods or custom functions
def custom_obs():
    return np.exp( sim.avg_local_time() )

observables = {
    'avg_links': sim.avg_links,
    'max_links': sim.max_links,
    'avg_local_time': sim.avg_local_time,
    'custom_obs': custom_obs,
    'links_std': lambda : np.std(sim.grid, axis = (1,2,3))
}

# run the simulation
sim.step(num_steps=100_000, sample_rate=1_000, observables=observables)

# Analyze the collected data
print(sim.data)
```

### Study loops
After running the simulation, we can calculate the loops and their length for each color using the loop_builder method.

```python
import numpy as np
import matplotlib.pyplot as plt 

# Calculate the loops for each color
loops, lengths, visits = sim.loop_builder()

# Plot the histogram of loop lengths for each color
for c in range(sim.num_colors):
    plt.hist(lengths[c], log = True, align='left', label= f'Color {c}', alpha=0.7)

plt.xlabel('Loop Length')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# find 3 longest loops of color 0
sorted = np.sort(lengths[0])[-3:]

top_3 = []

for l in loops[0]:
    if len(l) in sorted:
        top_3.append(l)

#plot them
sim.plot_loop_overlap(top_3, color=0, alpha_loop=0.5)
```

### Tests and Benchmark 

To run a test that checks all the functionality and a benchmark , you can run the scripts `test.py` and `benchmark.py` in the `PyRandomLoop.tests` submodule:

```python
from PyRandomLoop.tests import test, benchmark

test.main()
benchmark.main()
```


