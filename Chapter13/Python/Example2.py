# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 2: Έλεγχος αναλογίας με μέγεθος φαινομένου

import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
import statsmodels.stats.power as smp

# Sample data
n = 500
x = 380
p0 = 0.80
alpha = 0.05

p_hat = x / n

print("=== PROPORTION TEST ===")
print(f"Sample: n={n}, x={x}, p-hat={p_hat:.4f} ({p_hat*100:.2f}%)")
print(f"Hypothesized: p0={p0:.2f} ({p0*100:.0f}%)\n")

# Check conditions
print(f"Conditions: np0={n*p0:.1f}, n(1-p0)={n*(1-p0):.1f} "
      f"(both >= 5: {'OK' if n*p0 >= 5 and n*(1-p0) >= 5 else 'WARNING'})\n")

# Manual Z-test
se = np.sqrt(p0 * (1 - p0) / n)
z_stat = (p_hat - p0) / se
p_value = 2 * stats.norm.sf(abs(z_stat))

print("Manual calculation:")
print(f"SE = {se:.4f}")
print(f"z = {z_stat:.3f}")
print(f"p-value = {p_value:.4f}")
print(f"Decision: {'REJECT' if p_value < alpha else 'FAIL TO REJECT'} H0\n")

# Using statsmodels
z_stat_sm, p_value_sm = proportions_ztest(x, n, value=p0,
                                          alternative='two-sided')
print("Using statsmodels:")
print(f"z = {z_stat_sm:.3f}")
print(f"p-value = {p_value_sm:.4f}\n")

# Confidence interval
ci_lower, ci_upper = proportion_confint(x, n, alpha=alpha, method='normal')
print(f"95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")
print(f"Contains p0={p0}? "
      f"{'YES' if ci_lower <= p0 <= ci_upper else 'NO'}\n")

# Effect size (Cohen's h)
h = 2 * (np.arcsin(np.sqrt(p_hat)) - np.arcsin(np.sqrt(p0)))
print(f"Effect size (Cohen's h) = {h:.3f}")
interp = ("Small" if abs(h) < 0.2 else
          "Small-Medium" if abs(h) < 0.5 else
          "Medium-Large" if abs(h) < 0.8 else "Large")
print(f"Interpretation: {interp} effect")

# Sample size for desired margin of error
E = 0.03  # 3% margin of error
z_crit = stats.norm.ppf(1 - alpha/2)
n_required = (z_crit / E)**2 * p_hat * (1 - p_hat)
print(f"\nSample size for E={E:.2f}, confidence={(1-alpha)*100:.0f}%: "
      f"n = {int(np.ceil(n_required))}")

# Power analysis
h_values = np.arange(0.1, 0.6, 0.1)
print("\n=== POWER FOR DIFFERENT EFFECT SIZES ===")
print("Cohen's h | Power")
print("----------+-------")
for h_val in h_values:
    power = smp.zt_ind_solve_power(effect_size=h_val, nobs1=n,
                                   alpha=alpha, alternative='two-sided')
    print(f"  {h_val:.2f}    | {power:.3f}")
