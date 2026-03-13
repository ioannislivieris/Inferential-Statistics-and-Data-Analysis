# Chapter 4 - Poisson Distribution
# Example 3: Visualization of Poisson(7)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameter
lam = 7

# Values (0 to 20 covers most of the distribution)
x = np.arange(0, 21)

# Calculate probabilities
pmf = poisson.pmf(x, lam)

# Create plot
plt.figure(figsize=(10, 6))
plt.bar(x, pmf, color='darkgreen', alpha=0.7, edgecolor='black')
plt.xlabel('Number of Events (k)', fontsize=12)
plt.ylabel('Probability P(X = k)', fontsize=12)
plt.title(f'Poisson Distribution with lambda = {lam}', fontsize=14)
plt.grid(axis='y', alpha=0.3)
plt.xticks(x)

# Mark mean value (= lambda)
plt.axvline(lam, color='red', linestyle='--',
            label=f'Mean = lambda = {lam}')
plt.legend()
plt.tight_layout()
plt.show()
