# Chapter 4 - Poisson Distribution
# Example 1: Basic Probability Calculations  Poisson(5)

from scipy.stats import poisson

# Parameter
lam = 5

# P(X = 4)
prob_exact = poisson.pmf(4, lam)
print(f"P(X = 4) = {prob_exact:.4f}")

# P(X <= 6)
prob_cumulative = poisson.cdf(6, lam)
print(f"P(X <= 6) = {prob_cumulative:.4f}")

# P(X >= 3) = 1 - P(X <= 2)
prob_greater = 1 - poisson.cdf(2, lam)
print(f"P(X >= 3) = {prob_greater:.4f}")
