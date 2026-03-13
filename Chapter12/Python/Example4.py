# Chapter 12 - Διαστήματα Εμπιστοσύνης
# Example 4: Διάστημα για Διαφορά Δύο Μέσων (άνισες διασπορές, Welch)
#   2 εργοστάσια, n1=25, n2=30: F-test + Welch-Satterthwaite df

import numpy as np
from scipy import stats

# Sample data
factory1 = np.array([50.2, 48.7, 51.3, 49.8, 52.1, 50.5, 48.9, 51.7,
                     49.2, 52.4, 50.8, 49.5, 51.0, 48.6, 52.2,
                     50.1, 49.7, 51.4, 50.3, 48.8, 51.9, 49.4,
                     52.0, 50.6, 49.1])

factory2 = np.array([51.1, 52.5, 50.8, 52.9, 51.4, 52.2, 50.6, 53.1,
                     51.7, 52.8, 51.2, 52.6, 50.9, 53.0, 51.5,
                     52.3, 51.0, 52.7, 51.8, 52.4, 51.3, 52.1,
                     50.7, 52.9, 51.6, 52.5, 51.1, 52.8, 51.4, 52.2])

n1    = len(factory1)
n2    = len(factory2)
xbar1 = np.mean(factory1)
xbar2 = np.mean(factory2)
s1    = np.std(factory1, ddof=1)
s2    = np.std(factory2, ddof=1)
conf_level = 0.95

# F-test for equal variances
f_stat = s1**2 / s2**2
f_pval = 2 * min(stats.f.cdf(f_stat, n1 - 1, n2 - 1),
                 1 - stats.f.cdf(f_stat, n1 - 1, n2 - 1))

print("F-test for equal variances:")
print(f"  F-statistic: {f_stat:.3f}")
print(f"  p-value:     {f_pval:.4f}")
print(f"  Variances equal? "
      f"{'Yes (use pooled)' if f_pval > 0.05 else 'No (use Welch)'}\n")

# Welch's method
print("Welch's t-interval (unequal variances):")
print(f"  Factory 1: n={n1}, mean={xbar1:.2f}, sd={s1:.2f}")
print(f"  Factory 2: n={n2}, mean={xbar2:.2f}, sd={s2:.2f}")

# Standard error (no pooling)
se = np.sqrt(s1**2 / n1 + s2**2 / n2)

# Welch-Satterthwaite degrees of freedom
df_welch = (s1**2/n1 + s2**2/n2)**2 / \
           ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))

alpha        = 1 - conf_level
t_crit       = stats.t.ppf(1 - alpha / 2, df_welch)
diff         = xbar1 - xbar2
margin_error = t_crit * se
ci_lower     = diff - margin_error
ci_upper     = diff + margin_error

print(f"  Welch df:       {df_welch:.2f}")
print(f"  Difference:     {diff:.3f}")
print(f"  Standard error: {se:.3f}")
print(f"  {conf_level*100:.0f}% CI: [{ci_lower:.3f}, {ci_upper:.3f}]")

# Verify using scipy
ci_scipy = stats.t.interval(conf_level, df_welch, loc=diff, scale=se)
print(f"\nUsing scipy (Welch's method):")
print(f"  {conf_level*100:.0f}% CI: [{ci_scipy[0]:.3f}, {ci_scipy[1]:.3f}]")
