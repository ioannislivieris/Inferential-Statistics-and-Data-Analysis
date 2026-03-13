# Chapter 6 - Κανονική Κατανομή
# Example 4: Προσομοίωση και Επαλήθευση  X ~ N(100, 15²), n = 10.000

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu    = 100
sigma = 15
n     = 10000

# Simulation
np.random.seed(42)
samples = norm.rvs(loc=mu, scale=sigma, size=n)

# Verify empirical rule
within_1sd = np.sum((samples >= mu - sigma) &
                    (samples <= mu + sigma)) / n
within_2sd = np.sum((samples >= mu - 2*sigma) &
                    (samples <= mu + 2*sigma)) / n
within_3sd = np.sum((samples >= mu - 3*sigma) &
                    (samples <= mu + 3*sigma)) / n

print("Empirical Rule Verification:")
print(f"Within 1 SD: {within_1sd*100:.2f}% (Expected: 68%)")
print(f"Within 2 SD: {within_2sd*100:.2f}% (Expected: 95%)")
print(f"Within 3 SD: {within_3sd*100:.2f}% (Expected: 99.7%)")

# Summary statistics
print(f"\nSample Mean: {np.mean(samples):.2f} (True: {mu})")
print(f"Sample SD: {np.std(samples, ddof=1):.2f} (True: {sigma})")

# Histogram with overlay
plt.figure(figsize=(12, 7))
plt.hist(samples, bins=50, density=True, alpha=0.6,
         color='blue', edgecolor='black',
         label='Simulated Data')

# Theoretical density curve
x_theory = np.linspace(samples.min(), samples.max(), 200)
y_theory  = norm.pdf(x_theory, loc=mu, scale=sigma)
plt.plot(x_theory, y_theory, 'r-', linewidth=2,
         label='Theoretical Density')

plt.xlabel('x', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title(f'Simulation: N({mu}, {sigma}\u00b2)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
