# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 3: Έλεγχος διασποράς με διαστήματα εμπιστοσύνης

import numpy as np
from scipy import stats

# Sample data
sample_data = np.array([2.1, 2.5, 2.3, 2.7, 2.4, 2.6, 2.2, 2.8,
                        2.5, 2.3, 2.6, 2.4, 2.7, 2.3, 2.5, 2.4,
                        2.6, 2.5, 2.7, 2.4])

sigma2_0 = 0.04
alpha = 0.05

n = len(sample_data)
s2 = np.var(sample_data, ddof=1)
s = np.std(sample_data, ddof=1)
df = n - 1

print("=== VARIANCE TEST ===")
print(f"n={n}, s^2={s2:.4f}, s={s:.3f}")
print(f"Hypothesized: sigma^2={sigma2_0:.4f}, sigma={np.sqrt(sigma2_0):.3f}\n")

# Chi-square test
chi2_stat = (n - 1) * s2 / sigma2_0
p_right = 1 - stats.chi2.cdf(chi2_stat, df)
p_left = stats.chi2.cdf(chi2_stat, df)
p_value = 2 * min(p_right, p_left)

print("Chi-square test:")
print(f"chi^2 = {chi2_stat:.3f} (df={df})")
print(f"p-value (two-tailed) = {p_value:.4f}")
print(f"p-value (right, H1: sigma^2 > {sigma2_0:.4f}) = {p_right:.4f}")
print(f"p-value (left, H1: sigma^2 < {sigma2_0:.4f}) = {p_left:.4f}")
print(f"\nDecision: {'REJECT' if p_value < alpha else 'FAIL TO REJECT'} H0\n")

# Critical values
chi2_lower = stats.chi2.ppf(alpha/2, df)
chi2_upper = stats.chi2.ppf(1 - alpha/2, df)
print(f"Critical values: [{chi2_lower:.3f}, {chi2_upper:.3f}]")
print(f"Observed chi^2={chi2_stat:.3f} is "
      f"{'IN' if chi2_stat < chi2_lower or chi2_stat > chi2_upper else 'NOT IN'} "
      f"critical region\n")

# Confidence intervals
ci_var_lower = (n - 1) * s2 / chi2_upper
ci_var_upper = (n - 1) * s2 / chi2_lower
ci_sd_lower = np.sqrt(ci_var_lower)
ci_sd_upper = np.sqrt(ci_var_upper)

print(f"95% CI for variance: [{ci_var_lower:.4f}, {ci_var_upper:.4f}]")
print(f"95% CI for SD: [{ci_sd_lower:.3f}, {ci_sd_upper:.3f}]")
print(f"Contains sigma^2_0={sigma2_0:.4f}? "
      f"{'YES (Consistent with not rejecting H0)' if ci_var_lower <= sigma2_0 <= ci_var_upper else 'NO (Consistent with rejecting H0)'}")

# Relationship between CI and hypothesis test
print("\n=== CI-TEST EQUIVALENCE ===")
print("For two-tailed test at alpha=0.05:")
print("- If 95% CI contains sigma^2_0: Fail to reject H0")
print("- If 95% CI excludes sigma^2_0: Reject H0")
print(f"This example: "
      f"{'CI contains sigma^2_0, so we fail to reject H0' if ci_var_lower <= sigma2_0 <= ci_var_upper else 'CI excludes sigma^2_0, so we reject H0'}")
