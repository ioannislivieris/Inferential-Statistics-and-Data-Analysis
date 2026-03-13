# Chapter 4 - Poisson Distribution
# Example 5: Comparing Poisson(λ) for λ = 2, 5, 10

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameters
lambdas = [2, 5, 10]

# Individual plots + comparison
plt.figure(figsize=(12, 8))

for i, lam in enumerate(lambdas, 1):
    plt.subplot(2, 2, i)
    x   = np.arange(0, lam * 3)
    pmf = poisson.pmf(x, lam)
    plt.bar(x, pmf, color=f'C{i-1}', alpha=0.7, edgecolor='black')
    plt.xlabel('k')
    plt.ylabel('P(X = k)')
    plt.title(f'Poisson({lam}): Mean={lam}, SD={np.sqrt(lam):.2f}')
    plt.grid(axis='y', alpha=0.3)

# Overlay comparison
plt.subplot(2, 2, 4)
x_max = max(lambdas) * 3
for i, lam in enumerate(lambdas):
    x   = np.arange(0, x_max)
    pmf = poisson.pmf(x, lam)
    plt.plot(x, pmf, 'o-', label=f'lambda = {lam}', linewidth=2)

plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.title('Distribution Comparison')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
