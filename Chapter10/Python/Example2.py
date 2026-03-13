# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 2: ΚΟΘ με Εκθετική Κατανομή (Exp λ=0.5)
#   Έντονα ασύμμετρη — n = 5, 10, 30, 100

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon

np.random.seed(42)
n_simulations  = 10000
lambda_param   = 0.5
sample_sizes   = [5, 10, 30, 100]

# Population parameters
pop_mean = 1 / lambda_param   # = 2
pop_sd   = 1 / lambda_param   # = 2

fig = plt.figure(figsize=(15, 10))

# Plot original exponential distribution
ax1   = plt.subplot(2, 3, 1)
x_exp = np.linspace(0, 10, 200)
y_exp = expon.pdf(x_exp, scale=1 / lambda_param)
ax1.plot(x_exp, y_exp, 'b-', linewidth=2)
ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('Density', fontsize=11)
ax1.set_title('Original Exponential Distribution', fontsize=12)
ax1.grid(alpha=0.3)

# Plot sampling distributions
for idx, n in enumerate(sample_sizes, start=2):
    sample_means = [np.mean(np.random.exponential(
                        scale=1 / lambda_param, size=n))
                    for _ in range(n_simulations)]

    se = pop_sd / np.sqrt(n)

    ax = plt.subplot(2, 3, idx)
    ax.hist(sample_means, bins=50, density=True,
            alpha=0.6, color='blue', edgecolor='black')

    x = np.linspace(min(sample_means), max(sample_means), 200)
    y = norm.pdf(x, loc=pop_mean, scale=se)
    ax.plot(x, y, 'r-', linewidth=2, label='Theoretical N')

    ax.axvline(pop_mean, color='green', linestyle='--',
               linewidth=2, label='Pop. Mean')

    ax.set_xlabel('Sample Mean', fontsize=11)
    ax.set_ylabel('Density', fontsize=11)
    ax.set_title(f'n = {n}', fontsize=12)
    ax.set_xlim(0, 5)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

plt.suptitle('CLT — Exponential Distribution (lambda=0.5)',
             fontsize=14, y=1.01)
plt.tight_layout()
plt.show()
