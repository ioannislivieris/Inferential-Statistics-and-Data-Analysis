# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 3: Σύγκριση Δύο Αναλογιών (Z-test Αναλογιών)

import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

n1, x1 = 200, 85
n2, x2 = 220, 105
p1, p2 = x1/n1, x2/n2

# Check assumptions
for label, n, p in [("Group 1", n1, p1), ("Group 2", n2, p2)]:
    print(f"{label}: n*p = {n*p:.1f}, n*(1-p) = {n*(1-p):.1f}")

# Two-proportion z-test via statsmodels
z_stat, p_value = proportions_ztest([x1, x2], [n1, n2],
                                    alternative='two-sided')
print(f"\nz-statistic = {z_stat:.4f}, p-value = {p_value:.4f}")

# Manual calculation
p_bar   = (x1 + x2) / (n1 + n2)
se_pool = np.sqrt(p_bar * (1 - p_bar) * (1/n1 + 1/n2))
z_man   = (p1 - p2) / se_pool
p_man   = 2 * stats.norm.cdf(-abs(z_man))
print(f"Manual: z = {z_man:.4f}, p-value = {p_man:.4f}")

# 95% Confidence interval (unpooled)
se_ci = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)
ci_lo = (p1 - p2) - 1.96 * se_ci
ci_hi = (p1 - p2) + 1.96 * se_ci
print(f"95% CI for (p1-p2): [{ci_lo:.4f}, {ci_hi:.4f}]")
