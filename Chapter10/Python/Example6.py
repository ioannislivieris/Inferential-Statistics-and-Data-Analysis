# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 6: Ρυθμός Σύγκλισης ΚΟΘ — Shapiro-Wilk τεστ
#   Σύγκριση 4 κατανομών × 5 μεγέθη δείγματος

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro

np.random.seed(42)
n_simulations = 500
sample_sizes  = [5, 10, 30, 50, 100]

# Define distributions
distributions = {
    'Uniform(0,10)':      lambda n: np.random.uniform(0, 10, n),
    'Exponential(l=0.5)': lambda n: np.random.exponential(2, n),
    'Chi-square(df=3)':   lambda n: np.random.chisquare(3, n),
    'Normal(50,10)':      lambda n: np.random.normal(50, 10, n)
}

# For each distribution and sample size, compute
# proportion of Shapiro-Wilk tests that accept normality (p > 0.05)
results = pd.DataFrame(index=list(distributions.keys()),
                       columns=[f'n={n}' for n in sample_sizes],
                       dtype=float)

for dist_name, dist_func in distributions.items():
    for n in sample_sizes:
        p_values = []
        for _ in range(n_simulations):
            means = [np.mean(dist_func(n)) for _ in range(30)]
            _, p  = shapiro(means)
            p_values.append(p)
        # Proportion where normality is NOT rejected at alpha=0.05
        results.loc[dist_name, f'n={n}'] = np.mean(
            np.array(p_values) > 0.05)

print("Proportion of Shapiro-Wilk tests accepting normality (p > 0.05):\n")
print(results.round(3))

# Visualization: heatmap
fig, ax = plt.subplots(figsize=(10, 5))
data = results.values.astype(float)
im   = ax.imshow(data, cmap='RdYlGn', vmin=0, vmax=1, aspect='auto')

ax.set_xticks(range(len(sample_sizes)))
ax.set_xticklabels([f'n={n}' for n in sample_sizes], fontsize=11)
ax.set_yticks(range(len(distributions)))
ax.set_yticklabels(list(distributions.keys()), fontsize=11)
ax.set_title('CLT Convergence: Proportion Accepting Normality\n'
             '(Shapiro-Wilk, p > 0.05)', fontsize=13)

# Add text annotations
for i in range(len(distributions)):
    for j in range(len(sample_sizes)):
        ax.text(j, i, f'{data[i, j]:.2f}',
                ha='center', va='center',
                fontsize=11, fontweight='bold',
                color='black')

plt.colorbar(im, ax=ax, label='Proportion accepting normality')
plt.tight_layout()
plt.show()
