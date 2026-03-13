# Chapter 3 - Binomial Distribution
# Example 4: Simulation  B(50, 0.3) — 1000 experiments

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n               = 50
p               = 0.3
num_simulations = 1000

# Simulation
np.random.seed(42)
simulated_data = binom.rvs(n, p, size=num_simulations)

# Theoretical distribution
x               = np.arange(0, n + 1)
theoretical_pmf = binom.pmf(x, n, p)

# Plot
plt.figure(figsize=(12, 6))

plt.hist(simulated_data, bins=np.arange(-0.5, n + 1.5, 1),
         density=True, alpha=0.6, color='blue',
         edgecolor='black', label='Simulation')

plt.plot(x, theoretical_pmf, 'ro-', linewidth=2,
         markersize=6, label='Theoretical Distribution')

plt.xlabel('Number of Successes', fontsize=12)
plt.ylabel('Frequency / Probability', fontsize=12)
plt.title(f'Simulation vs Theoretical Distribution: B({n}, {p})', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Statistics comparison
print(f"Simulation Mean:       {np.mean(simulated_data):.2f}")
print(f"Theoretical Mean:      {n * p:.2f}")
print(f"Simulation Std Dev:    {np.std(simulated_data, ddof=1):.2f}")
print(f"Theoretical Std Dev:   {np.sqrt(n * p * (1 - p)):.2f}")
