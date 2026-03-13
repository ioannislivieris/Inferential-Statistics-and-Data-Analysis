# Chapter 2 - Sampling Methods and Basic Concepts
# Example 2: Bayes' Theorem Simulation (Monte Carlo)

import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Simulation parameters
n_simulations = 100000

# Factory probabilities and names
factory_probs = np.array([0.50, 0.30, 0.20])
factory_names = ['A', 'B', 'C']

# Defect probabilities per factory
defect_probs = np.array([0.02, 0.03, 0.04])

# Simulate factory selection
factories = np.random.choice(factory_names, n_simulations, p=factory_probs)

# Simulate defects
defects = np.zeros(n_simulations, dtype=int)
for i in range(n_simulations):
    factory_idx = factory_names.index(factories[i])
    defects[i]  = np.random.binomial(1, defect_probs[factory_idx])

# Calculate probabilities
total_defective = np.sum(defects)
p_defective     = total_defective / n_simulations

print(f"P(Defective) simulation:   {p_defective:.4f}")
print(f"P(Defective) theoretical:  {np.sum(factory_probs * defect_probs):.4f}\n")

# Bayes' Theorem: P(Factory C | Defective)
defective_from_c    = np.sum((defects == 1) & (factories == 'C'))
p_c_given_defective = defective_from_c / total_defective

print(f"P(Factory C | Defective) simulation:  {p_c_given_defective:.4f}")
print(f"P(Factory C | Defective) theoretical: {(0.20 * 0.04) / 0.027:.4f}")

# Visualization
defective_factories = factories[defects == 1]
unique, counts      = np.unique(defective_factories, return_counts=True)
proportions         = counts / len(defective_factories)

plt.figure(figsize=(10, 6))
plt.bar(unique, proportions, color='coral', alpha=0.7, edgecolor='black')
plt.xlabel('Factory', fontsize=12)
plt.ylabel('Proportion', fontsize=12)
plt.title('Distribution of Defectives by Factory', fontsize=14)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
