# Chapter 4 - Poisson Distribution
# Example 8: Call Center — Two Departments & Additive Property + Bayes
#   X ~ Poisson(4)  Technical Support
#   Y ~ Poisson(6)  Sales
#   X + Y ~ Poisson(10)  (additive property)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameters
lambda_tech  = 4    # Technical Support
lambda_sales = 6    # Sales

print("=== Call Center Analysis ===\n")

# i. P(Total = 8) using additive property
lambda_total = lambda_tech + lambda_sales   # = 10
prob_total_8 = poisson.pmf(8, lambda_total)
print(f"i. P(Total = 8 calls) = {prob_total_8:.4f}\n")

# ii. Conditional probability P(Tech=3 | Total=8)
k_values    = np.arange(0, 9)
probs_joint = np.array([
    poisson.pmf(k, lambda_tech) * poisson.pmf(8 - k, lambda_sales)
    for k in k_values
])

prob_tech_3_given_8 = probs_joint[3] / np.sum(probs_joint)
print(f"ii. P(Tech=3 | Total=8) = {prob_tech_3_given_8:.4f}\n")
print(f"    Verification: sum(joint probs) = {np.sum(probs_joint):.4f}")
print(f"    (should equal P(Total=8) = {prob_total_8:.4f})\n")

# iii. P(Total >= 10)
prob_at_least_10 = 1 - poisson.cdf(9, lambda_total)
print(f"iii. P(Total >= 10 calls) = {prob_at_least_10:.4f}\n")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

x_tech = np.arange(0, 16)
axes[0, 0].stem(x_tech, poisson.pmf(x_tech, lambda_tech),
                basefmt=' ', linefmt='blue', markerfmt='bo')
axes[0, 0].axvline(lambda_tech, color='red', linestyle='--', linewidth=2)
axes[0, 0].set_xlabel('Number of Calls')
axes[0, 0].set_ylabel('Probability')
axes[0, 0].set_title(f'Technical Support\nPoisson({lambda_tech})')
axes[0, 0].grid(alpha=0.3)

x_sales = np.arange(0, 21)
axes[0, 1].stem(x_sales, poisson.pmf(x_sales, lambda_sales),
                basefmt=' ', linefmt='darkgreen', markerfmt='go')
axes[0, 1].axvline(lambda_sales, color='red', linestyle='--', linewidth=2)
axes[0, 1].set_xlabel('Number of Calls')
axes[0, 1].set_ylabel('Probability')
axes[0, 1].set_title(f'Sales\nPoisson({lambda_sales})')
axes[0, 1].grid(alpha=0.3)

x_total = np.arange(0, 26)
axes[1, 0].stem(x_total, poisson.pmf(x_total, lambda_total),
                basefmt=' ', linefmt='purple', markerfmt='mo')
axes[1, 0].axvline(lambda_total, color='red',    linestyle='--', linewidth=2, label='Mean')
axes[1, 0].axvline(8,            color='orange', linestyle=':',  linewidth=2, label='Total=8')
axes[1, 0].set_xlabel('Number of Calls')
axes[1, 0].set_ylabel('Probability')
axes[1, 0].set_title(f'Total Calls\nPoisson({lambda_total})')
axes[1, 0].legend()
axes[1, 0].grid(alpha=0.3)

conditional_probs = probs_joint / np.sum(probs_joint)
axes[1, 1].bar(k_values, conditional_probs, color='coral', edgecolor='black', alpha=0.7)
axes[1, 1].axvline(3, color='blue', linestyle='--', linewidth=2)
axes[1, 1].set_xlabel('Technical Calls (k)')
axes[1, 1].set_ylabel('P(Tech=k | Total=8)')
axes[1, 1].set_title('Conditional Distribution\nP(Tech=k | Total=8)')
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Results table
print("\n=== Conditional Probabilities Table ===")
print("k\tP(Tech=k, Sales=8-k)\tP(Tech=k | Total=8)")
print("-" * 60)
for k in k_values:
    print(f"{k}\t{probs_joint[k]:.6f}\t\t{conditional_probs[k]:.4f}")
