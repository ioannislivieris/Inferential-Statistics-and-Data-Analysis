# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 2: Απλή Τυχαία Δειγματοληψία
#   N=500 υπάλληλοι, n=50 δείγμα

import numpy as np
import pandas as pd

# Set seed for reproducibility of random results
np.random.seed(123)

# Create population: Employee IDs numbered from 1 to 500
population = np.arange(1, 501)

# Perform simple random sampling without replacement
sample_size = 50
simple_random_sample = np.random.choice(population,
                                        size=sample_size,
                                        replace=False)

# Display the first 10 selected employee IDs
print("First 10 selected employees:")
print(simple_random_sample[:10])

# Create a DataFrame with employee characteristics
employees = pd.DataFrame({
    'ID':         range(1, 501),
    'Age':        np.random.randint(22, 66, 500),
    'Salary':     np.random.normal(35000, 8000, 500),
    'Department': np.random.choice(['Sales', 'IT', 'HR', 'Finance'], 500)
})

# Perform simple random sampling using pandas
srs_sample = employees.sample(n=50, random_state=123)

# Calculate and display sample statistics
print(f"\nSample mean age: {srs_sample['Age'].mean():.1f} years")
print(f"Sample mean salary: {srs_sample['Salary'].mean():.2f} Euros")
print(f"\nDepartment distribution in the sample:")
print(srs_sample['Department'].value_counts())
