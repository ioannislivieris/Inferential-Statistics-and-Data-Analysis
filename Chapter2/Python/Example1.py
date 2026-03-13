# Chapter 2 - Sampling Methods and Basic Concepts
# Example 1: Discrete Distribution Calculations

import numpy as np
import matplotlib.pyplot as plt

# Define values and probabilities
values = np.array([10, 20, 30, 40, 50])
probs  = np.array([0.15, 0.25, 0.30, 0.20, 0.10])

# Expected value
expected_value = np.sum(values * probs)
print(f"Expected Value: {expected_value:.2f}")

# Variance
expected_x2 = np.sum(values**2 * probs)
variance     = expected_x2 - expected_value**2
print(f"Variance: {variance:.2f}")

# Standard deviation
std_dev = np.sqrt(variance)
print(f"Standard Deviation: {std_dev:.2f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(values, probs, color='steelblue', alpha=0.7,
        edgecolor='black', width=5)
plt.axvline(expected_value, color='red', linestyle='--',
            linewidth=2, label=f'E(X) = {expected_value:.2f}')
plt.xlabel('Values', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title('Probability Distribution', fontsize=14)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
