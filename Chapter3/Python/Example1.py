# Chapter 3 - Binomial Distribution
# Example 1: Basic Probability Calculations  B(10, 0.3)

from scipy.stats import binom

# Parameters
n = 10
p = 0.3

# P(X = 3)
prob_exact = binom.pmf(3, n, p)
print(f"P(X = 3) = {prob_exact:.4f}")

# P(X <= 5)
prob_cumulative = binom.cdf(5, n, p)
print(f"P(X <= 5) = {prob_cumulative:.4f}")

# P(X >= 4) = 1 - P(X <= 3)
prob_greater = 1 - binom.cdf(3, n, p)
print(f"P(X >= 4) = {prob_greater:.4f}")
