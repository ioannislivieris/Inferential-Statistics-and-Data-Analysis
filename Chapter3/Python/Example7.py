# Chapter 3 - Binomial Distribution
# Example 7: Comparing Two Production Lines  A~B(50,0.08), B~B(60,0.05)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n_A, p_A = 50, 0.08
n_B, p_B = 60, 0.05

# i. P(X_A = 4 and X_B = 3)  — independent lines
prob_A_4  = binom.pmf(4, n_A, p_A)
prob_B_3  = binom.pmf(3, n_B, p_B)
prob_both = prob_A_4 * prob_B_3
print(f"i. P(X_A=4 and X_B=3) = {prob_both:.6f}")

# ii. P(X_A > 5 or X_B > 5)
prob_A_gt5    = 1 - binom.cdf(5, n_A, p_A)
prob_B_gt5    = 1 - binom.cdf(5, n_B, p_B)
prob_both_gt5 = prob_A_gt5 * prob_B_gt5
prob_union    = prob_A_gt5 + prob_B_gt5 - prob_both_gt5
print(f"\nii. P(X_A>5 or X_B>5) = {prob_union:.6f}")
print(f"    P(X_A>5) = {prob_A_gt5:.6f}")
print(f"    P(X_B>5) = {prob_B_gt5:.6f}")

# iii. Expected total defects and standard deviation
mean_A = n_A * p_A;  mean_B = n_B * p_B
var_A  = n_A * p_A * (1 - p_A);  var_B = n_B * p_B * (1 - p_B)
mean_total = mean_A + mean_B
sd_total   = np.sqrt(var_A + var_B)

print(f"\niii. Expected defects:")
print(f"     Line A: {mean_A:.2f}")
print(f"     Line B: {mean_B:.2f}")
print(f"     Total:  {mean_total:.2f}")
print(f"     Std Dev: {sd_total:.2f}")

# iv. Comparison plots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

x_A   = np.arange(0, n_A + 1)
pmf_A = binom.pmf(x_A, n_A, p_A)
axes[0].bar(x_A, pmf_A, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].axvline(mean_A, color='red', linestyle='--', linewidth=2,
                label=f'Mean = {mean_A:.2f}')
axes[0].set_xlabel('Number of Defects', fontsize=11)
axes[0].set_ylabel('Probability', fontsize=11)
axes[0].set_title(f'Line A: B({n_A}, {p_A})', fontsize=12)
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

x_B   = np.arange(0, n_B + 1)
pmf_B = binom.pmf(x_B, n_B, p_B)
axes[1].bar(x_B, pmf_B, color='coral', alpha=0.7, edgecolor='black')
axes[1].axvline(mean_B, color='red', linestyle='--', linewidth=2,
                label=f'Mean = {mean_B:.2f}')
axes[1].set_xlabel('Number of Defects', fontsize=11)
axes[1].set_ylabel('Probability', fontsize=11)
axes[1].set_title(f'Line B: B({n_B}, {p_B})', fontsize=12)
axes[1].legend()
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# Overlay comparison
plt.figure(figsize=(12, 6))
plt.plot(x_A, pmf_A, 'o-', color='steelblue', linewidth=2,
         markersize=6, label=f'Line A: B({n_A}, {p_A})')
plt.plot(x_B, pmf_B, 's-', color='coral', linewidth=2,
         markersize=6, label=f'Line B: B({n_B}, {p_B})')
plt.xlabel('Number of Defects', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title('Comparison of Two Production Lines', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
