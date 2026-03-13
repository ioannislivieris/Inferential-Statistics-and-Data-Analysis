# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 8: Welch's ANOVA και Kruskal-Wallis (Εναλλακτικές Μέθοδοι)

import pandas as pd
from scipy import stats
import numpy as np

advertising = pd.DataFrame({
    'Sales'   : [23,25,27,24,26, 30,32,28,31,29, 20,22,19,21,20],
    'Strategy': ['Television']*5 + ['Internet']*5 + ['Print']*5
})

groups = [advertising[advertising['Strategy'] == s]['Sales'].values
          for s in ['Television', 'Internet', 'Print']]

# Kruskal-Wallis test (non-parametric)
h_stat, p_kw = stats.kruskal(*groups)
print(f"Kruskal-Wallis: H = {h_stat:.4f}, p-value = {p_kw:.6f}")

# Welch's ANOVA via pingouin (pip install pingouin)
# import pingouin as pg
# welch_result = pg.welch_anova(data=advertising, dv='Sales',
#                               between='Strategy')
# print(welch_result[['Source','ddof1','ddof2','F','p-unc','np2']])

# Log transformation and standard ANOVA
advertising_log = advertising.copy()
advertising_log['LogSales'] = np.log(advertising_log['Sales'])
groups_log = [advertising_log[advertising_log['Strategy'] == s]
              ['LogSales'].values for s in ['Television','Internet','Print']]
f_log, p_log = stats.f_oneway(*groups_log)
print(f"\nANOVA on log(Sales): F = {f_log:.3f}, p = {p_log:.6f}")
