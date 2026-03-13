# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 1: ΚΟΘ με Ομοιόμορφη Κατανομή U(0,10)
#   n = 5, 10, 30, 100 — 10000 προσομοιώσεις ανά μέγεθος

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)
n_simulations = 10000
sample_sizes  = [5, 10, 30, 100]

# Theoretical parameters for U(0,10)
mu    = 5
sigma = np.sqrt((10 - 0)**2 / 12)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

for idx, n in enumerate(sample_sizes):
    # Generate sample means from uniform distribution
    sample_means = [np.mean(np.random.uniform(0, 10, n))
                    for _ in range(n_simulations)]

    se = sigma / np.sqrt(n)

    # Histogram
    axes[idx].hist(sample_means, bins=50, density=True,
                   alpha=0.6, color='blue', edgecolor='black',
                   label='Simulated')

    # Overlay theoretical normal curve
    x = np.linspace(min(sample_means), max(sample_means), 200)
    y = norm.pdf(x, loc=mu, scale=se)
    axes[idx].plot(x, y, 'r-', linewidth=2, label='Theoretical N')

    # Add vertical line at population mean
    axes[idx].axvline(mu, color='green', linestyle='--',
                      linewidth=2, label='Pop. Mean')

    axes[idx].set_xlabel('Sample Mean', fontsize=11)
    axes[idx].set_ylabel('Density', fontsize=11)
    axes[idx].set_title(f'Sample Size n = {n}', fontsize=12)
    axes[idx].legend(fontsize=9)
    axes[idx].grid(alpha=0.3)

plt.suptitle('CLT Demonstration — Uniform Distribution U(0,10)',
             fontsize=14, y=1.01)
plt.tight_layout()
plt.show()
