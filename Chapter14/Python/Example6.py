# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 6: Έλεγχος Κανονικότητας Υπολοίπων ANOVA (Shapiro-Wilk, Q-Q plot)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

advertising_data = {
    'Sales'   : [23,25,27,24,26, 30,32,28,31,29, 20,22,19,21,20],
    'Strategy': ['Television']*5 + ['Internet']*5 + ['Print']*5
}
import pandas as pd
advertising = pd.DataFrame(advertising_data)

model     = ols('Sales ~ C(Strategy)', data=advertising).fit()
residuals = model.resid

# Shapiro-Wilk on residuals
w, p_sw = stats.shapiro(residuals)
print(f"Shapiro-Wilk on residuals: W = {w:.4f}, p = {p_sw:.4f}")
print("Conclusion:", "Normality supported." if p_sw > 0.05
      else "Normality may be violated.")

# Per-group Shapiro-Wilk
print("\nPer-group Shapiro-Wilk:")
for s in advertising['Strategy'].unique():
    g = advertising[advertising['Strategy'] == s]['Sales']
    w_g, p_g = stats.shapiro(g)
    print(f"  {s:<12}: W = {w_g:.4f}, p = {p_g:.4f}")

# Q-Q plot
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
# Q-Q of residuals
stats.probplot(residuals, dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot of ANOVA Residuals")
# Histogram of residuals
axes[1].hist(residuals, bins=8, color='steelblue',
             edgecolor='white', density=True, alpha=0.8)
x = np.linspace(residuals.min(), residuals.max(), 100)
axes[1].plot(x, stats.norm.pdf(x, residuals.mean(), residuals.std()),
             'r-', linewidth=2)
axes[1].set_title("Histogram of Residuals")
axes[1].set_xlabel("Residual")
plt.tight_layout()
plt.savefig('normality_check.png', dpi=300, bbox_inches='tight')
