# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 1: Έλεγχοι Z και t για μία μέση τιμή

import numpy as np
from scipy import stats
import statsmodels.stats.power as smp

# Sample data
sample_data = np.array([8.5, 7.2, 9.1, 8.8, 7.5, 8.3, 9.2, 8.1,
                        7.8, 8.6, 9.0, 8.4, 7.9, 8.7, 9.3, 8.2,
                        7.6, 8.9, 8.0, 8.5, 7.7, 9.1, 8.3, 8.6, 7.4])

mu0 = 8.0
sigma_known = 0.6  # For Z-test
alpha = 0.05

# Descriptive statistics
n = len(sample_data)
xbar = np.mean(sample_data)
s = np.std(sample_data, ddof=1)

print("=== DESCRIPTIVE STATISTICS ===")
print(f"n = {n}, x-bar = {xbar:.3f}, s = {s:.3f}\n")

# ============ Z-TEST (KNOWN SIGMA) ============
print(f"=== Z-TEST (Known sigma = {sigma_known:.2f}) ===")
se_z = sigma_known / np.sqrt(n)
z_stat = (xbar - mu0) / se_z
p_value_z = 2 * stats.norm.sf(abs(z_stat))
z_crit = stats.norm.ppf(1 - alpha/2)

print(f"SE = {se_z:.4f}")
print(f"z-statistic = {z_stat:.3f}")
print(f"Critical value = +/- {z_crit:.3f}")
print(f"p-value = {p_value_z:.4f}")
print(f"Decision: {'REJECT' if p_value_z < alpha else 'FAIL TO REJECT'} H0\n")

# 95% CI with known sigma
ci_z_lower = xbar - z_crit * se_z
ci_z_upper = xbar + z_crit * se_z
print(f"95% CI (Z): [{ci_z_lower:.3f}, {ci_z_upper:.3f}]")
print(f"Does CI contain mu0={mu0:.1f}? "
      f"{'YES' if ci_z_lower <= mu0 <= ci_z_upper else 'NO'}\n")

# ============ T-TEST (UNKNOWN SIGMA) ============
print("=== T-TEST (Unknown sigma) ===")
t_stat, p_value_t = stats.ttest_1samp(sample_data, mu0)
df = n - 1
t_crit = stats.t.ppf(1 - alpha/2, df)

print(f"t-statistic = {t_stat:.3f}")
print(f"df = {df}")
print(f"Critical value = +/- {t_crit:.3f}")
print(f"p-value = {p_value_t:.4f}")
print(f"Decision: {'REJECT' if p_value_t < alpha else 'FAIL TO REJECT'} H0")

# 95% CI with unknown sigma
se_t = s / np.sqrt(n)
ci_t_lower = xbar - t_crit * se_t
ci_t_upper = xbar + t_crit * se_t
print(f"95% CI (t): [{ci_t_lower:.3f}, {ci_t_upper:.3f}]")

# Effect size
cohens_d = (xbar - mu0) / s
print(f"\nEffect size (Cohen's d) = {cohens_d:.3f}")
interp = ("Small" if abs(cohens_d) < 0.2 else
          "Small-Medium" if abs(cohens_d) < 0.5 else
          "Medium-Large" if abs(cohens_d) < 0.8 else "Large")
print(f"Interpretation: {interp} effect")

print(f"\nCI contains mu0? "
      f"{'YES (Consistent with failing to reject H0)' if ci_t_lower <= mu0 <= ci_t_upper else 'NO (Consistent with rejecting H0)'}")

# ============ POWER ANALYSIS ============
print("\n=== POWER ANALYSIS ===")
effect_sizes = np.arange(0.2, 1.2, 0.2)
print("Effect Size (d) | Power")
print("----------------+-------")
for d in effect_sizes:
    power = smp.TTestPower().solve_power(effect_size=d, nobs=n,
                                         alpha=alpha, alternative='two-sided')
    print(f"     {d:.2f}       | {power:.3f}")

# Sample size for desired power
desired_power = 0.80
n_required = smp.TTestPower().solve_power(effect_size=0.5,
                                          power=desired_power,
                                          alpha=alpha,
                                          alternative='two-sided')
print(f"\nSample size needed for d=0.5, power={desired_power:.2f}: "
      f"n = {int(np.ceil(n_required))}")
