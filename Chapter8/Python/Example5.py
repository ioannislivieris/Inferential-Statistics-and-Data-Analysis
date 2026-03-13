# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 5: Σύγκριση Κατανομών t (df = 3, 10, 30) vs N(0,1)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

# Compare t-distributions with different degrees of freedom
x = np.linspace(-4, 4, 1000)

# Calculate densities
y_norm = norm.pdf(x)
y_t3   = t.pdf(x, df=3)
y_t10  = t.pdf(x, df=10)
y_t30  = t.pdf(x, df=30)

# Plot
plt.figure(figsize=(12, 7))
plt.plot(x, y_norm, 'k-', linewidth=2, label='N(0,1)')
plt.plot(x, y_t3,   'r-', linewidth=2, label='t(3)')
plt.plot(x, y_t10,  'b-', linewidth=2, label='t(10)')
plt.plot(x, y_t30,  'g-', linewidth=2, label='t(30)')

plt.xlabel('t', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('t-Distributions with Different Degrees of Freedom',
          fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)

# Add text annotation
plt.text(0, max(y_norm) * 0.9,
         'As df increases,\nt approaches N(0,1)',
         ha='center', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
