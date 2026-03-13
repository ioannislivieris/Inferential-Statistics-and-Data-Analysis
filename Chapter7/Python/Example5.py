# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 5: Πλήρης Επιχειρηματική Ανάλυση Πωλήσεων
#   X ~ N(50.000, 8.000²)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu    = 50000
sigma = 8000

# 1. Probabilities for different ranges
print("=== Sales Analysis Report ===\n")

# Below average
prob_below_avg = norm.cdf(mu, loc=mu, scale=sigma)
print(f"1. Probability of below-average sales: {prob_below_avg*100:.2f}%")

# Above 60000
prob_above_60k = 1 - norm.cdf(60000, loc=mu, scale=sigma)
print(f"2. Probability of sales > 60,000: {prob_above_60k*100:.2f}%")

# Between 45000 and 55000
prob_middle = norm.cdf(55000, loc=mu, scale=sigma) - \
              norm.cdf(45000, loc=mu, scale=sigma)
print(f"3. Probability of sales between 45K-55K: {prob_middle*100:.2f}%")

# 2. Key quantiles
print("\n=== Performance Quantiles ===")
quantiles = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95]
values    = norm.ppf(quantiles, loc=mu, scale=sigma)

for q, v in zip(quantiles, values):
    print(f"{int(q*100)}th percentile: EUR {v:.0f}")

# 3. Visualization
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(14, 8))
plt.plot(x, y, 'b-', linewidth=2, label='Distribution')

# Shade regions
x_low = x[x <= 45000]
plt.fill_between(x_low, norm.pdf(x_low, loc=mu, scale=sigma),
                 alpha=0.3, color='red', label='Below Target (<45K)')

x_mid = x[(x >= 45000) & (x <= 55000)]
plt.fill_between(x_mid, norm.pdf(x_mid, loc=mu, scale=sigma),
                 alpha=0.3, color='green', label='Target Range (45K-55K)')

x_high = x[x >= 60000]
plt.fill_between(x_high, norm.pdf(x_high, loc=mu, scale=sigma),
                 alpha=0.3, color='blue', label='Excellent (>60K)')

# Add reference lines
plt.axvline(mu,    color='black',   linestyle='--', linewidth=2,
            label=f'Mean = EUR {mu:,.0f}')
plt.axvline(45000, color='darkgray', linestyle=':', linewidth=1.5)
plt.axvline(55000, color='darkgray', linestyle=':', linewidth=1.5)
plt.axvline(60000, color='darkgray', linestyle=':', linewidth=1.5)

# Labels
plt.text(mu,    max(y)*1.05, f'Mean = EUR {mu:,.0f}',
         ha='center', fontsize=10, weight='bold')
plt.text(40000, max(y)*0.5, 'Below\nTarget',
         ha='center', color='red', fontsize=9)
plt.text(50000, max(y)*0.3, 'Target\nRange',
         ha='center', color='darkgreen', fontsize=9)
plt.text(65000, max(y)*0.5, 'Excellent',
         ha='center', color='blue', fontsize=9)

plt.xlabel('Sales (EUR)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Sales Distribution Analysis', fontsize=14, weight='bold')
plt.legend(fontsize=10, loc='upper right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# 4. Summary statistics table
print("\n=== Summary Statistics ===")
print(f"Mean: EUR {mu:,.0f}")
print(f"Standard Deviation: EUR {sigma:,.0f}")
print(f"Coefficient of Variation: {(sigma/mu)*100:.2f}%")
print(f"\nZ-scores for key values:")
print(f"Sales = 45,000: z = {(45000-mu)/sigma:.2f}")
print(f"Sales = 55,000: z = {(55000-mu)/sigma:.2f}")
print(f"Sales = 60,000: z = {(60000-mu)/sigma:.2f}")
