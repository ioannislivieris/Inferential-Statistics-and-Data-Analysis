# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 9: Post-hoc Αναλύσεις (Tukey HSD, Bonferroni, Scheffé)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from itertools import combinations

advertising = pd.DataFrame({
    'Sales'   : [23,25,27,24,26, 30,32,28,31,29, 20,22,19,21,20],
    'Strategy': ['Television']*5 + ['Internet']*5 + ['Print']*5
})

# 1. Tukey HSD
print("=== Tukey HSD ===")
tukey = pairwise_tukeyhsd(advertising['Sales'], advertising['Strategy'],
                          alpha=0.05)
print(tukey)

# Visualize Tukey CI
fig, ax = plt.subplots(figsize=(9, 5))
tukey.plot_simultaneous(ax=ax, xlabel='Mean Difference',
                        ylabel='Comparison')
ax.set_title('Tukey HSD 95% Confidence Intervals')
plt.tight_layout()
plt.savefig('tukey_hsd.png', dpi=300, bbox_inches='tight')

# 2. Bonferroni correction (manual pairwise t-tests)
strategies = advertising['Strategy'].unique()
pairs_list = list(combinations(strategies, 2))
m = len(pairs_list)

print(f"\nBonferroni Post-hoc (m={m}, alpha_adj={0.05/m:.4f}):")
for (s1, s2) in pairs_list:
    g1 = advertising[advertising['Strategy'] == s1]['Sales']
    g2 = advertising[advertising['Strategy'] == s2]['Sales']
    t_stat, p_raw = stats.ttest_ind(g1, g2)
    p_adj = min(p_raw * m, 1.0)  # Bonferroni adjustment
    sig = "***" if p_adj < 0.001 else "**" if p_adj < 0.01 else "*" if p_adj < 0.05 else "ns"
    print(f"  {s1} vs {s2}: t={t_stat:.3f}, p_raw={p_raw:.4f}, "
          f"p_adj={p_adj:.4f} {sig}")

# 3. Scheffe test (manual implementation)
print("\nScheffe Post-hoc:")
from statsmodels.formula.api import ols
import statsmodels.api as sm
model = ols('Sales ~ C(Strategy)', data=advertising).fit()
anova_table = sm.stats.anova_lm(model, typ=1)
MSW = anova_table.loc['Residual', 'sum_sq'] / anova_table.loc['Residual', 'df']
k = len(strategies)
N = len(advertising)

for (s1, s2) in pairs_list:
    n1_g = len(advertising[advertising['Strategy'] == s1])
    n2_g = len(advertising[advertising['Strategy'] == s2])
    m1 = advertising[advertising['Strategy'] == s1]['Sales'].mean()
    m2 = advertising[advertising['Strategy'] == s2]['Sales'].mean()
    se = np.sqrt(MSW * (1/n1_g + 1/n2_g))
    f_obs = ((m1 - m2) / se) ** 2 / (k - 1)
    p_scheffe = 1 - stats.f.cdf(f_obs, k - 1, N - k)
    sig = "***" if p_scheffe < 0.001 else "**" if p_scheffe < 0.01 \
          else "*" if p_scheffe < 0.05 else "ns"
    print(f"  {s1} vs {s2}: F={f_obs:.3f}, p={p_scheffe:.4f} {sig}")
