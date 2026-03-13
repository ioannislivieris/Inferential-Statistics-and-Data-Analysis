# Chapter 3 - Binomial Distribution
# Example 5: Comparing B(20, p) for p = 0.2, 0.5, 0.8

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n     = 20
probs = [0.2, 0.5, 0.8]
x     = np.arange(0, n + 1)

# Individual plots + comparison
plt.figure(figsize=(12, 8))

for i, p in enumerate(probs, 1):
    plt.subplot(2, 2, i)
    pmf  = binom.pmf(x, n, p)
    mean = n * p
    sd   = np.sqrt(n * p * (1 - p))
    plt.bar(x, pmf, color=f'C{i-1}', alpha=0.7, edgecolor='black')
    plt.xlabel('k')
    plt.ylabel('P(X = k)')
    plt.title(f'B({n}, {p}): E(X)={mean:.1f}, SD={sd:.2f}')
    plt.grid(axis='y', alpha=0.3)
    plt.xticks(range(0, n + 1, 2))

# Overlay comparison
plt.subplot(2, 2, 4)
for i, p in enumerate(probs):
    pmf = binom.pmf(x, n, p)
    plt.plot(x, pmf, 'o-', label=f'p = {p}', linewidth=2)

plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.title('Distribution Comparison')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
