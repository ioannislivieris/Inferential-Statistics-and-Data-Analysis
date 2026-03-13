# Chapter 6 - Κανονική Κατανομή
# Example 1: Υπολογισμός πιθανοτήτων  X ~ N(100, 15²)

from scipy.stats import norm

# Parameters
mu = 100
sigma = 15

# P(X <= 120)
prob1 = norm.cdf(120, loc=mu, scale=sigma)
print(f"P(X <= 120) = {prob1:.4f}")

# P(X > 90) = 1 - P(X <= 90)
prob2 = 1 - norm.cdf(90, loc=mu, scale=sigma)
print(f"P(X > 90) = {prob2:.4f}")

# P(85 < X < 110) = P(X < 110) - P(X < 85)
prob3 = norm.cdf(110, loc=mu, scale=sigma) - \
        norm.cdf(85, loc=mu, scale=sigma)
print(f"P(85 < X < 110) = {prob3:.4f}")
