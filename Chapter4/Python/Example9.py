# Chapter 4 - Poisson Distribution
# Example 9: Defect Analysis — Multiple Production Lines & Bayes
#   Line A (30%): Poisson(2)
#   Line B (45%): Poisson(3)
#   Line C (25%): Poisson(5)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameters
lambda_A = 2;  lambda_B = 3;  lambda_C = 5
p_A      = 0.30; p_B = 0.45; p_C = 0.25

print("=== Defects Analysis Multiple Lines ===\n")

# i. P(E1 ∪ E2) where E1={X>=4}, E2={X<=3}
# Note: E1 and E2 are complementary → P(E1 ∪ E2) = 1
prob_ge4_A = 1 - poisson.cdf(3, lambda_A)
prob_ge4_B = 1 - poisson.cdf(3, lambda_B)
prob_ge4_C = 1 - poisson.cdf(3, lambda_C)
prob_ge4   = prob_ge4_A * p_A + prob_ge4_B * p_B + prob_ge4_C * p_C

print("i. Union of events:")
print(f"   P(X >= 4|A) = {prob_ge4_A:.4f}")
print(f"   P(X >= 4|B) = {prob_ge4_B:.4f}")
print(f"   P(X >= 4|C) = {prob_ge4_C:.4f}")
print(f"   P(X >= 4)   = {prob_ge4:.4f}")
print(f"   P(X <= 3)   = {1 - prob_ge4:.4f}")
print(f"   P(E1 ∪ E2)  = {prob_ge4 + (1 - prob_ge4):.4f}\n")

# ii. P(Line C | X = 4) — Bayes' Theorem
prob_4_A = poisson.pmf(4, lambda_A)
prob_4_B = poisson.pmf(4, lambda_B)
prob_4_C = poisson.pmf(4, lambda_C)
prob_4   = prob_4_A * p_A + prob_4_B * p_B + prob_4_C * p_C

prob_C_given_4 = (prob_4_C * p_C) / prob_4

print("ii. Bayes' Theorem:")
print(f"   P(X=4|A)   = {prob_4_A:.4f}")
print(f"   P(X=4|B)   = {prob_4_B:.4f}")
print(f"   P(X=4|C)   = {prob_4_C:.4f}")
print(f"   P(X=4)     = {prob_4:.4f}")
print(f"   P(C|X=4)   = {prob_C_given_4:.4f}\n")

# iii. P(X=2 and all from A)
prob_2_A     = poisson.pmf(2, lambda_A)
prob_2_all_A = prob_2_A * p_A
prob_2       = (poisson.pmf(2, lambda_A)*p_A +
                poisson.pmf(2, lambda_B)*p_B +
                poisson.pmf(2, lambda_C)*p_C)

print("iii. Poisson combined with binomial:")
print(f"   P(X=2|A)              = {prob_2_A:.4f}")
print(f"   P(X=2)                = {prob_2:.4f}")
print(f"   P(X=2 and all from A) = {prob_2_all_A:.4f}\n")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

x_vals     = np.arange(0, 13)
colors     = ['blue', 'darkgreen', 'red']
line_names = ['Line A', 'Line B', 'Line C']
lambdas    = [lambda_A, lambda_B, lambda_C]

for i in range(3):
    row, col = divmod(i, 2)
    axes[row, col].stem(x_vals, poisson.pmf(x_vals, lambdas[i]),
                        basefmt=' ', linefmt=colors[i],
                        markerfmt=colors[i] + 'o')
    axes[row, col].axvline(lambdas[i], color='orange', linestyle='--', linewidth=2)
    axes[row, col].set_xlabel('Defects')
    axes[row, col].set_ylabel('Probability')
    axes[row, col].set_title(f'{line_names[i]}: Poisson({lambdas[i]})')
    axes[row, col].grid(alpha=0.3)

for i, (lam, col, name) in enumerate(zip(lambdas, colors,
                                          ['A (λ=2)', 'B (λ=3)', 'C (λ=5)'])):
    axes[1, 1].plot(x_vals, poisson.pmf(x_vals, lam), 'o-',
                    color=col, linewidth=2, label=name)

axes[1, 1].set_xlabel('Defects')
axes[1, 1].set_ylabel('Probability')
axes[1, 1].set_title('Production Lines Comparison')
axes[1, 1].legend()
axes[1, 1].grid(alpha=0.3)
axes[1, 1].set_ylim([0, 0.3])

plt.tight_layout()
plt.show()

# Summary table
print("\n=== Results Table ===")
print("k\tP(X=k|A)\tP(X=k|B)\tP(X=k|C)\tP(X=k)")
print("-" * 65)
for k in range(9):
    pa = poisson.pmf(k, lambda_A)
    pb = poisson.pmf(k, lambda_B)
    pc = poisson.pmf(k, lambda_C)
    pk = pa*p_A + pb*p_B + pc*p_C
    print(f"{k}\t{pa:.4f}\t\t{pb:.4f}\t\t{pc:.4f}\t\t{pk:.4f}")
