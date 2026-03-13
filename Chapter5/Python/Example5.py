# Chapter 5 - Other Discrete Distributions
# Example 5: Geometric Distribution Simulation  p = 0.2  (1000 observations)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# Parameter
p               = 0.2
num_simulations = 1000

# Simulation
np.random.seed(42)
simulated_data = geom.rvs(p, size=num_simulations)

# Theoretical distribution
x               = np.arange(1, 21)
theoretical_pmf = geom.pmf(x, p)

# Plot
plt.figure(figsize=(12, 6))

plt.hist(simulated_data, bins=np.arange(0.5, 20.5, 1),
         density=True, alpha=0.6, color='blue',
         edgecolor='black', label='Simulation')

plt.plot(x, theoretical_pmf, 'ro-', linewidth=2,
         markersize=6, label='Theoretical')

plt.xlabel('Number of Trials', fontsize=12)
plt.ylabel('Frequency / Probability', fontsize=12)
plt.title(f'Simulation vs Theoretical: Geom({p})', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.xlim(0, 20)
plt.tight_layout()
plt.show()

# Statistics comparison
print(f"Simulation Mean:       {np.mean(simulated_data):.2f}")
print(f"Theoretical Mean:      {1/p:.2f}")
print(f"Simulation Std Dev:    {np.std(simulated_data, ddof=1):.2f}")
print(f"Theoretical Std Dev:   {np.sqrt((1-p)/p**2):.2f}")
