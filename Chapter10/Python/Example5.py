# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 5: Δειγματοληπτική Κατανομή Αναλογίας
#   p=0.3, n = 20, 50, 100, 500 — 10000 προσομοιώσεις

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

p             = 0.3  # Population proportion
sample_sizes  = [20, 50, 100, 500]

np.random.seed(42)
n_simulations = 10000

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

for idx, n in enumerate(sample_sizes):
    # Generate sample proportions
    sample_props = [np.sum(np.random.binomial(1, p, n)) / n
                    for _ in range(n_simulations)]

    # Theoretical parameters
    se = np.sqrt(p * (1 - p) / n)

    # Check conditions for normal approximation
    np_val    = n * p
    n_1_p_val = n * (1 - p)
    conditions_met = (np_val >= 10 and n_1_p_val >= 10)

    # Histogram
    axes[idx].hist(sample_props, bins=30, density=True,
                   alpha=0.6, color='blue', edgecolor='black')

    # Overlay normal curve
    x = np.linspace(min(sample_props), max(sample_props), 200)
    y = norm.pdf(x, loc=p, scale=se)
    axes[idx].plot(x, y, 'r-', linewidth=2, label='Normal approx.')

    # Add vertical line at p
    axes[idx].axvline(p, color='green', linestyle='--',
                      linewidth=2, label='Pop. proportion')

    title = (f'n = {n}\n'
             f'(Normal approx. {"valid" if conditions_met else "questionable"})')
    axes[idx].set_title(title, fontsize=11)
    axes[idx].set_xlabel('Sample Proportion', fontsize=10)
    axes[idx].set_ylabel('Density', fontsize=10)
    axes[idx].legend(fontsize=9)
    axes[idx].grid(alpha=0.3)

    # Conditions annotation
    axes[idx].text(0.95, 0.95,
                   f'np = {np_val}\nn(1-p) = {n_1_p_val}',
                   transform=axes[idx].transAxes,
                   va='top', ha='right', fontsize=9,
                   bbox=dict(boxstyle='round',
                             facecolor='wheat', alpha=0.5))

plt.suptitle('Sampling Distribution of Proportion (p=0.3)',
             fontsize=14, y=1.01)
plt.tight_layout()
plt.show()
