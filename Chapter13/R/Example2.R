# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 2: Έλεγχος αναλογίας με μέγεθος φαινομένου

# Sample data
n <- 500
x <- 380
p0 <- 0.80
alpha <- 0.05

p_hat <- x / n

cat("=== PROPORTION TEST ===\n")
cat(sprintf("Sample: n=%d, x=%d, p-hat=%.4f (%.2f%%)\n",
            n, x, p_hat, p_hat*100))
cat(sprintf("Hypothesized: p0=%.2f (%.0f%%)\n\n", p0, p0*100))

# Check conditions
cat("Conditions: np0=%.1f, n(1-p0)=%.1f (both >= 5: %s)\n\n",
    n*p0, n*(1-p0),
    ifelse(n*p0 >= 5 & n*(1-p0) >= 5, "OK", "WARNING"))

# Manual Z-test
se <- sqrt(p0 * (1 - p0) / n)
z_stat <- (p_hat - p0) / se
p_value <- 2 * pnorm(-abs(z_stat))

cat("Manual calculation:\n")
cat(sprintf("SE = %.4f\n", se))
cat(sprintf("z = %.3f\n", z_stat))
cat(sprintf("p-value = %.4f\n", p_value))
cat(sprintf("Decision: %s H0\n\n",
            ifelse(p_value < alpha, "REJECT", "FAIL TO REJECT")))

# Using prop.test
result <- prop.test(x, n, p = p0, correct = FALSE)
print(result)

# Effect size (Cohen's h)
h <- 2 * (asin(sqrt(p_hat)) - asin(sqrt(p0)))
cat(sprintf("\nEffect size (Cohen's h) = %.3f\n", h))
cat(sprintf("Interpretation: %s effect\n",
            ifelse(abs(h) < 0.2, "Small",
            ifelse(abs(h) < 0.5, "Small-Medium",
            ifelse(abs(h) < 0.8, "Medium-Large", "Large")))))

# Sample size for desired margin of error
E <- 0.03  # 3% margin of error
z_crit <- qnorm(1 - alpha/2)
n_required <- (z_crit / E)^2 * p_hat * (1 - p_hat)
cat(sprintf("\nSample size for E=%.2f, confidence=%.0f%%: n = %.0f\n",
            E, (1-alpha)*100, ceiling(n_required)))

# Power analysis for proportions
library(pwr)
h_values <- seq(0.1, 0.5, by = 0.1)
cat("\n=== POWER FOR DIFFERENT EFFECT SIZES ===\n")
cat("Cohen's h | Power\n")
cat("----------+-------\n")
for(h_val in h_values) {
  pwr_result <- pwr.p.test(h = h_val, n = n, sig.level = alpha,
                           alternative = "two.sided")
  cat(sprintf("  %.2f    | %.3f\n", h_val, pwr_result$power))
}
