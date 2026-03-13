# Chapter 12 - Διαστήματα Εμπιστοσύνης
# Example 9: Οπτικοποίηση Πολλαπλών Διαστημάτων Εμπιστοσύνης
#   Monte Carlo: 100 δείγματα n=30 από N(100,15), 95% CI
#   Επίδειξη ότι ~95% των διαστημάτων περιέχουν τη μ=100

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy import stats

np.random.seed(123)

# True population parameters
mu_true    = 100
sigma_true = 15
n          = 30
conf_level = 0.95
n_sim      = 100

# Critical value (known σ → z-interval)
alpha  = 1 - conf_level
z_crit = stats.norm.ppf(1 - alpha / 2)
se_pop = sigma_true / np.sqrt(n)

# Simulate n_sim confidence intervals
ci_lower    = np.zeros(n_sim)
ci_upper    = np.zeros(n_sim)
contains_mu = np.zeros(n_sim, dtype=bool)

for i in range(n_sim):
    samp           = np.random.normal(mu_true, sigma_true, n)
    xbar           = np.mean(samp)
    margin         = z_crit * se_pop
    ci_lower[i]    = xbar - margin
    ci_upper[i]    = xbar + margin
    contains_mu[i] = (ci_lower[i] <= mu_true) & (mu_true <= ci_upper[i])

coverage = np.mean(contains_mu)
print(f"True μ:             {mu_true:.1f}")
print(f"Confidence level:   {conf_level*100:.0f}%")
print(f"Number of CIs:      {n_sim}")
print(f"CIs containing μ:   {contains_mu.sum()}")
print(f"Empirical coverage: {coverage*100:.1f}%")

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

ax.axvline(mu_true, color='red', linewidth=2, linestyle='--', zorder=1)

for i in range(n_sim):
    color = 'steelblue' if contains_mu[i] else 'darkorange'
    ax.plot([ci_lower[i], ci_upper[i]], [i + 1, i + 1],
            color=color, linewidth=0.9, zorder=2)
    ax.plot((ci_lower[i] + ci_upper[i]) / 2, i + 1,
            'o', color=color, markersize=2.5, zorder=3)

ax.set_xlim(ci_lower.min() - 1, ci_upper.max() + 1)
ax.set_ylim(0, n_sim + 1)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Simulation number', fontsize=12)
ax.set_title(f'{n_sim} Confidence Intervals — {conf_level*100:.0f}% Confidence Level',
             fontsize=14, fontweight='bold')

legend_elements = [
    Line2D([0], [0], color='red',        linewidth=2, linestyle='--', label='True μ'),
    Line2D([0], [0], color='steelblue',  linewidth=2, label='Contains μ'),
    Line2D([0], [0], color='darkorange', linewidth=2, label='Misses μ'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

ax.text(ci_lower.min() - 0.5, n_sim - 4,
        f'Coverage: {coverage*100:.1f}%',
        fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.6))

ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
