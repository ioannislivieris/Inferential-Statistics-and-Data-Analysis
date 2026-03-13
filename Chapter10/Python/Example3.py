# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 3: Επαλήθευση ΚΟΘ με Q-Q Plots
#   4 αρχικές κατανομές, n=30, 1000 δείγματα ανά κατανομή

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(42)
n_simulations = 1000
n             = 30  # Sample size

# Define distributions
distributions = {
    'Uniform(0,10)':      lambda: np.random.uniform(0, 10, n),
    'Exponential(l=0.5)': lambda: np.random.exponential(2, n),
    'Chi-square(df=3)':   lambda: np.random.chisquare(3, n),
    'Normal(50,10)':      lambda: np.random.normal(50, 10, n)
}

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

for idx, (dist_name, dist_func) in enumerate(distributions.items()):
    # Generate sample means
    sample_means = [np.mean(dist_func())
                    for _ in range(n_simulations)]

    # Q-Q plot
    stats.probplot(sample_means, dist="norm", plot=axes[idx])
    axes[idx].get_lines()[0].set_markerfacecolor('blue')
    axes[idx].get_lines()[0].set_markersize(4)
    axes[idx].get_lines()[1].set_color('red')
    axes[idx].get_lines()[1].set_linewidth(2)

    axes[idx].set_title(f'Q-Q Plot: {dist_name}\nn = {n}', fontsize=12)
    axes[idx].grid(alpha=0.3)

plt.suptitle('Q-Q Plots — Verification of CLT (n=30)', fontsize=14, y=1.01)
plt.tight_layout()
plt.show()
