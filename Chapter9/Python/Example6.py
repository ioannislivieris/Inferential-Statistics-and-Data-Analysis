# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 6: Επίδραση Μεγέθους Δείγματος στο Τυπικό Σφάλμα
#   SE = σ/√n, σ=15

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define different sample sizes to analyze
sample_sizes  = np.array([10, 30, 50, 100, 200, 500])
population_sd = 15  # Known population standard deviation

# Calculate theoretical standard error for each sample size
standard_errors = population_sd / np.sqrt(sample_sizes)

# Create a DataFrame for analysis and visualization
df = pd.DataFrame({
    'SampleSize':    sample_sizes,
    'StandardError': standard_errors
})

print("Relationship between sample size and standard error:")
print(df)

# Create visualization showing inverse square root relationship
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(sample_sizes, standard_errors,
        'b-', linewidth=2, marker='o',
        markersize=8, markerfacecolor='red')
ax.set_xlabel('Sample Size (n)', fontsize=12)
ax.set_ylabel('Standard Error SE(x)', fontsize=12)
ax.set_title('Effect of Sample Size on Standard Error\n'
             'Standard error decreases with rate 1/sqrt(n)',
             fontsize=14)
ax.grid(True, alpha=0.3)
ax.set_xticks(sample_sizes)

plt.tight_layout()
plt.show()

# Demonstrate the inverse square root relationship
print("\nTo reduce standard error by half,",
      "we need a 4-fold increase in sample size:")
print(f"  n = 10 -> SE = {standard_errors[0]:.2f}")
print(f"  n = 40 -> SE = {population_sd / np.sqrt(40):.2f}",
      "(half of the SE at n=10)")
