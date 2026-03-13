# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 4: Κατανομές χ² και F
#   χ²(10) και F(5, 10)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, f

# Chi-square distribution
df_chi = 10

# i. P(chi^2 > 15) for chi^2(10)
prob_chi = 1 - chi2.cdf(15, df_chi)
print(f"P(chi^2 > 15) for chi^2(10) = {prob_chi:.4f}")

# Critical value
chi_critical = chi2.ppf(0.95, df_chi)
print(f"chi^2_{{0.05, 10}} = {chi_critical:.4f}")

# F distribution
df1 = 5
df2 = 10

# ii. P(F > 2.5) for F(5, 10)
prob_f = 1 - f.cdf(2.5, df1, df2)
print(f"P(F > 2.5) for F(5,10) = {prob_f:.4f}")

# Critical value
f_critical = f.ppf(0.95, df1, df2)
print(f"F_{{0.05, 5, 10}} = {f_critical:.4f}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Chi-square plot
x_chi = np.linspace(0, 25, 1000)
y_chi  = chi2.pdf(x_chi, df_chi)

ax1.plot(x_chi, y_chi, 'b-', linewidth=2, label='PDF')
ax1.axvline(chi_critical, color='red', linestyle='--', linewidth=2,
            label=f'Critical value = {chi_critical:.2f}')

x_shade = x_chi[x_chi >= chi_critical]
ax1.fill_between(x_shade, chi2.pdf(x_shade, df_chi), alpha=0.3, color='red',
                 label='Rejection region (5%)')

ax1.set_xlabel(r'$\chi^2$', fontsize=12)
ax1.set_ylabel('Density', fontsize=12)
ax1.set_title(r'$\chi^2(10)$ Distribution', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(alpha=0.3)

# F plot
x_f = np.linspace(0, 5, 1000)
y_f  = f.pdf(x_f, df1, df2)

ax2.plot(x_f, y_f, 'b-', linewidth=2, label='PDF')
ax2.axvline(f_critical, color='red', linestyle='--', linewidth=2,
            label=f'Critical value = {f_critical:.2f}')

x_shade = x_f[x_f >= f_critical]
ax2.fill_between(x_shade, f.pdf(x_shade, df1, df2), alpha=0.3, color='red',
                 label='Rejection region (5%)')

ax2.set_xlabel('F', fontsize=12)
ax2.set_ylabel('Density', fontsize=12)
ax2.set_title('F(5, 10) Distribution', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()
