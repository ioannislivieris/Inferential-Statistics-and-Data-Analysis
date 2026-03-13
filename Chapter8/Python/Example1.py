# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 1: Ομοιόμορφη Κατανομή  X ~ U(5, 15)
#   Note: scipy uniform(loc=a, scale=b-a)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Parameters: uniform(loc=a, scale=b-a)
a    = 5
b    = 15
dist = uniform(loc=a, scale=b - a)

# i. P(X <= 10)
prob1 = dist.cdf(10)
print(f"P(X <= 10) = {prob1:.4f}")

# ii. P(8 < X < 12)
prob2 = dist.cdf(12) - dist.cdf(8)
print(f"P(8 < X < 12) = {prob2:.4f}")

# iii. 75th percentile
q75 = dist.ppf(0.75)
print(f"75th percentile: {q75:.2f}")

# Visualization
x = np.linspace(a - 2, b + 2, 1000)
y = dist.pdf(x)

plt.figure(figsize=(12, 7))
plt.plot(x, y, 'b-', linewidth=2, label='PDF')

# Shade area for P(8 < X < 12)
x_shade = np.linspace(8, 12, 100)
y_shade  = dist.pdf(x_shade)
plt.fill_between(x_shade, y_shade, alpha=0.3, color='blue',
                 label=f'P(8 < X < 12) = {prob2:.2f}')

plt.axvline(a, color='red', linestyle='--', linewidth=1.5,
            label='Support boundaries')
plt.axvline(b, color='red', linestyle='--', linewidth=1.5)

plt.xlabel('x', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Uniform Distribution U(5, 15)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
