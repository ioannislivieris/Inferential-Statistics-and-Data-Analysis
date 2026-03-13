# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 5: One-Way ANOVA — Πλήρης Ανάλυση (διαφήμιση)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm

# Dataset
advertising = pd.DataFrame({
    'Sales'   : [23,25,27,24,26, 30,32,28,31,29, 20,22,19,21,20],
    'Strategy': ['Television']*5 + ['Internet']*5 + ['Print']*5
})

# --- Descriptive statistics ---
print(advertising.groupby('Strategy')['Sales']
      .agg(['count','mean','std','min','max'])
      .round(3))

# --- Visualization ---
fig, ax = plt.subplots(figsize=(9, 6))
sns.boxplot(x='Strategy', y='Sales', data=advertising,
            palette='Blues', width=0.4, ax=ax)
sns.stripplot(x='Strategy', y='Sales', data=advertising,
              color='steelblue', alpha=0.5, size=5, ax=ax)
means = advertising.groupby('Strategy')['Sales'].mean()
for i, (strat, m) in enumerate(means.items()):
    ax.scatter(i, m, marker='D', s=80, color='white',
               edgecolors='black', zorder=5)
ax.set_title('Sales by Advertising Strategy')
ax.set_ylabel('Sales (thousands EUR)')
plt.tight_layout()
plt.savefig('anova_boxplots.png', dpi=300, bbox_inches='tight')

# --- One-Way ANOVA via scipy ---
groups = [advertising[advertising['Strategy'] == s]['Sales'].values
          for s in ['Television', 'Internet', 'Print']]
f_stat, p_value = stats.f_oneway(*groups)
print(f"\nF-statistic = {f_stat:.3f}, p-value = {p_value:.6f}")

# --- ANOVA table via statsmodels ---
model       = ols('Sales ~ C(Strategy)', data=advertising).fit()
anova_table = sm.stats.anova_lm(model, typ=1)
print("\nANOVA Table:\n", anova_table.round(4))

# --- Effect size ---
SSB    = anova_table['sum_sq']['C(Strategy)']
SST    = anova_table['sum_sq'].sum()
MSW    = anova_table['mean_sq']['Residual']
eta_sq = SSB / SST
k, N   = 3, len(advertising)
omega_sq = (SSB - (k-1)*MSW) / (SST + MSW)
print(f"\neta-squared   = {eta_sq:.4f}")
size_label = "small" if eta_sq < 0.06 else "medium" if eta_sq < 0.14 else "large"
print(f"Interpretation: {size_label} effect")
print(f"omega-squared = {omega_sq:.4f}")

# --- Decision ---
print("\nDecision:", "Reject H0" if p_value < 0.05 else "Fail to reject H0")
