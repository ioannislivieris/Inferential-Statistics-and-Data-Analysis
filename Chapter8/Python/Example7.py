# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 7: Ανάλυση Κατανομής F — Σύγκριση Μεταβλητότητας Πωλήσεων
#   Κατάστημα Α: n1=20, s1=1200 EUR
#   Κατάστημα Β: n2=25, s2=800  EUR

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

# Data
n1, s1 = 20, 1200
n2, s2 = 25, 800

# Degrees of freedom
df1 = n1 - 1   # 19
df2 = n2 - 1   # 24

# F-statistic
F_stat = (s1**2) / (s2**2)
print(f"F-statistic: {F_stat:.4f}")
print(f"Degrees of freedom: df1 = {df1}, df2 = {df2}")

# Critical values (two-tailed, alpha = 0.05)
F_upper = f.ppf(0.975, df1, df2)
F_lower = f.ppf(0.025, df1, df2)
print(f"F_lower (0.025): {F_lower:.4f}")
print(f"F_upper (0.975): {F_upper:.4f}")
position = "inside" if (F_stat > F_upper or F_stat < F_lower) else "outside"
print(f"Observed F = {F_stat:.4f} lies {position} the critical region")

# Visualization
x = np.linspace(0, 5, 1000)
y = f.pdf(x, df1, df2)

plt.figure(figsize=(12, 7))
plt.plot(x, y, 'b-', linewidth=2, label='F distribution')

# Shade critical regions
x_upper = x[x >= F_upper]
plt.fill_between(x_upper, f.pdf(x_upper, df1, df2),
                 alpha=0.3, color='red',
                 label='Critical regions (2.5% each)')
x_lower = x[x <= F_lower]
plt.fill_between(x_lower, f.pdf(x_lower, df1, df2),
                 alpha=0.3, color='red')

plt.axvline(F_stat, color='darkgreen', linestyle='--', linewidth=3,
            label=f'Observed F = {F_stat:.2f}')
plt.axvline(F_lower, color='red', linestyle=':', linewidth=2)
plt.axvline(F_upper, color='red', linestyle=':', linewidth=2,
            label=f'Critical values = {F_lower:.2f}, {F_upper:.2f}')

plt.xlabel('F', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title(f'F({df1}, {df2}) Distribution', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
