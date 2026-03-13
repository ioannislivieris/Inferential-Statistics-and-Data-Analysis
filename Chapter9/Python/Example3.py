# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 3: Στρωματοποιημένη Δειγματοληψία
#   N=1000 υπάλληλοι, 4 τμήματα, n=100

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

np.random.seed(456)

# Create a population with strata defined by departments
population = pd.DataFrame({
    'ID':           range(1, 1001),
    'Department':   np.random.choice(['Sales', 'IT', 'HR', 'Finance'],
                                     1000, p=[0.4, 0.3, 0.2, 0.1]),
    'Satisfaction': np.random.normal(7, 1.5, 1000)
})

# Display the department distribution in the population
print("Department distribution in population:")
print(population['Department'].value_counts())

# Perform proportional stratified sampling
sample_size = 100
sampling_fraction = sample_size / len(population)

stratified_sample = population.groupby('Department',
                                       group_keys=False).apply(
    lambda x: x.sample(frac=sampling_fraction, random_state=456)
)

# Display sample size per department (should be proportional)
print("\nSample size per department:")
print(stratified_sample['Department'].value_counts())

# Perform simple random sampling for comparison
srs_sample = population.sample(n=sample_size, random_state=456)

# Compare results from both sampling methods
print("\n--- Comparison of Sampling Methods ---")
print(f"Stratified sampling - Mean satisfaction score: "
      f"{stratified_sample['Satisfaction'].mean():.2f}")
print(f"Simple random sampling - Mean satisfaction score: "
      f"{srs_sample['Satisfaction'].mean():.2f}")
print(f"Population - True mean satisfaction score: "
      f"{population['Satisfaction'].mean():.2f}")

# Alternative: use scikit-learn stratified split
stratified_sample_sk, _ = train_test_split(
    population,
    train_size=sample_size,
    stratify=population['Department'],
    random_state=456
)
print(f"\nScikit-learn stratified sample mean: "
      f"{stratified_sample_sk['Satisfaction'].mean():.2f}")
