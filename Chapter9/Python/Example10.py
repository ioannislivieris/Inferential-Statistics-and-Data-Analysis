# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 10: Μεροληψία Μη Απόκρισης — Ανίχνευση και Διόρθωση
#   N=5000, ικανοποίηση~N(55,18), P(απόκριση) εξαρτάται από ικανοποίηση

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(456)

# === Create the population ===
N = 5000
population = pd.DataFrame({
    'ID':           range(1, N + 1),
    'Satisfaction': np.random.normal(55, 18, N).clip(1, 100)
})

true_mean = population['Satisfaction'].mean()
print(f"True population mean satisfaction: {true_mean:.2f}\n")

# === Model response probability as function of satisfaction ===
population['ResponseProb'] = (0.2 + 0.6 *
    (population['Satisfaction'] - 1) / 99)

# === Draw sample and simulate non-response ===
n           = 500
sample_data = population.sample(n=n, replace=False).copy()
sample_data['Responds'] = np.random.binomial(
    1, sample_data['ResponseProb'])

respondents = sample_data[sample_data['Responds'] == 1].copy()
print(f"Original sample size: {n}")
print(f"Number of respondents: {len(respondents)}")
print(f"Response rate: {len(respondents) / n * 100:.1f}%\n")

# === Calculate bias ===
naive_estimate = respondents['Satisfaction'].mean()
bias           = naive_estimate - true_mean
print(f"Naive estimate (respondents only): {naive_estimate:.2f}")
print(f"True population mean: {true_mean:.2f}")
print(f"Bias: {bias:.2f}\n")

# === Show that increasing sample size does NOT reduce bias ===
sample_sizes = [100, 200, 500, 1000, 2000]
print("--- Effect of sample size on bias ---")

for sz in sample_sizes:
    biases = []
    for j in range(200):
        s = population.sample(n=min(sz, N), replace=False).copy()
        s['Responds'] = np.random.binomial(1, s['ResponseProb'])
        resp = s[s['Responds'] == 1]
        biases.append(resp['Satisfaction'].mean() - true_mean)
    biases = np.array(biases)
    print(f"n = {sz}: Mean bias = {biases.mean():.2f}, "
          f"SD of estimates = {biases.std():.2f}")

# === Weighted estimation to correct for non-response ===
print("\n--- Weighted estimation (correction) ---")

respondents['Weight'] = 1 / respondents['ResponseProb']
weighted_estimate = np.average(respondents['Satisfaction'],
                               weights=respondents['Weight'])

print(f"Naive (unweighted) estimate: {naive_estimate:.2f}")
print(f"Weighted estimate: {weighted_estimate:.2f}")
print(f"True mean: {true_mean:.2f}")
print(f"Bias (naive): {naive_estimate - true_mean:.2f}")
print(f"Bias (weighted): {weighted_estimate - true_mean:.2f}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.hist(population['Satisfaction'], bins=30, density=True,
         alpha=0.5, color='lightgray', label='Population',
         edgecolor='black')
ax1.hist(respondents['Satisfaction'], bins=30, density=True,
         alpha=0.4, color='red', label='Respondents',
         edgecolor='black')
ax1.axvline(true_mean, color='blue', linestyle='--',
            linewidth=2, label=f'True mean = {true_mean:.1f}')
ax1.axvline(naive_estimate, color='red', linestyle='--',
            linewidth=2, label=f'Naive est. = {naive_estimate:.1f}')
ax1.set_title('Population vs Respondents')
ax1.set_xlabel('Satisfaction')
ax1.legend(fontsize=8)

ax2.scatter(population['Satisfaction'], population['ResponseProb'],
            s=1, alpha=0.3, color='gray', label='Population')
ax2.scatter(respondents['Satisfaction'], respondents['ResponseProb'],
            s=5, alpha=0.5, color='red', label='Respondents')
ax2.set_title('Response Probability vs Satisfaction')
ax2.set_xlabel('Satisfaction')
ax2.set_ylabel('P(Response)')
ax2.legend()

plt.tight_layout()
plt.show()
