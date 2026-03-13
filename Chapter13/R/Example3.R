# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 3: Έλεγχος διασποράς με διαστήματα εμπιστοσύνης

# Sample data
sample_data <- c(2.1, 2.5, 2.3, 2.7, 2.4, 2.6, 2.2, 2.8,
                 2.5, 2.3, 2.6, 2.4, 2.7, 2.3, 2.5, 2.4,
                 2.6, 2.5, 2.7, 2.4)

sigma2_0 <- 0.04
alpha <- 0.05

n <- length(sample_data)
s2 <- var(sample_data)
s <- sd(sample_data)
df <- n - 1

cat("=== VARIANCE TEST ===\n")
cat(sprintf("n=%d, s^2=%.4f, s=%.3f\n", n, s2, s))
cat(sprintf("Hypothesized: sigma^2=%.4f, sigma=%.3f\n\n",
            sigma2_0, sqrt(sigma2_0)))

# Chi-square test
chi2_stat <- (n - 1) * s2 / sigma2_0
p_right <- pchisq(chi2_stat, df, lower.tail = FALSE)
p_left <- pchisq(chi2_stat, df)
p_value <- 2 * min(p_right, p_left)

cat("Chi-square test:\n")
cat(sprintf("chi^2 = %.3f (df=%d)\n", chi2_stat, df))
cat(sprintf("p-value (two-tailed) = %.4f\n", p_value))
cat(sprintf("p-value (right, H1: sigma^2 > %.4f) = %.4f\n",
            sigma2_0, p_right))
cat(sprintf("p-value (left, H1: sigma^2 < %.4f) = %.4f\n",
            sigma2_0, p_left))
cat(sprintf("\nDecision: %s H0\n\n",
            ifelse(p_value < alpha, "REJECT", "FAIL TO REJECT")))

# Critical values and rejection regions
chi2_lower <- qchisq(alpha/2, df)
chi2_upper <- qchisq(1 - alpha/2, df)
cat(sprintf("Critical values: [%.3f, %.3f]\n", chi2_lower, chi2_upper))
cat(sprintf("Observed chi^2=%.3f is %s critical region\n\n",
            chi2_stat,
            ifelse(chi2_stat < chi2_lower | chi2_stat > chi2_upper,
                   "IN", "NOT IN")))

# Confidence intervals
ci_var_lower <- (n - 1) * s2 / chi2_upper
ci_var_upper <- (n - 1) * s2 / chi2_lower
ci_sd_lower <- sqrt(ci_var_lower)
ci_sd_upper <- sqrt(ci_var_upper)

cat(sprintf("95%% CI for variance: [%.4f, %.4f]\n",
            ci_var_lower, ci_var_upper))
cat(sprintf("95%% CI for SD: [%.3f, %.3f]\n", ci_sd_lower, ci_sd_upper))
cat(sprintf("Contains sigma^2_0=%.4f? %s\n",
            sigma2_0,
            ifelse(ci_var_lower <= sigma2_0 & sigma2_0 <= ci_var_upper,
                   "YES (Consistent with not rejecting H0)",
                   "NO (Consistent with rejecting H0)")))

# Relationship between CI and hypothesis test
cat("\n=== CI-TEST EQUIVALENCE ===\n")
cat("For two-tailed test at alpha=0.05:\n")
cat("- If 95% CI contains sigma^2_0: Fail to reject H0\n")
cat("- If 95% CI excludes sigma^2_0: Reject H0\n")
cat(sprintf("This example: %s\n",
            ifelse(ci_var_lower <= sigma2_0 & sigma2_0 <= ci_var_upper,
                   "CI contains sigma^2_0, so we fail to reject H0",
                   "CI excludes sigma^2_0, so we reject H0")))
