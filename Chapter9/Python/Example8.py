# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 8: Στρωματοποιημένη Δειγματοληψία — Έλεγχος Ποιότητας
#   3 γραμμές παραγωγής (A:50%, B:30%, C:20%), ελαττωματικά 2/5/8%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# === Create the population ===
N_A, N_B, N_C = 5000, 3000, 2000
N = N_A + N_B + N_C  # Total population = 10000

population = pd.DataFrame({
    'ID':        range(1, N + 1),
    'Line':      ['A'] * N_A + ['B'] * N_B + ['C'] * N_C,
    'Defective': np.concatenate([
        np.random.binomial(1, 0.02, N_A),  # Line A: 2%
        np.random.binomial(1, 0.05, N_B),  # Line B: 5%
        np.random.binomial(1, 0.08, N_C)   # Line C: 8%
    ])
})

# True population defect rate
true_rate = population['Defective'].mean()
print(f"True population defect rate: {true_rate * 100:.2f}%\n")

# === Proportional stratified sampling (n = 200) ===
n = 200
n_A, n_B, n_C = round(n * N_A / N), round(n * N_B / N), round(n * N_C / N)
print(f"Sample allocation: A = {n_A}, B = {n_B}, C = {n_C}")

stratified_sample = pd.concat([
    population[population['Line'] == 'A'].sample(n=n_A),
    population[population['Line'] == 'B'].sample(n=n_B),
    population[population['Line'] == 'C'].sample(n=n_C)
])

# Estimated defect rate from stratified sample
strat_rate = stratified_sample['Defective'].mean()
strat_se   = np.sqrt(strat_rate * (1 - strat_rate) / n)
print(f"Stratified sample defect rate: {strat_rate * 100:.2f}%")
print(f"Standard error: {strat_se:.4f}\n")

# === Monte Carlo comparison: Stratified vs SRS ===
num_simulations = 1000
strat_estimates = np.zeros(num_simulations)
srs_estimates   = np.zeros(num_simulations)

for i in range(num_simulations):
    s = pd.concat([
        population[population['Line'] == 'A'].sample(n=n_A),
        population[population['Line'] == 'B'].sample(n=n_B),
        population[population['Line'] == 'C'].sample(n=n_C)
    ])
    strat_estimates[i] = s['Defective'].mean()

    srs = population.sample(n=n)
    srs_estimates[i] = srs['Defective'].mean()

print("--- Monte Carlo Comparison (1000 simulations) ---")
print(f"True defect rate: {true_rate * 100:.2f}%")
print(f"Stratified: Mean = {strat_estimates.mean() * 100:.2f}%, "
      f"SD = {strat_estimates.std() * 100:.2f}%")
print(f"SRS:        Mean = {srs_estimates.mean() * 100:.2f}%, "
      f"SD = {srs_estimates.std() * 100:.2f}%")
print(f"Efficiency gain (variance ratio): "
      f"{srs_estimates.var() / strat_estimates.var():.2f}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.hist(strat_estimates * 100, bins=30, color='steelblue',
         alpha=0.7, edgecolor='black')
ax1.axvline(true_rate * 100, color='red', linestyle='--', linewidth=2)
ax1.set_title('Stratified Sampling')
ax1.set_xlabel('Defect Rate (%)')
ax1.set_xlim(0, 10)

ax2.hist(srs_estimates * 100, bins=30, color='coral',
         alpha=0.7, edgecolor='black')
ax2.axvline(true_rate * 100, color='red', linestyle='--', linewidth=2)
ax2.set_title('Simple Random Sampling')
ax2.set_xlabel('Defect Rate (%)')
ax2.set_xlim(0, 10)

plt.tight_layout()
plt.show()
