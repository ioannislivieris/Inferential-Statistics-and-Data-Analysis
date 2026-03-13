# Chapter 5 - Other Discrete Distributions
# Example 3: Negative Binomial Distribution  r=5, p=0.4

# Note: scipy's nbinom counts FAILURES before the r-th success.
# X = total trials = failures + r  →  failures = X - r

import numpy as np
from scipy.stats import nbinom

# Parameters
r = 5    # number of successes required
p = 0.4  # probability of success per trial

# P(X = 12 total trials) → 12 - 5 = 7 failures before 5th success
prob_exact = nbinom.pmf(7, r, p)
print(f"P(X = 12 trials) = {prob_exact:.4f}")

# Expected number of trials
expected_trials = r / p
print(f"Expected trials: {expected_trials:.2f}")

# Variance (for number of trials)
variance = r * (1 - p) / (p**2)
print(f"Variance: {variance:.2f}")
