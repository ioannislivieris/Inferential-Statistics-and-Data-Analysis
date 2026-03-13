# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 1: Υπολογισμός Δειγματικών Στατιστικών
#   n=10 μισθοί (χιλιάδες ευρώ)
#   Note: numpy var/std use ddof=1 for sample (Bessel's correction)

import numpy as np
import pandas as pd

# Create a sample of salaries for 10 employees (in thousands of euros)
salaries = np.array([28, 32, 35, 29, 41, 33, 30, 27, 38, 31])

# Calculate the sample size (number of observations)
n = len(salaries)
print(f"Sample size (number of employees): {n}")

# Calculate the sample mean (average salary)
x_bar = np.mean(salaries)
print(f"Sample mean (x): {x_bar:.2f} thousand Euros")

# Calculate the sample variance with Bessel's correction (ddof=1)
s_squared = np.var(salaries, ddof=1)
print(f"Sample variance (s^2): {s_squared:.2f}")

# Calculate the sample standard deviation (square root of variance)
s = np.std(salaries, ddof=1)
print(f"Sample standard deviation (s): {s:.2f} thousand Euros")

# Calculate the median (middle value when sorted)
median_salary = np.median(salaries)
print(f"Sample median: {median_salary:.2f} thousand Euros")

# Alternative approach using pandas for comprehensive descriptive statistics
df = pd.DataFrame({'Salary': salaries})
print("\nComprehensive descriptive statistics:")
print(df.describe())
