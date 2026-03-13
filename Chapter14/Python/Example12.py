# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 12: Ζευγαρωτός Έλεγχος και Σύγκριση Αναλογιών (Κλινική Μελέτη)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

np.random.seed(101)
n_pair = 20

# --- Paired t-test ---
before = np.round(np.random.normal(148, 14, n_pair), 1)
change = np.round(np.random.normal(12.5, 5, n_pair), 1)
after  = before - change
d      = before - after

print("=== Paired t-test ===")
print(f"Mean before  : {before.mean():.2f} mmHg")
print(f"Mean after   : {after.mean():.2f}  mmHg")
print(f"Mean diff    : {d.mean():.3f} mmHg")
print(f"SD of diff   : {d.std(ddof=1):.3f}")

w, p_sw = stats.shapiro(d)
print(f"\nShapiro-Wilk (differences): W = {w:.4f}, p = {p_sw:.4f}")
print("Normality:", "Supported" if p_sw > 0.05 else "Violated")

t_pair, p_pair_two = stats.ttest_rel(before, after)
p_pair_one = p_pair_two / 2 if t_pair > 0 else 1 - p_pair_two / 2
print(f"\nscipy ttest_rel: t = {t_pair:.4f}, "
      f"p (one-sided) = {p_pair_one:.4f}")

# Manual
d_bar  = d.mean();  s_d = d.std(ddof=1);  se_d = s_d / np.sqrt(n_pair)
t_man  = d_bar / se_d
p_man  = stats.t.sf(t_man, df=n_pair-1)
t_crit = stats.t.ppf(0.975, df=n_pair-1)
ci_d   = [d_bar - t_crit*se_d, d_bar + t_crit*se_d]
cohens_d_pair = d_bar / s_d

print(f"Manual: t = {t_man:.4f}, df = {n_pair-1}, "
      f"p (one-sided) = {p_man:.4f}")
print(f"95% CI for mu_d : [{ci_d[0]:.3f}, {ci_d[1]:.3f}] mmHg")
print(f"Cohen's d (paired): {cohens_d_pair:.4f}")
print("Decision:", "Reject H0" if p_man < 0.05 else "Fail to reject H0")

# --- Two-proportion z-test ---
print("\n=== Two-Proportion Z-test ===")
n1_p, x1_p = 35, 22
n2_p, x2_p = 30, 15
p1_h, p2_h = x1_p/n1_p, x2_p/n2_p

for lbl, n, p in [("A", n1_p, p1_h), ("B", n2_p, p2_h)]:
    print(f"Group {lbl}: n*p = {n*p:.1f}, n*(1-p) = {n*(1-p):.1f}")

z_sm, p_sm = proportions_ztest([x1_p, x2_p], [n1_p, n2_p],
                               alternative='two-sided')
print(f"\nstatsmodels: z = {z_sm:.4f}, p = {p_sm:.4f}")

# Manual
p_bar   = (x1_p + x2_p) / (n1_p + n2_p)
se_pool = np.sqrt(p_bar*(1-p_bar)*(1/n1_p + 1/n2_p))
z_man   = (p1_h - p2_h) / se_pool
p_man_z = 2 * stats.norm.cdf(-abs(z_man))
se_ci   = np.sqrt(p1_h*(1-p1_h)/n1_p + p2_h*(1-p2_h)/n2_p)
ci_p    = [(p1_h-p2_h) - 1.96*se_ci, (p1_h-p2_h) + 1.96*se_ci]
h_cohen = 2*np.arcsin(np.sqrt(p1_h)) - 2*np.arcsin(np.sqrt(p2_h))
h_lbl   = ("small"  if abs(h_cohen) < 0.2 else
           "medium" if abs(h_cohen) < 0.5 else "large")

print(f"Manual: z = {z_man:.4f}, p = {p_man_z:.4f}")
print(f"95% CI (p1-p2): [{ci_p[0]:.4f}, {ci_p[1]:.4f}]")
print(f"Cohen's h : {h_cohen:.4f} ({h_lbl} effect)")
print("Decision:", "Reject H0" if p_man_z < 0.05 else "Fail to reject H0")

# --- Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for i in range(n_pair):
    axes[0].plot(['Before','After'], [before[i], after[i]],
                 'o-', color='steelblue', alpha=0.35)
means_pair = [before.mean(), after.mean()]
axes[0].plot(['Before','After'], means_pair, 'D-',
             color='darkred', markersize=8, linewidth=2.5,
             label='Group mean')
axes[0].set_title(
    f"Blood Pressure: Before vs After\n"
    f"t = {t_man:.3f}, p = {p_man:.4f}, d = {cohens_d_pair:.3f}")
axes[0].set_ylabel("Systolic BP (mmHg)")
axes[0].legend()

grps = ['Treatment A', 'Treatment B']
props = [p1_h, p2_h]
ns    = [n1_p, n2_p]
errs  = [1.96*np.sqrt(p*(1-p)/n) for p, n in zip(props, ns)]
axes[1].bar(grps, props, color=['steelblue','cornflowerblue'],
            width=0.4, alpha=0.75)
axes[1].errorbar(grps, props, yerr=errs,
                 fmt='none', color='black', capsize=6, linewidth=1.5)
axes[1].set_ylim(0, 1)
axes[1].yaxis.set_major_formatter(
    plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
axes[1].set_title(
    f"Proportion Improved by Treatment\n"
    f"z = {z_man:.3f}, p = {p_man_z:.3f}, h = {h_cohen:.3f}")
axes[1].set_ylabel("Proportion Improved")

plt.tight_layout()
plt.savefig('paired_and_proportions.png', dpi=300, bbox_inches='tight')
