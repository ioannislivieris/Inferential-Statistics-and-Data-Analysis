# Chapter 4 - Poisson Distribution
# Example 2: Call Center Traffic Analysis  Poisson(30)

from scipy.stats import poisson

# Parameter
lam = 30

# i. P(X = 25)
prob_exact = poisson.pmf(25, lam)
print(f"i. P(X = 25) = {prob_exact:.4f}")

# ii. P(X > 35) = 1 - P(X <= 35)
prob_greater = 1 - poisson.cdf(35, lam)
print(f"ii. P(X > 35) = {prob_greater:.4f}")

# iii. 95th percentile
percentile_95 = poisson.ppf(0.95, lam)
print(f"iii. 95th percentile: {int(percentile_95)} calls")

# Verification
print(f"Verification: P(X <= {int(percentile_95)}) = {poisson.cdf(percentile_95, lam):.4f}")
