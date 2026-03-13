# Chapter 11 - Σημειακή Εκτίμηση
# Example 3: MLE για Εκθετική Κατανομή
#   Exp(λ=0.5), n=100: λ̂_MLE = 1/x̄, οπτικοποίηση log-likelihood
#   Note: np.random.exponential(scale=1/λ) — scale is the MEAN, not the rate

import numpy as np
import matplotlib.pyplot as plt

# Generate sample from exponential distribution
np.random.seed(42)
true_lambda = 0.5
n           = 100
sample_exp  = np.random.exponential(scale=1 / true_lambda, size=n)

# MLE for lambda: λ̂ = 1 / x̄
lambda_mle = 1 / np.mean(sample_exp)
print(f"True lambda:   {true_lambda:.4f}")
print(f"MLE estimate:  {lambda_mle:.4f}")
print(f"Sample mean:   {np.mean(sample_exp):.4f}  (= 1/lambda_mle)")

# Log-likelihood function: l(λ) = n*log(λ) - λ*Σx_i
def log_likelihood(lam, data):
    n = len(data)
    return n * np.log(lam) - lam * np.sum(data)

# Evaluate over a grid
lambda_seq = np.linspace(0.3, 0.7, 100)
ll_values  = [log_likelihood(l, sample_exp) for l in lambda_seq]

print(f"\nLog-likelihood at MLE:         {log_likelihood(lambda_mle, sample_exp):.4f}")
print(f"Log-likelihood at true lambda: {log_likelihood(true_lambda, sample_exp):.4f}")

# Plot log-likelihood
plt.figure(figsize=(10, 6))
plt.plot(lambda_seq, ll_values, linewidth=2, label='Log-Likelihood')
plt.axvline(lambda_mle,  color='red',       linestyle='--',
            linewidth=2, label=f'MLE = {lambda_mle:.4f}')
plt.axvline(true_lambda, color='darkgreen', linestyle=':',
            linewidth=2, label=f'True λ = {true_lambda:.4f}')
plt.xlabel(r'$\lambda$', fontsize=12)
plt.ylabel('Log-Likelihood', fontsize=12)
plt.title('Log-Likelihood Function — Exponential Distribution', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
