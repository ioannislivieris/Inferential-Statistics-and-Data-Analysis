# Chapter 4 - Poisson Distribution
# Example 6: Poisson Approximation to Binomial  B(100, 0.03) ≈ Poisson(3)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson
import pandas as pd

# Parameters
n   = 100
p   = 0.03
lam = n * p   # lambda = 3

# Range of values
k = np.arange(0, 16)

# Binomial probabilities
binomial_probs = binom.pmf(k, n, p)

# Poisson probabilities
poisson_probs = poisson.pmf(k, lam)

# Plot comparison
x     = np.arange(len(k))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width/2, binomial_probs, width,
       label='Binomial(100, 0.03)', color='skyblue', edgecolor='black')
ax.bar(x + width/2, poisson_probs, width,
       label='Poisson(3)', color='coral', edgecolor='black')

ax.set_xlabel('k', fontsize=12)
ax.set_ylabel('Probability', fontsize=12)
ax.set_title('Binomial(100, 0.03) vs Poisson(3)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(k)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Maximum absolute difference
max_diff = np.max(np.abs(binomial_probs - poisson_probs))
print(f"Maximum difference: {max_diff:.6f}")

# Comparison table
comparison = pd.DataFrame({
    'k':          k,
    'Binomial':   binomial_probs,
    'Poisson':    poisson_probs,
    'Difference': np.abs(binomial_probs - poisson_probs)
})
print(comparison.head(10).to_string(index=False))
