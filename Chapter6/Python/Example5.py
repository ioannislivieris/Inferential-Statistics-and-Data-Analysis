# Chapter 6 - Κανονική Κατανομή
# Example 5: Σύγκριση Κατανομών
#   N(50, 5²), N(50, 10²), N(60, 5²)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# x range
x = np.linspace(20, 80, 1000)

# Three distributions
y1 = norm.pdf(x, loc=50, scale=5)
y2 = norm.pdf(x, loc=50, scale=10)
y3 = norm.pdf(x, loc=60, scale=5)

# Plot
plt.figure(figsize=(12, 7))
plt.plot(x, y1, 'b-', linewidth=2, label='N(50, 5\u00b2)')
plt.plot(x, y2, 'r-', linewidth=2, label='N(50, 10\u00b2)')
plt.plot(x, y3, 'g-', linewidth=2, label='N(60, 5\u00b2)')

plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Comparison of Normal Distributions', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
