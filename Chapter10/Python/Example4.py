# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 4: Σύγκριση Θεωρητικού και Εμπειρικού Τυπικού Σφάλματος
#   N(100, 20), n = 5..200, 1000 προσομοιώσεις

import numpy as np
import matplotlib.pyplot as plt

# Population parameters
mu    = 100
sigma = 20

# Sample sizes to test
sample_sizes = np.arange(5, 201, 5)

# Calculate theoretical standard errors
theoretical_se = sigma / np.sqrt(sample_sizes)

# Simulate empirical standard errors
np.random.seed(42)
n_simulations = 1000
empirical_se  = []

for n in sample_sizes:
    sample_means = [np.mean(np.random.normal(mu, sigma, n))
                    for _ in range(n_simulations)]
    empirical_se.append(np.std(sample_means, ddof=1))

# Plot
plt.figure(figsize=(12, 7))
plt.plot(sample_sizes, theoretical_se, 'b-', linewidth=2,
         label=r'Theoretical SE = $\sigma/\sqrt{n}$')
plt.scatter(sample_sizes, empirical_se, c='red', s=20, alpha=0.6,
            label='Empirical SE (simulated)')

plt.xlabel('Sample Size (n)', fontsize=12)
plt.ylabel('Standard Error', fontsize=12)
plt.title('Standard Error vs Sample Size', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)

plt.text(150, theoretical_se[0] * 0.8,
         r'$SE = \frac{\sigma}{\sqrt{n}}$',
         fontsize=16, color='blue')

plt.tight_layout()
plt.show()

# Demonstrate 4x sample size for halving SE
print("To reduce SE by half, 4x sample size is needed:")
print(f"  n = 10 -> SE = {sigma / np.sqrt(10):.2f}")
print(f"  n = 40 -> SE = {sigma / np.sqrt(40):.2f}")
