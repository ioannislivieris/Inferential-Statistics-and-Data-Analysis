# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 4: Σύγκριση Δύο Διασπορών (F-test και Levene)

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt, seaborn as sns, pandas as pd

np.random.seed(789)
machine1 = np.random.normal(50, 2.5, 25)
machine2 = np.random.normal(50, 1.5, 30)

# F-test (larger variance in numerator for convenience)
s1_sq, s2_sq = machine1.var(ddof=1), machine2.var(ddof=1)
f_stat = s1_sq / s2_sq
df1, df2 = len(machine1) - 1, len(machine2) - 1
p_val = 2 * min(stats.f.cdf(f_stat, df1, df2),
                stats.f.sf(f_stat,  df1, df2))
print(f"F = {f_stat:.4f}, df1 = {df1}, df2 = {df2}")
print(f"p-value (two-sided) = {p_val:.4f}")

# Levene's test
lev_stat, lev_p = stats.levene(machine1, machine2)
print(f"\nLevene's test: stat = {lev_stat:.4f}, p = {lev_p:.4f}")

# Visualization
combined = pd.DataFrame({
    'Length' : np.concatenate([machine1, machine2]),
    'Machine': ['Machine 1']*25 + ['Machine 2']*30
})
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='Machine', y='Length', data=combined, palette='Blues',
            width=0.4, ax=ax)
sns.stripplot(x='Machine', y='Length', data=combined, color='steelblue',
              alpha=0.4, size=4, ax=ax)
ax.set_title(f'Comparison of Machine Variability\n'
             f'F-test p-value = {p_val:.4f}')
ax.set_ylabel('Length (mm)')
plt.tight_layout()
plt.savefig('variance_comparison.png', dpi=300, bbox_inches='tight')
