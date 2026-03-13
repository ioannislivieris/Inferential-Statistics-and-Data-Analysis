# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 1: Υπολογισμός πιθανοτήτων  Z ~ N(0, 1)

from scipy.stats import norm

# i. P(Z <= 1.5)
prob1 = norm.cdf(1.5)
print(f"P(Z <= 1.5) = {prob1:.4f}")

# ii. P(Z > -0.8) = 1 - P(Z <= -0.8)
prob2 = 1 - norm.cdf(-0.8)
print(f"P(Z > -0.8) = {prob2:.4f}")

# iii. P(-1 < Z < 2)
prob3 = norm.cdf(2) - norm.cdf(-1)
print(f"P(-1 < Z < 2) = {prob3:.4f}")
