# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 11: Πλήρης ANOVA με Post-hoc (Τρεις Μέθοδοι Διδασκαλίας)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from itertools import combinations

np.random.seed(42)
n = 8

# 1. Simulate data
education = pd.DataFrame({
    'Score' : np.concatenate([
        np.random.normal(72, 8, n),
        np.random.normal(81, 7, n),
        np.random.normal(85, 9, n)]),
    'Method': ['Traditional']*n + ['Interactive']*n + ['Flipped']*n
})

# 2. Descriptive statistics
print("=== Descriptive Statistics ===")
print(education.groupby('Method')['Score']
      .agg(['count','mean','std','min','max']).round(2))

# 3. Check assumptions
model     = ols('Score ~ C(Method)', data=education).fit()
residuals = model.resid

w, p_sw = stats.shapiro(residuals)
print(f"\nShapiro-Wilk (residuals): W = {w:.4f}, p = {p_sw:.4f}")
print("Normality:", "Supported" if p_sw > 0.05 else "Violated")

groups = [education[education['Method'] == m]['Score'].values
          for m in ['Traditional', 'Interactive', 'Flipped']]
lev_stat, lev_p = stats.levene(*groups)
print(f"\nLevene test: stat = {lev_stat:.4f}, p = {lev_p:.4f}")
print("Homoscedasticity:", "Supported" if lev_p > 0.05 else "Violated")

vars_g = {m: education[education['Method']==m]['Score'].var(ddof=1)
          for m in education['Method'].unique()}
ratio = max(vars_g.values()) / min(vars_g.values())
print(f"Max/Min variance ratio: {ratio:.2f}")

# 4. One-Way ANOVA
anova_table = sm.stats.anova_lm(model, typ=1)
print("\n=== ANOVA Table ===")
print(anova_table.round(4))

SSB    = anova_table.loc['C(Method)', 'sum_sq']
SST    = anova_table['sum_sq'].sum()
MSW    = anova_table.loc['Residual', 'mean_sq']
f_stat = anova_table.loc['C(Method)', 'F']
p_val  = anova_table.loc['C(Method)', 'PR(>F)']
eta_sq = SSB / SST
k, N   = 3, len(education)

print(f"\nF-statistic = {f_stat:.3f},  p-value = {p_val:.6f}")
size_lbl = "small" if eta_sq < 0.06 else "medium" if eta_sq < 0.14 else "large"
print(f"eta-squared = {eta_sq:.4f} -> {size_lbl} effect")
print("Decision:", "Reject H0." if p_val < 0.05 else "Fail to reject H0.")

# 5. Post-hoc: Tukey HSD
print("\n=== Tukey HSD Post-hoc ===")
tukey = pairwise_tukeyhsd(education['Score'], education['Method'], alpha=0.05)
print(tukey)

# 6. Bonferroni (manual)
methods = education['Method'].unique()
pairs   = list(combinations(methods, 2))
m_bon   = len(pairs)
print(f"\nBonferroni Post-hoc (alpha_adj = {0.05/m_bon:.4f}):")
for s1, s2 in pairs:
    g1 = education[education['Method']==s1]['Score']
    g2 = education[education['Method']==s2]['Score']
    t_s, p_raw = stats.ttest_ind(g1, g2)
    p_adj = min(p_raw * m_bon, 1.0)
    sig   = ("***" if p_adj < 0.001 else "**" if p_adj < 0.01
             else "*" if p_adj < 0.05 else "ns")
    print(f"  {s1} vs {s2}: t={t_s:.3f}, "
          f"p_raw={p_raw:.4f}, p_adj={p_adj:.4f} {sig}")

# 7. Visualization
fig, axes = plt.subplots(1, 3, figsize=(16, 6))

sns.boxplot(x='Method', y='Score', data=education,
            palette='Blues', width=0.45, ax=axes[0])
sns.stripplot(x='Method', y='Score', data=education,
              color='steelblue', alpha=0.5, size=5, ax=axes[0])
axes[0].set_title(f'Scores by Method\nF={f_stat:.2f}, p={p_val:.4f}')
axes[0].set_ylabel('Exam Score')

tukey_summary = pd.DataFrame({
    'comparison': [f"{r[0]} vs {r[1]}" for r in tukey._results_table.data[1:]],
    'diff'      : [float(r[2]) for r in tukey._results_table.data[1:]],
    'lower'     : [float(r[4]) for r in tukey._results_table.data[1:]],
    'upper'     : [float(r[5]) for r in tukey._results_table.data[1:]]
})
axes[1].errorbar(tukey_summary['diff'], tukey_summary['comparison'],
                 xerr=[tukey_summary['diff']-tukey_summary['lower'],
                       tukey_summary['upper']-tukey_summary['diff']],
                 fmt='o', color='steelblue', capsize=5, linewidth=2)
axes[1].axvline(0, color='red', linestyle='--', linewidth=1.5)
axes[1].set_title('Tukey HSD 95% CI\nfor Mean Differences')
axes[1].set_xlabel('Mean Difference')

stats.probplot(residuals, dist='norm', plot=axes[2])
axes[2].set_title('Q-Q Plot of ANOVA Residuals')

plt.tight_layout()
plt.savefig('full_anova_example.png', dpi=300, bbox_inches='tight')
