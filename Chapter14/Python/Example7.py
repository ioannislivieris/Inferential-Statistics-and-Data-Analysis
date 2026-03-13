# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 7: Έλεγχος Ομοσκεδαστικότητας (Levene, Bartlett)

import pandas as pd
from scipy import stats
import numpy as np

advertising = pd.DataFrame({
    'Sales'   : [23,25,27,24,26, 30,32,28,31,29, 20,22,19,21,20],
    'Strategy': ['Television']*5 + ['Internet']*5 + ['Print']*5
})

groups = [advertising[advertising['Strategy'] == s]['Sales'].values
          for s in advertising['Strategy'].unique()]

# Levene's test
lev_stat, lev_p = stats.levene(*groups)
print(f"Levene's test: stat = {lev_stat:.4f}, p = {lev_p:.4f}")

# Bartlett's test
bar_stat, bar_p = stats.bartlett(*groups)
print(f"Bartlett's test: stat = {bar_stat:.4f}, p = {bar_p:.4f}")

# Variance ratio
vars_dict = {s: advertising[advertising['Strategy']==s]['Sales']
             .var(ddof=1)
             for s in advertising['Strategy'].unique()}
ratio = max(vars_dict.values()) / min(vars_dict.values())
print(f"Max/Min variance ratio: {ratio:.2f} (< 3 is acceptable)")
print("Variances:", {k: round(v, 3) for k, v in vars_dict.items()})
