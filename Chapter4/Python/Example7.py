# Chapter 4 - Poisson Distribution
# Example 7: Insurance Company Risk Analysis  Poisson(3)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameter
lam = 3

# i. P(X > 5) = 1 - P(X <= 5)
prob = 1 - poisson.cdf(5, lam)
print(f"i. P(X > 5) = {prob:.4f}")

# ii. Mean and standard deviation
mean = lam
std  = np.sqrt(lam)
print(f"\nii. Mean:               {mean}")
print(f"    Standard Deviation: {std:.2f}")

# iii. 95% confidence interval
lower = poisson.ppf(0.025, lam)
upper = poisson.ppf(0.975, lam)
print(f"\niii. 95% Confidence Interval: [{int(lower)}, {int(upper)}]")

# iv. Probabilities for k = 0, ..., 8
print("\niv. Probabilities:")
for k in range(9):
    print(f"    P(X = {k}) = {poisson.pmf(k, lam):.4f}")

# Visualization
x     = np.arange(0, 11)
probs = poisson.pmf(x, lam)

plt.figure(figsize=(10, 6))
plt.bar(x, probs, color='steelblue', alpha=0.7, edgecolor='black')
plt.xlabel('Number of Claims')
plt.ylabel('Probability')
plt.title('Poisson(3) - Insurance Claims Distribution')
plt.xticks(x)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
