# Chapter 5 - Other Discrete Distributions
# Example 1: Geometric Distribution  p = 0.3

# Note: scipy's geom counts TRIALS to first success, starting from k=1.

from scipy.stats import geom

# Parameter
p = 0.3

# P(X = 5)
prob_exact = geom.pmf(5, p)
print(f"P(X = 5) = {prob_exact:.4f}")

# P(X <= 4)
prob_cumulative = geom.cdf(4, p)
print(f"P(X <= 4) = {prob_cumulative:.4f}")

# P(X > 6) = 1 - P(X <= 6)
prob_greater = 1 - geom.cdf(6, p)
print(f"P(X > 6) = {prob_greater:.4f}")

# Expected number of trials
expected_trials = 1 / p
print(f"Expected trials: {expected_trials:.2f}")
