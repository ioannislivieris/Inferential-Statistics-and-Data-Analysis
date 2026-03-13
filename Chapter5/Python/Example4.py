# Chapter 5 - Other Discrete Distributions
# Example 4: Hypergeometric vs Binomial — Sampling from Finite Population
#   N=100, K=30, n=20

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom, binom

# Parameters
N = 100    # population size
K = 30     # successes in population
n = 20     # sample size
p = K / N  # probability for binomial approximation

# Values
x = np.arange(0, n + 1)

# Calculate probabilities
hypergeom_probs = hypergeom.pmf(x, N, K, n)
binom_probs     = binom.pmf(x, n, p)

# Plot comparison
width = 0.35
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - width/2, hypergeom_probs, width,
       label='Hypergeometric', color='steelblue', edgecolor='black')
ax.bar(x + width/2, binom_probs, width,
       label='Binomial', color='coral', edgecolor='black')

ax.set_xlabel('Number of Successes', fontsize=12)
ax.set_ylabel('Probability', fontsize=12)
ax.set_title('Hypergeometric vs Binomial Distribution', fontsize=14)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Maximum absolute difference
max_diff = np.max(np.abs(hypergeom_probs - binom_probs))
print(f"Maximum difference: {max_diff:.6f}")
