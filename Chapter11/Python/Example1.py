# Chapter 11 - Σημειακή Εκτίμηση
# Example 1: Βασικοί Εκτιμητές
#   N(100, 15^2), n=50: x̄, S², σ̂²_MLE, SE(x̄)
#   Note: numpy ddof=1 -> unbiased S², ddof=0 -> MLE

import numpy as np

# Simulated sample from N(100, 15^2)
np.random.seed(42)
n           = 50
sample_data = np.random.normal(loc=100, scale=15, size=n)

# Point estimates for mean
mean_estimate = np.mean(sample_data)
print(f"Mean estimate: {mean_estimate:.4f}")

# Point estimates for variance
# Unbiased estimator (S^2) - ddof=1
var_unbiased = np.var(sample_data, ddof=1)
# MLE estimator - ddof=0
var_mle      = np.var(sample_data, ddof=0)

print(f"Unbiased variance (S^2): {var_unbiased:.4f}")
print(f"MLE variance:            {var_mle:.4f}")

# Standard deviation estimates
sd_unbiased = np.std(sample_data, ddof=1)
sd_mle      = np.std(sample_data, ddof=0)

print(f"Unbiased SD: {sd_unbiased:.4f}")
print(f"MLE SD:      {sd_mle:.4f}")

# Standard error of the mean
se_mean = np.std(sample_data, ddof=1) / np.sqrt(n)
print(f"SE of mean:  {se_mean:.4f}")

# Summary comparison
print("\n--- Comparison of Unbiased vs MLE ---")
print(f"True sigma^2 = 225")
print(f"S^2 (unbiased) = {var_unbiased:.4f}  |  bias ≈ 0")
print(f"MLE var        = {var_mle:.4f}  |  bias = -sigma^2/n = {-225/n:.4f}")
