# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 1: Έλεγχοι Z και t για μία μέση τιμή

# Sample data
sample_data <- c(8.5, 7.2, 9.1, 8.8, 7.5, 8.3, 9.2, 8.1,
                 7.8, 8.6, 9.0, 8.4, 7.9, 8.7, 9.3, 8.2,
                 7.6, 8.9, 8.0, 8.5, 7.7, 9.1, 8.3, 8.6, 7.4)

mu0 <- 8.0
sigma_known <- 0.6  # For Z-test
alpha <- 0.05

# Descriptive statistics
n <- length(sample_data)
xbar <- mean(sample_data)
s <- sd(sample_data)

cat("=== DESCRIPTIVE STATISTICS ===\n")
cat(sprintf("n = %d, x-bar = %.3f, s = %.3f\n\n", n, xbar, s))

# ============ Z-TEST (KNOWN SIGMA) ============
cat("=== Z-TEST (Known sigma = %.2f) ===\n", sigma_known)
se_z <- sigma_known / sqrt(n)
z_stat <- (xbar - mu0) / se_z
p_value_z <- 2 * pnorm(-abs(z_stat))
z_crit <- qnorm(1 - alpha/2)

cat(sprintf("SE = %.4f\n", se_z))
cat(sprintf("z-statistic = %.3f\n", z_stat))
cat(sprintf("Critical value = +/- %.3f\n", z_crit))
cat(sprintf("p-value = %.4f\n", p_value_z))
cat(sprintf("Decision: %s H0\n\n",
            ifelse(p_value_z < alpha, "REJECT", "FAIL TO REJECT")))

# 95% CI with known sigma
ci_z_lower <- xbar - z_crit * se_z
ci_z_upper <- xbar + z_crit * se_z
cat(sprintf("95%% CI (Z): [%.3f, %.3f]\n", ci_z_lower, ci_z_upper))
cat(sprintf("Does CI contain mu0=%.1f? %s\n\n",
            mu0, ifelse(mu0 >= ci_z_lower & mu0 <= ci_z_upper, "YES", "NO")))

# ============ T-TEST (UNKNOWN SIGMA) ============
cat("=== T-TEST (Unknown sigma) ===\n")
result_t <- t.test(sample_data, mu = mu0)
print(result_t)

# Effect size
cohens_d <- (xbar - mu0) / s
cat(sprintf("\nEffect size (Cohen's d) = %.3f\n", cohens_d))
cat(sprintf("Interpretation: %s effect\n",
            ifelse(abs(cohens_d) < 0.2, "Small",
            ifelse(abs(cohens_d) < 0.5, "Small-Medium",
            ifelse(abs(cohens_d) < 0.8, "Medium-Large", "Large")))))

# CI already in result_t, but let's verify equivalence
cat(sprintf("\nCI contains mu0? %s\n",
            ifelse(result_t$conf.int[1] <= mu0 & mu0 <= result_t$conf.int[2],
                   "YES (Consistent with failing to reject H0)",
                   "NO (Consistent with rejecting H0)")))

# ============ POWER ANALYSIS ============
cat("\n=== POWER ANALYSIS ===\n")
library(pwr)
effect_sizes <- seq(0.2, 1.0, by = 0.2)
powers <- sapply(effect_sizes, function(d) {
  pwr.t.test(n = n, d = d, sig.level = alpha,
             type = "one.sample", alternative = "two.sided")$power
})

cat("Effect Size (d) | Power\n")
cat("----------------+-------\n")
for(i in seq_along(effect_sizes)) {
  cat(sprintf("     %.2f       | %.3f\n", effect_sizes[i], powers[i]))
}

# Sample size for desired power
desired_power <- 0.80
n_required <- pwr.t.test(d = 0.5, power = desired_power,
                         sig.level = alpha,
                         type = "one.sample",
                         alternative = "two.sided")$n
cat(sprintf("\nSample size needed for d=0.5, power=%.2f: n = %.0f\n",
            desired_power, ceiling(n_required)))
