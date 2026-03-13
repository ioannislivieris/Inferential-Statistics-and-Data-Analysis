# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 11: Σχεδιασμός Δειγματοληψίας για Δημοσκόπηση
#   N=50000 ψηφοφόροι, 3 ηλικιακές ομάδες, 3 μέθοδοι δειγματοληψίας

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# === Create the voter population ===
N        = 50000
n_young  = round(N * 0.30)
n_middle = round(N * 0.40)
n_older  = N - n_young - n_middle

population = pd.DataFrame({
    'ID':       range(1, N + 1),
    'AgeGroup': (['Young']  * n_young +
                 ['Middle'] * n_middle +
                 ['Older']  * n_older),
    'SupportsA': np.concatenate([
        np.random.binomial(1, 0.45, n_young),
        np.random.binomial(1, 0.52, n_middle),
        np.random.binomial(1, 0.38, n_older)
    ])
})

true_support = population['SupportsA'].mean()
print(f"True support for Candidate A: {true_support * 100:.2f}%\n")

# === Calculate required sample size ===
Z     = 1.96
E     = 0.03
p_est = 0.5

n_required = int(np.ceil(Z**2 * p_est * (1 - p_est) / E**2))
print(f"Required sample size for +/- 3% margin: {n_required}\n")

n = n_required

# Proportional allocation
n_y = round(n * 0.30)
n_m = round(n * 0.40)
n_o = n - n_y - n_m

# === Monte Carlo: Compare three sampling methods ===
num_sims  = 1000
srs_est   = np.zeros(num_sims)
strat_est = np.zeros(num_sims)
sys_est   = np.zeros(num_sims)

for i in range(num_sims):
    # 1. Simple Random Sampling
    srs        = population.sample(n=n)
    srs_est[i] = srs['SupportsA'].mean()

    # 2. Stratified Sampling (by age group)
    strat = pd.concat([
        population[population['AgeGroup'] == 'Young'].sample(n=n_y),
        population[population['AgeGroup'] == 'Middle'].sample(n=n_m),
        population[population['AgeGroup'] == 'Older'].sample(n=n_o)
    ])
    strat_est[i] = strat['SupportsA'].mean()

    # 3. Systematic Sampling
    k           = N // n
    start       = np.random.randint(0, k)
    sys_indices = list(range(start, N, k))[:n]
    sys         = population.iloc[sys_indices]
    sys_est[i]  = sys['SupportsA'].mean()

# === Results ===
print("--- Monte Carlo Comparison (1000 simulations) ---")
print(f"True support: {true_support * 100:.2f}%\n")

methods   = ['SRS', 'Stratified', 'Systematic']
estimates = [srs_est, strat_est, sys_est]

results = []
for name, est in zip(methods, estimates):
    moe     = np.percentile(np.abs(est - true_support), 95)
    correct = np.mean((est > 0.5) == (true_support > 0.5))
    results.append({
        'Method':      name,
        'Mean (%)':    f"{est.mean() * 100:.2f}",
        'SD (%)':      f"{est.std()  * 100:.2f}",
        'Bias (%)':    f"{(est.mean() - true_support) * 100:.2f}",
        'MoE 95% (%)': f"{moe * 100:.2f}",
        'Correct (%)': f"{correct * 100:.1f}"
    })

print(pd.DataFrame(results).to_string(index=False))

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
colors = ['steelblue', 'coral', 'gold']
titles = ['Simple Random Sampling', 'Stratified Sampling',
          'Systematic Sampling']

for ax, est, color, title in zip(axes, estimates, colors, titles):
    ax.hist(est * 100, bins=30, color=color,
            alpha=0.7, edgecolor='black')
    ax.axvline(true_support * 100, color='red',
               linestyle='--', linewidth=2, label='True support')
    ax.axvline(50, color='darkgreen',
               linestyle=':', linewidth=2, label='50% threshold')
    ax.set_title(title)
    ax.set_xlabel('Support for A (%)')
    ax.set_xlim(35, 60)
    ax.legend(fontsize=8)

plt.tight_layout()
plt.show()
