# Chapter 6 - Κανονική Κατανομή
# Example 2: Υπολογισμός Κβαντιλίων  X ~ N(50, 10²)

from scipy.stats import norm

# Parameters
mu = 50
sigma = 10

# Quantiles
q25 = norm.ppf(0.25, loc=mu, scale=sigma)
q50 = norm.ppf(0.50, loc=mu, scale=sigma)
q75 = norm.ppf(0.75, loc=mu, scale=sigma)

print(f"First quartile (Q1): {q25:.2f}")
print(f"Median (Q2): {q50:.2f}")
print(f"Third quartile (Q3): {q75:.2f}")
print(f"Interquartile Range (IQR): {q75 - q25:.2f}")
