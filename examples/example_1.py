import numpy as np
import matplotlib.pyplot as plt 
from PyRandomLoop import RPM 

sim = RPM(3, 32, 2)
sim.step(1_000_000)
# Calculate the loops for each color
loops, lengths, visits = sim.loop_builder()

# Plot the histogram of loop lengths for each color
for c in range(sim.num_colors):
    plt.hist(lengths[c], log = True, align='left', label= f'Color {c}', alpha=0.7)

plt.xlabel('Loop Length')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# find 3 longest loops
sorted = np.sort(lengths[0])[-3:]

top_3 = []

for l in loops[0]:
    if len(l) in sorted:
        top_3.append(l)

#plot them
sim.plot_loop_overlap(top_3, color=0, alpha_loop=0.5)