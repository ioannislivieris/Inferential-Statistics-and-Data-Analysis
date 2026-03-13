# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 2: Ανάλυση Ζευγαρωτών Δεδομένων (Paired t-test)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(456)
n = 12
before      = np.round(np.random.normal(85, 12, n), 1)
weight_loss = np.round(np.random.normal(3.5, 2, n), 1)
after       = before - weight_loss

weight_data = pd.DataFrame({
    'Subject'   : range(1, n + 1),
    'Before'    : before,
    'After'     : after,
    'Difference': before - after
})
print(weight_data)

# Paired t-test (one-sided: before > after)
t_stat, p_val = stats.ttest_rel(weight_data['Before'], weight_data['After'],
                                alternative='greater')
print(f"\nPaired t-test: t = {t_stat:.4f}, p-value = {p_val:.4f}")

# Manual calculation
d_bar = weight_data['Difference'].mean()
s_d   = weight_data['Difference'].std(ddof=1)
se_d  = s_d / np.sqrt(n)
t_man = d_bar / se_d
p_man = stats.t.sf(t_man, df=n-1)   # one-sided (upper)

print(f"\nManual: d_bar = {d_bar:.3f}, s_d = {s_d:.3f}, SE = {se_d:.3f}")
print(f"        t = {t_man:.4f}, p-value = {p_man:.4f}")

# 95% CI
t_crit = stats.t.ppf(0.975, df=n-1)
ci_lo  = d_bar - t_crit * se_d
ci_hi  = d_bar + t_crit * se_d
print(f"95% CI for mu_d: [{ci_lo:.2f}, {ci_hi:.2f}] kg")

# Normality of differences
w, p_sw = stats.shapiro(weight_data['Difference'])
print(f"\nShapiro-Wilk: W = {w:.4f}, p = {p_sw:.4f}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

for i in range(n):
    ax1.plot(['Before', 'After'],
             [weight_data.loc[i, 'Before'], weight_data.loc[i, 'After']],
             'o-', color='steelblue', alpha=0.5)
ax1.set_title(f'Individual Weight Changes\n'
              f'Mean loss = {d_bar:.2f} kg, p = {p_man:.4f}')
ax1.set_ylabel('Weight (kg)')

ax2.hist(weight_data['Difference'], bins=6, color='steelblue',
         edgecolor='white', alpha=0.8)
ax2.axvline(x=0, color='red', linestyle='--', label='H0: mu_d = 0')
ax2.axvline(x=d_bar, color='orange', linestyle='-',
            linewidth=2, label=f'mean = {d_bar:.2f}')
ax2.set_title('Distribution of Differences')
ax2.set_xlabel('Weight Loss (kg)')
ax2.legend()

plt.tight_layout()
plt.savefig('paired_analysis.png', dpi=300, bbox_inches='tight')
