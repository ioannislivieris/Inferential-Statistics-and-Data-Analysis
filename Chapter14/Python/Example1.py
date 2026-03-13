# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 1: Σύγκριση Δύο Μέσων με Ανεξάρτητα Δείγματα (Welch t-test)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(123)
n1, n2 = 30, 25
x_bar1, x_bar2, s1, s2 = 82, 78, 10, 12

# Generate and standardize samples
sample1 = np.random.normal(x_bar1, s1, n1)
sample2 = np.random.normal(x_bar2, s2, n2)
sample1 = sample1 * (s1 / sample1.std(ddof=1)) + (x_bar1 - sample1.mean())
sample2 = sample2 * (s2 / sample2.std(ddof=1)) + (x_bar2 - sample2.mean())

# Levene's test for equality of variances
lev_stat, lev_p = stats.levene(sample1, sample2)
print(f"Levene's test: stat = {lev_stat:.4f}, p-value = {lev_p:.4f}")

# Welch's t-test (default: equal_var=False)
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)
print(f"\nWelch's t-test: t = {t_stat:.4f}, p-value = {p_value:.4f}")

# Pooled t-test (for comparison)
t_pool, p_pool = stats.ttest_ind(sample1, sample2, equal_var=True)
print(f"Pooled  t-test: t = {t_pool:.4f}, p-value = {p_pool:.4f}")

# Manual Welch calculation
se_welch = np.sqrt(s1**2/n1 + s2**2/n2)
t_manual = (x_bar1 - x_bar2) / se_welch
num_df   = (s1**2/n1 + s2**2/n2)**2
den_df   = (s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1)
df_welch = num_df / den_df
p_manual = 2 * stats.t.cdf(-abs(t_manual), df=df_welch)

print(f"\nManual Welch: t = {t_manual:.4f}, df = {df_welch:.2f},"
      f" p-value = {p_manual:.4f}")

# 95% Confidence interval
t_crit  = stats.t.ppf(0.975, df=df_welch)
ci_lo   = (x_bar1 - x_bar2) - t_crit * se_welch
ci_hi   = (x_bar1 - x_bar2) + t_crit * se_welch
print(f"95% CI for (mu1 - mu2): [{ci_lo:.2f}, {ci_hi:.2f}]")

# Cohen's d
sp = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
cohens_d = (x_bar1 - x_bar2) / sp
print(f"Cohen's d: {cohens_d:.3f}")

# Visualization
data = pd.DataFrame({
    'Score' : np.concatenate([sample1, sample2]),
    'Method': ['Method A'] * n1 + ['Method B'] * n2
})
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='Method', y='Score', data=data, palette='Blues', ax=ax,
            width=0.4)
sns.stripplot(x='Method', y='Score', data=data, color='steelblue',
              alpha=0.4, size=4, ax=ax)
ax.set_title(f'Comparison of Two Teaching Methods\n'
             f'Welch t = {t_manual:.3f}, p-value = {p_manual:.3f}',
             fontsize=13)
ax.set_ylabel('Exam Score'); ax.set_xlabel('Teaching Method')
plt.tight_layout()
plt.savefig('two_means_comparison.png', dpi=300, bbox_inches='tight')
