# Chapter 5 - Other Discrete Distributions
# Example 2: Hypergeometric Distribution
#   Population N=100, defective K=15, sample n=20

# Note: scipy's hypergeom.pmf(k, M, n, N)
#   M = population size
#   n = number of successes in population
#   N = sample size

from scipy.stats import hypergeom

# Parameters
M = 100   # population size
n = 15    # successes in population (defective)
N = 20    # sample size

# P(X = 3)
prob_exact = hypergeom.pmf(3, M, n, N)
print(f"P(X = 3) = {prob_exact:.4f}")

# P(X <= 2)
prob_cumulative = hypergeom.cdf(2, M, n, N)
print(f"P(X <= 2) = {prob_cumulative:.4f}")

# Expected value
expected_value = N * (n / M)
print(f"Expected defective: {expected_value:.2f}")
