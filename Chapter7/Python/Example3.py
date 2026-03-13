# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 3: Οπτικοποίηση τυπικής κανονικής  Z ~ N(0, 1)
#   Κρίσιμες τιμές ±1.96 (95%) και ±1 (68%)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate z values
z = np.linspace(-4, 4, 1000)
y = norm.pdf(z)

# Create plot
plt.figure(figsize=(12, 7))
plt.plot(z, y, 'b-', linewidth=2, label='PDF')

# Add critical values
plt.axvline(-1.96, color='red', linestyle='--',
            linewidth=2, label='+-1.96 (95%)')
plt.axvline(1.96, color='red', linestyle='--', linewidth=2)
plt.axvline(-1, color='gray', linestyle=':',
            linewidth=1, label='+-1 (68%)')
plt.axvline(0,  color='gray', linestyle=':', linewidth=1)
plt.axvline(1,  color='gray', linestyle=':', linewidth=1)

# Shade 95% area
z_shade = z[(z >= -1.96) & (z <= 1.96)]
y_shade = norm.pdf(z_shade)
plt.fill_between(z_shade, y_shade, alpha=0.2, color='blue',
                 label='95% of data')

# Add annotations
plt.text(0, max(y) * 0.9,
         '95% of data\nbetween -1.96 and 1.96',
         ha='center', fontsize=11, color='red')
plt.text(0, max(y) * 0.5, r'$\mu = 0$',
         ha='center', fontsize=13)
plt.text(2, max(y) * 0.3, r'$\sigma = 1$',
         ha='center', fontsize=13)

plt.xlabel('z', fontsize=12)
plt.ylabel(r'$\phi(z)$', fontsize=12)
plt.title('Standard Normal Distribution', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
