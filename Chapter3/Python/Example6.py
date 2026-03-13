# Chapter 3 - Binomial Distribution
# Example 6: Customer Satisfaction Survey — Event Analysis  B(20, 0.65)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from matplotlib.patches import Rectangle

# Parameters
n = 20
p = 0.65

# Events:
#   A: X >= 15  (at least 15 satisfied customers)
#   B: X <= 17  (at most 17 satisfied customers)
#   A ∩ B: 15 <= X <= 17

# i. Calculate probabilities
prob_A       = 1 - binom.cdf(14, n, p)
prob_B       = binom.cdf(17, n, p)
prob_A_and_B = binom.cdf(17, n, p) - binom.cdf(14, n, p)
prob_A_or_B  = prob_A + prob_B - prob_A_and_B

print("i. Probabilities:")
print(f"   P(A) = P(X >= 15)       = {prob_A:.4f}")
print(f"   P(B) = P(X <= 17)       = {prob_B:.4f}")
print(f"   P(A ∩ B) = P(15<=X<=17) = {prob_A_and_B:.4f}")
print(f"   P(A ∪ B)                = {prob_A_or_B:.4f}")

# ii. Conditional probability P(A|B)
prob_A_given_B = prob_A_and_B / prob_B
print(f"\nii. P(A|B) = {prob_A_given_B:.4f}")
print("    Interpretation: Given that at most 17 customers are satisfied,")
print(f"    there is a {prob_A_given_B*100:.2f}% probability that at least 15 are satisfied.")

# iii. Test independence
prob_A_times_B = prob_A * prob_B
is_independent  = abs(prob_A_and_B - prob_A_times_B) < 0.0001

print(f"\niii. Independence test:")
print(f"     P(A ∩ B)   = {prob_A_and_B:.4f}")
print(f"     P(A)·P(B)  = {prob_A_times_B:.4f}")
print(f"     Events A and B are {'independent' if is_independent else 'NOT independent'}")

# iv. Visualization
x   = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Bar plot with highlighted regions
axes[0].bar(x, pmf, color='lightgray', edgecolor='black', alpha=0.7)
axes[0].add_patch(Rectangle((-0.5, 0), 15,      max(pmf)*1.1, facecolor='blue',   alpha=0.1))
axes[0].add_patch(Rectangle((14.5, 0), 3,       max(pmf)*1.1, facecolor='purple', alpha=0.2))
axes[0].add_patch(Rectangle((17.5, 0), n-17.5,  max(pmf)*1.1, facecolor='red',    alpha=0.1))
axes[0].set_xlabel('Number of Satisfied Customers (X)', fontsize=11)
axes[0].set_ylabel('Probability', fontsize=11)
axes[0].set_title('Events A and B on Binomial Distribution', fontsize=12)
axes[0].legend(['B only (X<=14)', 'A∩B (15<=X<=17)', 'A only (X>=18)'],
               loc='upper left', fontsize=9)
axes[0].grid(axis='y', alpha=0.3)

# Probability summary
region_probs  = [prob_A_and_B,
                 prob_A - prob_A_and_B,
                 prob_B - prob_A_and_B,
                 1 - prob_A_or_B]
region_labels = ['A∩B', 'A only', 'B only', 'Neither']
colors        = ['purple', 'red', 'blue', 'lightgray']
alphas        = [0.5, 0.3, 0.3, 0.7]

bars = axes[1].bar(region_labels, region_probs, color=colors, alpha=alphas, edgecolor='black')
axes[1].set_ylabel('Probability', fontsize=11)
axes[1].set_title('Probability Regions', fontsize=12)
axes[1].set_ylim(0, max(region_probs) * 1.2)

for bar, prob in zip(bars, region_probs):
    axes[1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.01,
                 f'{prob:.4f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
