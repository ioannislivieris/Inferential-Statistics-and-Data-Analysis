# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 5: Οπτικοποίηση σφαλμάτων τύπου I και II και ισχύος

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.stats.power as smp

# Parameters
mu0 = 100
sigma = 15
n = 36
alpha = 0.05
se = sigma / np.sqrt(n)

fig, axes = plt.subplots(3, 2, figsize=(14, 14))

# ============ TYPE I AND TYPE II ERRORS ============
# Critical values
z_crit = stats.norm.ppf(1 - alpha/2)
x_crit_lower = mu0 - z_crit * se
x_crit_upper = mu0 + z_crit * se

x_vals = np.linspace(mu0 - 4*se, mu0 + 4*se, 500)

# Plot 1: Type I error
y_h0 = stats.norm.pdf(x_vals, mu0, se)
axes[0, 0].plot(x_vals, y_h0, 'k-', linewidth=2)
axes[0, 0].fill_between(x_vals[x_vals <= x_crit_lower],
                        y_h0[x_vals <= x_crit_lower],
                        alpha=0.3, color='red', label='Type I Error')
axes[0, 0].fill_between(x_vals[x_vals >= x_crit_upper],
                        y_h0[x_vals >= x_crit_upper],
                        alpha=0.3, color='red')
axes[0, 0].axvline(x_crit_lower, color='red', linestyle='--', linewidth=2)
axes[0, 0].axvline(x_crit_upper, color='red', linestyle='--', linewidth=2)
axes[0, 0].set_title(f'Type I Error (alpha)\n'
                     f'P(Reject H0 | H0 true) = {alpha:.3f}',
                     fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Sample Mean')
axes[0, 0].set_ylabel('Density')
axes[0, 0].legend()
axes[0, 0].grid(alpha=0.3)

# Plot 2: Type II error and Power
mu1 = 108
y_h1 = stats.norm.pdf(x_vals, mu1, se)
beta_val = (stats.norm.cdf(x_crit_upper, mu1, se) -
            stats.norm.cdf(x_crit_lower, mu1, se))
power_val = 1 - beta_val

axes[0, 1].plot(x_vals, y_h0, 'k--', linewidth=1,
                alpha=0.5, label='H0 true')
axes[0, 1].plot(x_vals, y_h1, 'b-', linewidth=2, label='H1 true')
mask_beta = (x_vals >= x_crit_lower) & (x_vals <= x_crit_upper)
axes[0, 1].fill_between(x_vals[mask_beta], y_h1[mask_beta],
                        alpha=0.3, color='orange',
                        label=f'Type II Error (beta={beta_val:.3f})')
mask_power = (x_vals < x_crit_lower) | (x_vals > x_crit_upper)
axes[0, 1].fill_between(x_vals[mask_power], y_h1[mask_power],
                        alpha=0.3, color='green',
                        label=f'Power (1-beta={power_val:.3f})')
axes[0, 1].axvline(x_crit_lower, color='red', linestyle='--', linewidth=2)
axes[0, 1].axvline(x_crit_upper, color='red', linestyle='--', linewidth=2)
axes[0, 1].set_title('Type II Error (beta) and Power (1-beta)',
                     fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Sample Mean')
axes[0, 1].set_ylabel('Density')
axes[0, 1].legend(fontsize=8)
axes[0, 1].grid(alpha=0.3)

# ============ POWER CURVES ============
# Effect of sample size
n_vals = np.arange(10, 101, 5)
effect_size = 0.5
powers_n = [smp.TTestPower().solve_power(effect_size=effect_size,
                                         nobs=n, alpha=alpha,
                                         alternative='two-sided')
            for n in n_vals]

axes[1, 0].plot(n_vals, powers_n, 'b-', linewidth=2)
axes[1, 0].axhline(0.80, color='red', linestyle='--', linewidth=1)
axes[1, 0].set_title(f'Power vs Sample Size\n'
                     f'Effect size d = {effect_size:.1f}, alpha = {alpha:.2f}',
                     fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Sample Size (n)')
axes[1, 0].set_ylabel('Power (1-beta)')
axes[1, 0].set_ylim(0, 1)
axes[1, 0].grid(alpha=0.3)

# Effect of effect size
d_vals = np.arange(0.1, 1.25, 0.05)
powers_d = [smp.TTestPower().solve_power(effect_size=d, nobs=36,
                                         alpha=alpha,
                                         alternative='two-sided')
            for d in d_vals]

axes[1, 1].plot(d_vals, powers_d, 'g-', linewidth=2)
axes[1, 1].axhline(0.80, color='red', linestyle='--', linewidth=1)
axes[1, 1].axvline([0.2, 0.5, 0.8], color='gray',
                   linestyle=':', linewidth=1)
axes[1, 1].text(0.2, 0.05, 'Small', ha='center', fontsize=9)
axes[1, 1].text(0.5, 0.05, 'Medium', ha='center', fontsize=9)
axes[1, 1].text(0.8, 0.05, 'Large', ha='center', fontsize=9)
axes[1, 1].set_title(f'Power vs Effect Size\nn = {n}, alpha = {alpha:.2f}',
                     fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel("Effect Size (Cohen's d)")
axes[1, 1].set_ylabel('Power (1-beta)')
axes[1, 1].set_ylim(0, 1)
axes[1, 1].grid(alpha=0.3)

# ============ ONE-TAILED VS TWO-TAILED ============
z_obs = 1.8
p_two = 2 * stats.norm.sf(abs(z_obs))
p_one = stats.norm.sf(abs(z_obs))

x_z = np.linspace(-4, 4, 500)
y_z = stats.norm.pdf(x_z)

# Two-tailed
axes[2, 0].plot(x_z, y_z, 'k-', linewidth=2)
axes[2, 0].fill_between(x_z[x_z <= -abs(z_obs)],
                        y_z[x_z <= -abs(z_obs)],
                        alpha=0.3, color='blue')
axes[2, 0].fill_between(x_z[x_z >= abs(z_obs)],
                        y_z[x_z >= abs(z_obs)],
                        alpha=0.3, color='blue')
axes[2, 0].axvline(-z_obs, color='blue', linestyle='--', linewidth=2)
axes[2, 0].axvline(z_obs, color='blue', linestyle='--', linewidth=2)
axes[2, 0].set_title(f'Two-tailed Test\nz = {z_obs:.2f}, '
                     f'p-value = {p_two:.4f}',
                     fontsize=12, fontweight='bold')
axes[2, 0].set_xlabel('z')
axes[2, 0].set_ylabel('Density')
axes[2, 0].grid(alpha=0.3)

# One-tailed
axes[2, 1].plot(x_z, y_z, 'k-', linewidth=2)
axes[2, 1].fill_between(x_z[x_z >= z_obs], y_z[x_z >= z_obs],
                        alpha=0.3, color='red')
axes[2, 1].axvline(z_obs, color='red', linestyle='--', linewidth=2)
axes[2, 1].set_title(f'One-tailed Test (Right)\nz = {z_obs:.2f}, '
                     f'p-value = {p_one:.4f}',
                     fontsize=12, fontweight='bold')
axes[2, 1].set_xlabel('z')
axes[2, 1].set_ylabel('Density')
axes[2, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Print summary
print("\n=== SUMMARY ===")
print(f"Type I Error (alpha): {alpha:.3f}")
print(f"Type II Error (beta): {beta_val:.3f}")
print(f"Power (1-beta): {power_val:.3f}")
print(f"\nFor z = {z_obs:.2f}:")
print(f"  Two-tailed p-value: {p_two:.4f}")
print(f"  One-tailed p-value: {p_one:.4f}")
print(f"  One-tailed has {(1 - p_one/p_two) * 100:.1f}% lower p-value")
