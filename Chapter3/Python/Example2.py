# Chapter 3 - Binomial Distribution
# Example 2: Quality Control - Acceptance Sampling  (n=100, c=3)

from scipy.stats import binom
from scipy.optimize import fsolve

# Parameters
n = 100
c = 3  # Acceptance number

# i. Probability of acceptance with p = 0.02
p1             = 0.02
prob_accept_p1 = binom.cdf(c, n, p1)
print(f"i. P(Accept | p=0.02) = {prob_accept_p1:.4f}")

# ii. Probability of acceptance with p = 0.05
p2             = 0.05
prob_accept_p2 = binom.cdf(c, n, p2)
print(f"ii. P(Accept | p=0.05) = {prob_accept_p2:.4f}")

# iii. Defect rate for 50% acceptance probability
# Solve: P(X <= 3) = 0.50
def equation(p):
    return binom.cdf(c, n, p) - 0.50

p_50 = fsolve(equation, 0.03)[0]
print(f"iii. Defect rate for 50% acceptance: {p_50:.4f}")

# Verification
print(f"Verification: P(Accept | p={p_50:.4f}) = {binom.cdf(c, n, p_50):.4f}")
