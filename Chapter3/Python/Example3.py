# Chapter 3 - Binomial Distribution
# Example 3: Visualization of B(20, 0.4)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 20
p = 0.4

# Values of x
x = np.arange(0, n + 1)

# Calculate probabilities
pmf = binom.pmf(x, n, p)

# Create plot
plt.figure(figsize=(10, 6))
plt.bar(x, pmf, color='steelblue', alpha=0.7, edgecolor='black')
plt.xlabel('Number of Successes (k)', fontsize=12)
plt.ylabel('Probability P(X = k)', fontsize=12)
plt.title(f'Binomial Distribution B({n}, {p})', fontsize=14)
plt.grid(axis='y', alpha=0.3)
plt.xticks(x)

# Mark mean value
mean = n * p
std  = np.sqrt(n * p * (1 - p))
plt.axvline(mean, color='red', linestyle='--', label=f'Mean = {mean}')
plt.legend()
plt.tight_layout()
plt.show()
