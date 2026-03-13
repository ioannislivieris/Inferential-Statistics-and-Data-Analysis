# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 6: Σύγκριση Κατανομών χ² (df = 2, 5, 10, 15)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Compare chi-square distributions with different degrees of freedom
x = np.linspace(0, 30, 1000)

# Calculate densities
y_chi2  = chi2.pdf(x, df=2)
y_chi5  = chi2.pdf(x, df=5)
y_chi10 = chi2.pdf(x, df=10)
y_chi15 = chi2.pdf(x, df=15)

# Plot
plt.figure(figsize=(12, 7))
plt.plot(x, y_chi2,  'r-',      linewidth=2, label=r'$\chi^2(2)$')
plt.plot(x, y_chi5,  'b-',      linewidth=2, label=r'$\chi^2(5)$')
plt.plot(x, y_chi10, 'g-',      linewidth=2, label=r'$\chi^2(10)$')
plt.plot(x, y_chi15, 'purple',  linewidth=2, label=r'$\chi^2(15)$')

# Mark means
plt.axvline(2,  color='red',    linestyle=':', alpha=0.5)
plt.axvline(5,  color='blue',   linestyle=':', alpha=0.5)
plt.axvline(10, color='green',  linestyle=':', alpha=0.5)
plt.axvline(15, color='purple', linestyle=':', alpha=0.5)

plt.xlabel(r'$\chi^2$', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title(r'$\chi^2$-Distributions with Different Degrees of Freedom',
          fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)

# Add text annotation
plt.text(20, max(y_chi2) * 0.9,
         r'Mean = $\nu$, Var = $2\nu$',
         fontsize=10,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
