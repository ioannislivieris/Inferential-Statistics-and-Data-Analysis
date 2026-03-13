# Chapter 6 - Κανονική Κατανομή
# Example 3: Οπτικοποίηση Κατανομής  X ~ N(70, 12²)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 70
sigma = 12

# x values
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, loc=mu, scale=sigma)

# Plot
plt.figure(figsize=(12, 7))
plt.plot(x, y, 'b-', linewidth=2, label='PDF')

# Mean line
plt.axvline(mu, color='red', linestyle='--',
            linewidth=2, label='Mean')

# Standard deviation lines
plt.axvline(mu - sigma, color='orange', linestyle=':',
            linewidth=1.5, label='+-1 SD (68%)')
plt.axvline(mu + sigma, color='orange', linestyle=':',
            linewidth=1.5)
plt.axvline(mu - 2*sigma, color='green', linestyle=':',
            linewidth=1.5, label='+-2 SD (95%)')
plt.axvline(mu + 2*sigma, color='green', linestyle=':',
            linewidth=1.5)

# Fill areas
plt.fill_between(x, y,
                 where=(x >= mu - sigma) & (x <= mu + sigma),
                 alpha=0.2, color='orange')
plt.fill_between(x, y,
                 where=(x >= mu - 2*sigma) & (x <= mu + 2*sigma),
                 alpha=0.1, color='green')

plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title(f'Normal Distribution N({mu}, {sigma}\u00b2)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
