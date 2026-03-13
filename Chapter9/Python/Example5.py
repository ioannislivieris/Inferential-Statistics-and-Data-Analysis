# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 5: Προσομοίωση Δειγματοληπτικού Σφάλματος
#   N=10000, μ=100, σ=15, n=30, 1000 δείγματα

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(100)

# Create a large population with known parameters
population_mean = 100
population_sd   = 15
N               = 10000

population = np.random.normal(population_mean, population_sd, N)

# Calculate actual population parameters
mu    = population.mean()
sigma = population.std(ddof=1)

print("Population parameters:")
print(f"  True mean (mu) = {mu:.2f}")
print(f"  True standard deviation (sigma) = {sigma:.2f}\n")

# Simulation: Draw many samples and calculate their means
num_samples = 1000  # Number of samples to draw
sample_size = 30    # Size of each sample
sample_means = []

for i in range(num_samples):
    sample_data = np.random.choice(population, sample_size, replace=False)
    sample_means.append(sample_data.mean())

sample_means = np.array(sample_means)

# Analyse the distribution of sample means
print("Sampling distribution statistics:")
print(f"  Mean of sample means: {sample_means.mean():.2f} "
      f"(theoretical: mu = {mu:.2f})")
print(f"  Standard deviation of sample means: {sample_means.std(ddof=1):.2f}")
print(f"  Theoretical standard error (sigma/sqrt(n)): "
      f"{sigma / np.sqrt(sample_size):.2f}")

# Create visualization of the sampling distribution
fig, ax = plt.subplots(figsize=(12, 6))

ax.hist(sample_means, bins=30, density=True,
        alpha=0.7, color='steelblue', edgecolor='black')
ax.axvline(mu, color='darkgreen', linestyle='--',
           linewidth=2, label=f'Population mu = {mu:.2f}')

# Overlay theoretical normal distribution
x             = np.linspace(sample_means.min(), sample_means.max(), 100)
theoretical_se = sigma / np.sqrt(sample_size)
ax.plot(x, stats.norm.pdf(x, mu, theoretical_se),
        'r-', linewidth=2, label='Theoretical distribution')

ax.set_xlabel('Sample Mean')
ax.set_ylabel('Density')
ax.set_title(f'Distribution of Sample Means (Sampling Distribution)\n'
             f'Sample size n = {sample_size}, '
             f'Number of samples = {num_samples}')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
