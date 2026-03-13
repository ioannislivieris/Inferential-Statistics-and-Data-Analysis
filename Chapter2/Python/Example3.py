# Chapter 2 - Sampling Methods and Basic Concepts
# Example 3: Portfolio Analysis

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set seed for reproducibility
np.random.seed(123)
n_periods = 100

# Stock A: mean 8%, sd 15%
returns_a = np.random.normal(8, 15, n_periods)

# Stock B: mean 12%, sd 20%
returns_b = np.random.normal(12, 20, n_periods)

# Portfolio weights
weight_a = 0.6
weight_b = 0.4

# Portfolio returns
portfolio_returns = weight_a * returns_a + weight_b * returns_b

# Calculate statistics
print("Stock A:")
print(f"  Mean Return: {np.mean(returns_a):.2f}%")
print(f"  Std Dev:     {np.std(returns_a, ddof=1):.2f}%\n")

print("Stock B:")
print(f"  Mean Return: {np.mean(returns_b):.2f}%")
print(f"  Std Dev:     {np.std(returns_b, ddof=1):.2f}%\n")

print("Portfolio (60% A, 40% B):")
print(f"  Mean Return: {np.mean(portfolio_returns):.2f}%")
print(f"  Std Dev:     {np.std(portfolio_returns, ddof=1):.2f}%")

# Correlation
correlation = np.corrcoef(returns_a, returns_b)[0, 1]
print(f"  Correlation: {correlation:.3f}")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].hist(returns_a, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Stock A Returns')
axes[0, 0].set_xlabel('Return (%)')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].hist(returns_b, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Stock B Returns')
axes[0, 1].set_xlabel('Return (%)')
axes[0, 1].set_ylabel('Frequency')

axes[1, 0].hist(portfolio_returns, bins=20, color='lightgreen',
                edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Portfolio Returns')
axes[1, 0].set_xlabel('Return (%)')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].scatter(returns_a, returns_b, color='darkblue', alpha=0.6)
slope, intercept, _, _, _ = stats.linregress(returns_a, returns_b)
line = slope * returns_a + intercept
axes[1, 1].plot(returns_a, line, color='red', linewidth=2)
axes[1, 1].set_title('Scatter Plot: A vs B')
axes[1, 1].set_xlabel('Stock A Return (%)')
axes[1, 1].set_ylabel('Stock B Return (%)')

plt.tight_layout()
plt.show()
