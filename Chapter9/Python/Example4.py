# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 4: Δειγματοληψία Κατά Συστάδες
#   50 καταστήματα, 100 πελάτες/κατάστημα, επιλογή 5 καταστημάτων

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(321)

# Create a population organized in clusters (e.g., retail stores)
stores              = 50   # Total number of stores (clusters)
customers_per_store = 100  # Customers per store

population = pd.DataFrame({
    'StoreID':    np.repeat(range(1, stores + 1), customers_per_store),
    'CustomerID': range(1, stores * customers_per_store + 1),
    'Spending':   np.random.normal(100, 30, stores * customers_per_store)
})

print(f"Total population size: {len(population)} customers")
print(f"Number of clusters (stores): {stores}")

# Perform cluster sampling: Randomly select 5 stores
num_clusters    = 5
selected_stores = np.random.choice(range(1, stores + 1),
                                   num_clusters, replace=False)
print(f"Selected store IDs: {selected_stores}")

# Include all customers from selected stores in the sample
cluster_sample = population[population['StoreID'].isin(selected_stores)]

print(f"\nTotal sample size: {len(cluster_sample)} customers")
print(f"Sample mean spending: {cluster_sample['Spending'].mean():.2f} Euros")
print(f"Population mean spending (true parameter): "
      f"{population['Spending'].mean():.2f} Euros")

# Perform simple random sampling of same size for comparison
srs_sample = population.sample(n=len(cluster_sample), random_state=321)
print(f"\nSimple random sampling - Mean spending: "
      f"{srs_sample['Spending'].mean():.2f} Euros")

# Create boxplot visualization for selected stores
plt.figure(figsize=(12, 6))
sns.boxplot(data=cluster_sample, x='StoreID', y='Spending')
plt.title('Customer Spending Distribution by Selected Store')
plt.xlabel('Store ID')
plt.ylabel('Spending (Euros)')
plt.tight_layout()
plt.show()
