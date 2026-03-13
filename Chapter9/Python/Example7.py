# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 7: Δειγματοληπτική Κατανομή — Παράδειγμα Ζαριού
#   Πληθυσμός {1..6}, n=2, 10000 επαναλήψεις

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(200)

# Define the population: outcomes of a fair six-sided die
population = np.array([1, 2, 3, 4, 5, 6])

# Calculate population parameters
pop_mean = population.mean()
pop_var  = population.var(ddof=0)   # Population variance (ddof=0)
pop_sd   = population.std(ddof=0)   # Population standard deviation

print("Population (fair die) parameters:")
print(f"  Population mean (mu) = {pop_mean}")
print(f"  Population variance (sigma^2) = {pop_var:.3f}")
print(f"  Population standard deviation (sigma) = {pop_sd:.3f}\n")

# Simulation: Roll 2 dice and calculate their mean
num_samples = 10000  # Number of simulated experiments
sample_size = 2      # Number of dice rolled each time
sample_means = []

for i in range(num_samples):
    dice_rolls = np.random.choice(population, sample_size, replace=True)
    sample_means.append(dice_rolls.mean())

sample_means = np.array(sample_means)

# Analyse the sampling distribution
print(f"Sampling distribution statistics (n = {sample_size}):")
print(f"  Mean of sample means E[x] = {sample_means.mean():.3f} "
      f"(theoretical: mu = {pop_mean})")
print(f"  Variance of sample means Var(x) = {sample_means.var(ddof=1):.3f} "
      f"(theoretical: sigma^2/n = {pop_var/sample_size:.3f})")
print(f"  Standard error SE(x) = {sample_means.std(ddof=1):.3f} "
      f"(theoretical: sigma/sqrt(n) = "
      f"{pop_sd/np.sqrt(sample_size):.3f})")

# Create side-by-side visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Population distribution
ax1.bar(population, [1]*len(population),
        color='steelblue', alpha=0.7, width=0.8)
ax1.set_xlabel('Outcome')
ax1.set_ylabel('Probability')
ax1.set_title('Population Distribution (Fair Die)')
ax1.set_xticks(population)
ax1.grid(True, alpha=0.3)

# Sampling distribution
ax2.hist(sample_means, bins=20, density=True,
         alpha=0.7, color='coral', edgecolor='black')
ax2.axvline(pop_mean, color='darkgreen',
            linestyle='--', linewidth=2, label=f'mu = {pop_mean}')
ax2.set_xlabel('Sample Mean')
ax2.set_ylabel('Density')
ax2.set_title(f'Sampling Distribution of Mean (n={sample_size})')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
