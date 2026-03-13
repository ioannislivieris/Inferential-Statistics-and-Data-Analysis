# Chapter 4 - Poisson Distribution
# Example 4: Simulation  Poisson(6) — 1000 observations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameter
lam             = 6
num_simulations = 1000

# Simulation
np.random.seed(42)
simulated_data = poisson.rvs(lam, size=num_simulations)

# Theoretical distribution
x               = np.arange(0, 21)
theoretical_pmf = poisson.pmf(x, lam)

# Plot
plt.figure(figsize=(12, 6))

plt.hist(simulated_data, bins=np.arange(-0.5, 20.5, 1),
         density=True, alpha=0.6, color='green',
         edgecolor='black', label='Simulation')

plt.plot(x, theoretical_pmf, 'ro-', linewidth=2,
         markersize=6, label='Theoretical Distribution')

plt.xlabel('Number of Events', fontsize=12)
plt.ylabel('Frequency / Probability', fontsize=12)
plt.title(f'Simulation vs Theoretical: Poisson({lam})', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Statistics comparison
print(f"Simulation Mean:       {np.mean(simulated_data):.2f}")
print(f"Theoretical Mean:      {lam:.2f}")
print(f"Simulation Std Dev:    {np.std(simulated_data, ddof=1):.2f}")
print(f"Theoretical Std Dev:   {np.sqrt(lam):.2f}")
