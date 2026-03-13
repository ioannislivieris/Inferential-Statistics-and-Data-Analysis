# Chapter 6 - Κανονική Κατανομή
# Example 6: Quality Control  X ~ N(25, 0.5²)
#   LSL = 24 mm,  USL = 26 mm

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu    = 25
sigma = 0.5
LSL   = 24   # Lower Specification Limit
USL   = 26   # Upper Specification Limit

# i. Percentage within specifications
prob_within_spec = norm.cdf(USL, mu, sigma) - \
                   norm.cdf(LSL, mu, sigma)
print(f"i. Percentage within specs: {prob_within_spec*100:.2f}%")

# ii. Process capability index Cp
Cp = (USL - LSL) / (6 * sigma)
print(f"\nii. Process capability Cp: {Cp:.3f}")

if Cp >= 1.33:
    print("Process is capable (Cp >= 1.33)")
elif Cp >= 1:
    print("Process is minimally capable (1 <= Cp < 1.33)")
else:
    print("Process is not capable (Cp < 1)")

# iii. Required sigma for Cp = 1.33
target_Cp      = 1.33
required_sigma = (USL - LSL) / (6 * target_Cp)
print(f"\niii. Required SD for Cp=1.33: {required_sigma:.4f} mm")
print(f"Current SD: {sigma:.4f} mm")
print(f"Reduction needed: {(1 - required_sigma/sigma)*100:.2f}%")

# Visualization
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.figure(figsize=(12, 7))
plt.plot(x, y, 'b-', linewidth=2, label='Process Distribution')

# Specification limits
plt.axvline(LSL, color='red', linestyle='--', linewidth=2,
            label='Specification Limits')
plt.axvline(USL, color='red', linestyle='--', linewidth=2)

# Shade area within specs
x_within = x[(x >= LSL) & (x <= USL)]
y_within  = norm.pdf(x_within, mu, sigma)
plt.fill_between(x_within, y_within, alpha=0.3,
                 color='green', label='Within Specs')

# Add text
plt.text(mu, max(y)*1.05, f'Cp = {Cp:.3f}',
         ha='center', fontsize=12, weight='bold')
plt.text(LSL, max(y)*0.5, f'LSL\n{LSL}mm',
         ha='right', fontsize=10)
plt.text(USL, max(y)*0.5, f'USL\n{USL}mm',
         ha='left', fontsize=10)

plt.xlabel('Diameter (mm)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Process Distribution vs Specifications', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
