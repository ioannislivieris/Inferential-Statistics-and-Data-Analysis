# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 4: Επαλήθευση Εμπειρικού Κανόνα (68-95-99.7)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Calculate exact probabilities
prob_1sd = norm.cdf(1) - norm.cdf(-1)
prob_2sd = norm.cdf(2) - norm.cdf(-2)
prob_3sd = norm.cdf(3) - norm.cdf(-3)

# Display results
print("Empirical Rule Verification:")
print(f"Within +/-1 SD: {prob_1sd:.4f} ({prob_1sd*100:.2f}%) "
      f"[Expected: 68%]")
print(f"Within +/-2 SD: {prob_2sd:.4f} ({prob_2sd*100:.2f}%) "
      f"[Expected: 95%]")
print(f"Within +/-3 SD: {prob_3sd:.4f} ({prob_3sd*100:.2f}%) "
      f"[Expected: 99.7%]")

# Create visualization
z = np.linspace(-4, 4, 1000)
y = norm.pdf(z)

plt.figure(figsize=(12, 7))
plt.plot(z, y, 'b-', linewidth=2)

# Shade regions
regions = [
    ((-1, 1), 'red',   '68.27%'),
    ((-2, 2), 'green', '95.45%'),
    ((-3, 3), 'blue',  '99.73%')
]

for (lower, upper), color, label in regions:
    z_region = z[(z >= lower) & (z <= upper)]
    y_region = norm.pdf(z_region)
    plt.fill_between(z_region, y_region, alpha=0.2,
                     color=color, label=f'Within: {label}')

# Add vertical lines
for i in range(-3, 4):
    plt.axvline(i, linestyle='--', color='gray', alpha=0.5)

plt.xlabel('Standard Deviations from Mean', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Empirical Rule Visualization', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
