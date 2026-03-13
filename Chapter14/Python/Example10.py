# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 10: Πλήρης Ανάλυση Δύο Ανεξάρτητων Δειγμάτων
#   (Z-test, Welch, Pooled, Cohen's d, Power)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(2024)

# Known parameters
n1, n2     = 35, 30
sigma1, sigma2 = 8, 10
mu0_diff   = 0

# Generate samples
sample1 = np.random.normal(12.5, sigma1, n1)
sample2 = np.random.normal(9.0,  sigma2, n2)
x1, x2  = sample1.mean(), sample2.mean()
s1, s2  = sample1.std(ddof=1), sample2.std(ddof=1)

print("=== Descriptive Statistics ===")
for lbl, n, x, s in [("A", n1, x1, s1), ("B", n2, x2, s2)]:
    print(f"Group {lbl}: n={n}, mean={x:.3f}, sd={s:.3f}")
print(f"Observed difference (A - B): {x1-x2:.3f}")

# 1. Z-test (known sigmas)
print("\n=== Z-test (known sigma) ===")
se_z   = np.sqrt(sigma1**2/n1 + sigma2**2/n2)
z_stat = (x1 - x2 - mu0_diff) / se_z
p_z    = 2 * stats.norm.cdf(-abs(z_stat))
ci_z   = [(x1-x2) - 1.96*se_z, (x1-x2) + 1.96*se_z]

print(f"SE              : {se_z:.4f}")
print(f"z-statistic     : {z_stat:.4f}")
print(f"p-value         : {p_z:.4f}")
print(f"95% CI (mu1-mu2): [{ci_z[0]:.3f}, {ci_z[1]:.3f}]")
print("Decision:", "Reject H0" if p_z < 0.05 else "Fail to reject H0")

# 2. Equality of variances: F-test + Levene
print("\n=== Equality of Variances ===")
f_val = s1**2 / s2**2
df1_f, df2_f = n1-1, n2-1
p_f = 2 * min(stats.f.cdf(f_val, df1_f, df2_f),
              stats.f.sf(f_val,  df1_f, df2_f))
print(f"F-test: F = {f_val:.4f}, p = {p_f:.4f}")
print("Variances are", "equal" if p_f > 0.05 else "unequal",
      "(alpha = 0.05)")

lev_stat, lev_p = stats.levene(sample1, sample2)
print(f"Levene: stat = {lev_stat:.4f}, p = {lev_p:.4f}")

# 3. Welch t-test (default - unequal variances)
print("\n=== Welch t-test (unequal variances) ===")
t_w, p_w = stats.ttest_ind(sample1, sample2, equal_var=False)

se_w     = np.sqrt(s1**2/n1 + s2**2/n2)
t_w_man  = (x1 - x2 - mu0_diff) / se_w
num_df   = (s1**2/n1 + s2**2/n2)**2
den_df   = (s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1)
df_w     = num_df / den_df
p_w_man  = 2 * stats.t.cdf(-abs(t_w_man), df=df_w)
t_crit_w = stats.t.ppf(0.975, df=df_w)
ci_w     = [(x1-x2) - t_crit_w*se_w, (x1-x2) + t_crit_w*se_w]

print(f"scipy  : t = {t_w:.4f}, p = {p_w:.4f}")
print(f"Manual : t = {t_w_man:.4f}, df = {df_w:.2f}, p = {p_w_man:.4f}")
print(f"95% CI : [{ci_w[0]:.3f}, {ci_w[1]:.3f}]")
print("Decision:", "Reject H0" if p_w_man < 0.05 else "Fail to reject H0")

# 4. Pooled t-test (equal variances - for reference)
print("\n=== Pooled t-test (equal variances) ===")
t_pool, p_pool = stats.ttest_ind(sample1, sample2, equal_var=True)
sp    = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
se_p  = sp * np.sqrt(1/n1 + 1/n2)
print(f"scipy  : t = {t_pool:.4f}, p = {p_pool:.4f}")
print(f"Pooled SD (sp): {sp:.4f}")

# 5. Effect size and power
cohens_d = (x1 - x2) / sp
d_lbl    = ("small"        if abs(cohens_d) < 0.2 else
            "medium"       if abs(cohens_d) < 0.5 else
            "medium-large" if abs(cohens_d) < 0.8 else "large")
print(f"\nCohen's d : {cohens_d:.4f} ({d_lbl} effect)")

alpha = 0.05
z_alpha2 = stats.norm.ppf(1 - alpha/2)
se_effect = np.sqrt(sigma1**2/n1 + sigma2**2/n2)
ncp      = abs(x1 - x2) / se_effect
power    = stats.norm.cdf(ncp - z_alpha2) + stats.norm.cdf(-ncp - z_alpha2)
print(f"Power (1-beta): {power:.4f}")

# Power curve
d_seq  = np.linspace(0.1, 1.5, 100)
n_eff  = 1 / (1/n1 + 1/n2)
pwr_seq = []
for d in d_seq:
    ncp_d = d * np.sqrt(n_eff)
    pwr   = (stats.norm.cdf(ncp_d - z_alpha2) +
             stats.norm.cdf(-ncp_d - z_alpha2))
    pwr_seq.append(pwr)

# 6. Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

combined = pd.DataFrame({
    'Value': np.concatenate([sample1, sample2]),
    'Group': ['A']*n1 + ['B']*n2
})

sns.boxplot(x='Group', y='Value', data=combined,
            palette='Blues', width=0.4, ax=axes[0])
sns.stripplot(x='Group', y='Value', data=combined,
              color='steelblue', alpha=0.45, size=4, ax=axes[0])
for i, grp in enumerate(['A','B']):
    m = combined[combined['Group']==grp]['Value'].mean()
    axes[0].scatter(i, m, marker='D', s=70,
                    color='white', edgecolors='black', zorder=5)
axes[0].set_title(
    f"BP Reduction by Treatment\n"
    f"Welch t = {t_w_man:.3f}, p = {p_w_man:.3f}, "
    f"d = {cohens_d:.3f}")
axes[0].set_ylabel("BP Reduction (mmHg)")
axes[0].set_xlabel("Treatment")

axes[1].plot(d_seq, pwr_seq, color='steelblue', linewidth=2)
axes[1].axhline(0.80, color='red', linestyle='--',
                linewidth=1.2, label='80% power')
axes[1].axvline(abs(cohens_d), color='orange', linestyle=':',
                linewidth=1.5,
                label=f"Observed d = {abs(cohens_d):.2f}")
axes[1].set_title(f"Power Curve (n1={n1}, n2={n2})")
axes[1].set_xlabel("Cohen's d")
axes[1].set_ylabel("Power (1 - beta)")
axes[1].legend(fontsize=11)

plt.tight_layout()
plt.savefig('two_sample_full.png', dpi=300, bbox_inches='tight')
