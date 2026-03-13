# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 9: Δειγματοληψία Κατά Συστάδες vs Στρωματοποιημένη
#   80 καταστήματα, 4 περιφέρειες, 10 επιλεγμένα, 30 πελάτες/κατάστημα

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)

# === Create the population ===
stores_per_region   = 20
customers_per_store = 50
regions             = ['North', 'South', 'East', 'West']
region_means        = [7.5, 6.8, 7.2, 6.5]
sigma               = 1.5

data     = []
store_id = 1

for region, mu in zip(regions, region_means):
    for s in range(stores_per_region):
        satisfaction = np.random.normal(mu, sigma, customers_per_store)
        for sat in satisfaction:
            data.append({'StoreID': store_id, 'Region': region,
                         'Satisfaction': sat})
        store_id += 1

population = pd.DataFrame(data)
population['Satisfaction'] = population['Satisfaction'].clip(1, 10)

true_mean = population['Satisfaction'].mean()
print(f"Total population size: {len(population)} customers")
print(f"True mean satisfaction: {true_mean:.3f}\n")

# === Cluster Sampling: Select 10 stores, survey 30 customers each ===
num_clusters      = 10
customers_sampled = 30

selected_stores = np.random.choice(range(1, 81), num_clusters, replace=False)
print(f"Selected stores: {selected_stores}")

cluster_sample = (population[population['StoreID'].isin(selected_stores)]
                  .groupby('StoreID')
                  .apply(lambda x: x.sample(n=customers_sampled))
                  .reset_index(drop=True))

print(f"Sample size: {len(cluster_sample)} customers")
print(f"Cluster estimate: {cluster_sample['Satisfaction'].mean():.3f}")
print("\nRegions represented in cluster sample:")
print(cluster_sample['Region'].value_counts())

# === Stratified Sampling for comparison ===
n_total      = len(cluster_sample)
n_per_region = round(n_total / len(regions))

stratified_sample = (population.groupby('Region')
                     .apply(lambda x: x.sample(n=n_per_region))
                     .reset_index(drop=True))

print(f"\nStratified estimate: "
      f"{stratified_sample['Satisfaction'].mean():.3f}")

# === Monte Carlo Comparison ===
num_sims    = 1000
cluster_est = np.zeros(num_sims)
strat_est   = np.zeros(num_sims)

for i in range(num_sims):
    sel = np.random.choice(range(1, 81), num_clusters, replace=False)
    cs  = (population[population['StoreID'].isin(sel)]
           .groupby('StoreID')
           .apply(lambda x: x.sample(n=customers_sampled))
           .reset_index(drop=True))
    cluster_est[i] = cs['Satisfaction'].mean()

    ss = (population.groupby('Region')
          .apply(lambda x: x.sample(n=n_per_region))
          .reset_index(drop=True))
    strat_est[i] = ss['Satisfaction'].mean()

print("\n--- Monte Carlo Comparison (1000 simulations) ---")
print(f"True mean: {true_mean:.3f}")
print(f"Cluster:    Mean = {cluster_est.mean():.3f}, "
      f"SD = {cluster_est.std():.4f}")
print(f"Stratified: Mean = {strat_est.mean():.3f}, "
      f"SD = {strat_est.std():.4f}")
print(f"Cluster/Stratified variance ratio: "
      f"{cluster_est.var() / strat_est.var():.2f}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
xlims = (min(cluster_est.min(), strat_est.min()),
         max(cluster_est.max(), strat_est.max()))

ax1.hist(cluster_est, bins=30, color='steelblue',
         alpha=0.7, edgecolor='black')
ax1.axvline(true_mean, color='red', linestyle='--', linewidth=2)
ax1.set_title('Cluster Sampling')
ax1.set_xlabel('Mean Satisfaction')
ax1.set_xlim(xlims)

ax2.hist(strat_est, bins=30, color='coral',
         alpha=0.7, edgecolor='black')
ax2.axvline(true_mean, color='red', linestyle='--', linewidth=2)
ax2.set_title('Stratified Sampling')
ax2.set_xlabel('Mean Satisfaction')
ax2.set_xlim(xlims)

plt.tight_layout()
plt.show()
