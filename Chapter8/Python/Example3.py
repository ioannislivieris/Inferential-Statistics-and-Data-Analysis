# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 3: Κατανομή t Student  T ~ t(10)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

# Degrees of freedom
df = 10

# i. P(T <= 1.5)
prob1 = t.cdf(1.5, df)
print(f"P(T <= 1.5) = {prob1:.4f}")

# ii. P(-2 < T < 2)
prob2 = t.cdf(2, df) - t.cdf(-2, df)
print(f"P(-2 < T < 2) = {prob2:.4f}")

# iii. Critical value t_{0.025, 10}
t_critical = t.ppf(0.975, df)
print(f"t_{{0.025, 10}} = {t_critical:.4f}")

# Compare with standard normal
z_critical = norm.ppf(0.975)
print(f"z_{{0.025}} = {z_critical:.4f} (for comparison)")

# Visualization: Compare t(10) with standard normal
x      = np.linspace(-4, 4, 1000)
y_t    = t.pdf(x, df)
y_norm = norm.pdf(x)

plt.figure(figsize=(12, 7))
plt.plot(x, y_t,   'b-',  linewidth=2, label=f't({df})')
plt.plot(x, y_norm,'r--', linewidth=2, label='N(0,1)')

# Mark critical values
plt.axvline(-t_critical, color='blue', linestyle=':', linewidth=1.5, alpha=0.7)
plt.axvline( t_critical, color='blue', linestyle=':', linewidth=1.5, alpha=0.7,
             label=f't critical = +-{t_critical:.2f}')
plt.axvline(-z_critical, color='red', linestyle=':', linewidth=1.5, alpha=0.7)
plt.axvline( z_critical, color='red', linestyle=':', linewidth=1.5, alpha=0.7,
             label=f'z critical = +-{z_critical:.2f}')

# Shade 95% area for t
x_shade = x[(x >= -t_critical) & (x <= t_critical)]
y_shade  = t.pdf(x_shade, df)
plt.fill_between(x_shade, y_shade, alpha=0.2, color='blue',
                 label=f'95% for t({df})')

plt.xlabel('t', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('t-Distribution vs Standard Normal', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
