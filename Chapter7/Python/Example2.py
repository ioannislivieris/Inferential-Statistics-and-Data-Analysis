# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 2: Τυποποίηση και υπολογισμοί  X ~ N(100, 15²)

from scipy.stats import norm
import numpy as np

# Parameters
mu    = 100
sigma = 15

# i. Z-score for X = 120
x       = 120
z_score = (x - mu) / sigma
print(f"Z-score for X = 120: {z_score:.2f}")

# ii. P(X <= 120)
prob = norm.cdf(x, loc=mu, scale=sigma)
print(f"P(X <= 120) = {prob:.4f}")

# Alternatively using z-score
prob_z = norm.cdf(z_score)
print(f"P(X <= 120) using z-score = {prob_z:.4f}")

# iii. Find x such that P(X <= x) = 0.90
x_90 = norm.ppf(0.90, loc=mu, scale=sigma)
print(f"X value at 90th percentile: {x_90:.2f}")

# Verify using z-score
z_90        = norm.ppf(0.90)
x_90_manual = mu + z_90 * sigma
print(f"X value using z-score: {x_90_manual:.2f}")
