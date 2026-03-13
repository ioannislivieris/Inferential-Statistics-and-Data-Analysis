# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 4: Οπτικοποίηση p-value

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Parameters for visualization
mu0 = 100
xbar = 105
s = 15
n = 36
alpha = 0.05

# Calculate test statistic
se = s / np.sqrt(n)
t_stat = (xbar - mu0) / se
df = n - 1

# p-value
p_value = 2 * stats.t.sf(abs(t_stat), df)

# Create visualization
t_vals = np.linspace(-4, 4, 1000)
density_vals = stats.t.pdf(t_vals, df)

# Plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(t_vals, density_vals, 'k-', linewidth=2,
        label='t-distribution')

# Shade rejection regions (two-tailed)
t_crit = stats.t.ppf(1 - alpha/2, df)
t_left = t_vals[t_vals <= -t_crit]
t_right = t_vals[t_vals >= t_crit]

ax.fill_between(t_left, 0, stats.t.pdf(t_left, df),
                alpha=0.3, color='red',
                label=f'Rejection region (alpha={alpha})')
ax.fill_between(t_right, 0, stats.t.pdf(t_right, df),
                alpha=0.3, color='red')

# Mark observed t-statistic
ax.axvline(t_stat, color='blue', linewidth=2, linestyle='--',
           label=f'Observed t = {t_stat:.2f}')
ax.axvline(-t_stat, color='blue', linewidth=2, linestyle='--')

# Mark critical values
ax.axvline(-t_crit, color='red', linewidth=2, linestyle=':',
           label=f'Critical values = +/- {t_crit:.2f}')
ax.axvline(t_crit, color='red', linewidth=2, linestyle=':')

ax.set_xlabel('t', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.set_title(f't-distribution (df={df}) with Test Statistic',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper left')
ax.grid(alpha=0.3)

# Add text
ax.text(0, max(density_vals) * 0.9,
        f'p-value = {p_value:.4f}',
        ha='center', fontsize=12, fontweight='bold',
        color='blue',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

if p_value < alpha:
    decision_text = 'Decision: Reject H0'
    decision_color = 'red'
else:
    decision_text = 'Decision: Fail to reject H0'
    decision_color = 'darkgreen'

ax.text(0, max(density_vals) * 0.8,
        decision_text,
        ha='center', fontsize=11, fontweight='bold',
        color=decision_color,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout()
plt.show()
