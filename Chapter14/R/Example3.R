# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 3: Σύγκριση Δύο Αναλογιών (Z-test Αναλογιών)

n1 <- 200; x1 <- 85
n2 <- 220; x2 <- 105
p_hat1 <- x1 / n1;  p_hat2 <- x2 / n2

# Check assumptions
cat("n1*p1 =", n1*p_hat1, "  n1*(1-p1) =", n1*(1-p_hat1), "\n")
cat("n2*p2 =", n2*p_hat2, "  n2*(1-p2) =", n2*(1-p_hat2), "\n\n")

# Two-proportion z-test (no continuity correction)
prop_test <- prop.test(x = c(x1, x2), n = c(n1, n2),
                       alternative = "two.sided", correct = FALSE)
print(prop_test)

# Manual calculation
p_bar    <- (x1 + x2) / (n1 + n2)
se_pool  <- sqrt(p_bar * (1 - p_bar) * (1/n1 + 1/n2))
z_stat   <- (p_hat1 - p_hat2) / se_pool
p_value  <- 2 * pnorm(-abs(z_stat))

cat("\n--- Manual Calculation ---\n")
cat("Pooled p-hat:", round(p_bar, 4), "\n")
cat("SE (pooled) :", round(se_pool, 4), "\n")
cat("z-statistic :", round(z_stat, 4), "\n")
cat("p-value     :", round(p_value, 4), "\n")

# 95% CI (without pooling)
se_ci <- sqrt(p_hat1*(1-p_hat1)/n1 + p_hat2*(1-p_hat2)/n2)
ci_lo <- (p_hat1 - p_hat2) - 1.96 * se_ci
ci_hi <- (p_hat1 - p_hat2) + 1.96 * se_ci
cat("95% CI for (p1-p2): [", round(ci_lo, 4), ",", round(ci_hi, 4), "]\n")
