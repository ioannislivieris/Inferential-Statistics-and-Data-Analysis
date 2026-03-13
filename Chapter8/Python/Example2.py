# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 2: Εκθετική Κατανομή  X ~ Exp(λ = 0.5)
#   Note: scipy expon(scale=1/lambda)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parameter: expon(scale=1/lambda)
lambda_param = 0.5
dist         = expon(scale=1 / lambda_param)

# i. P(X <= 2)
prob1 = dist.cdf(2)
print(f"P(X <= 2) = {prob1:.4f}")

# ii. P(X > 3)
prob2 = 1 - dist.cdf(3)
print(f"P(X > 3) = {prob2:.4f}")

# iii. Median
median_x          = dist.ppf(0.5)
median_theoretical = np.log(2) / lambda_param
print(f"Median: {median_x:.4f}")
print(f"Theoretical median: {median_theoretical:.4f}")

# Mean
mean_x = dist.mean()
print(f"Mean: {mean_x:.4f}")

# Visualization
x = np.linspace(0, 10, 1000)
y = dist.pdf(x)

plt.figure(figsize=(12, 7))
plt.plot(x, y, 'b-', linewidth=2, label='PDF')

# Mark mean and median
plt.axvline(mean_x,   color='red',   linestyle='--', linewidth=2,
            label=f'Mean = {mean_x:.2f}')
plt.axvline(median_x, color='green', linestyle=':', linewidth=2,
            label=f'Median = {median_x:.2f}')

# Shade area for P(X > 3)
x_shade = x[x >= 3]
y_shade  = dist.pdf(x_shade)
plt.fill_between(x_shade, y_shade, alpha=0.2, color='red',
                 label=f'P(X > 3) = {prob2:.2f}')

plt.xlabel('x', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title(r'Exponential Distribution, $\lambda = 0.5$', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
