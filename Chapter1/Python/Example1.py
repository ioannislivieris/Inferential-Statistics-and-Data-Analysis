# Chapter 1 - Introduction to Inferential Statistics
# Example 1: Basic Operations & Data Manipulation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ── Basic Arithmetic ──────────────────────────────────────────────────────────
2 + 3
10 / 2
2**3

# Creating variables
x = 5
y = 10
z = x + y

# Creating arrays
numbers = np.array([1, 2, 3, 4, 5])
names = ['Alice', 'Bob', 'Charlie']

# Basic statistics
np.mean(numbers)    # Mean
np.median(numbers)  # Median
np.std(numbers)     # Standard deviation
np.var(numbers)     # Variance

# ── DataFrame Creation & Manipulation ────────────────────────────────────────
students = pd.DataFrame({
    'Name':  ['Alice', 'Bob', 'Charlie', 'David'],
    'Age':   [20, 22, 21, 23],
    'Grade': [85, 90, 78, 92]
})

# Viewing the data
print(students)
students.head()
students.describe()

# Accessing columns
students['Name']
students['Grade']

# Basic statistics
students['Grade'].mean()
students['Age'].max()

# ── Basic Visualization ───────────────────────────────────────────────────────
data = np.array([23, 25, 28, 30, 32, 28, 26, 24, 27, 29])

plt.figure(figsize=(10, 4))

# Histogram
plt.subplot(1, 2, 1)
plt.hist(data, bins=5, color='lightblue', edgecolor='black')
plt.title('Distribution of Data')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Box plot
plt.subplot(1, 2, 2)
plt.boxplot(data)
plt.title('Box Plot of Data')
plt.ylabel('Values')

plt.tight_layout()
plt.show()

# Line plot
plt.figure(figsize=(8, 5))
x = np.arange(1, 11)
plt.plot(x, data, 'b-', linewidth=2, marker='o', markersize=8, markerfacecolor='red')
plt.title('Time Series Plot')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True, alpha=0.3)
plt.show()
