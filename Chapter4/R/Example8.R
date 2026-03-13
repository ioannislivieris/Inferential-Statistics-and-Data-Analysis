# Chapter 4 - Poisson Distribution
# Example 8: Call Center — Two Departments & Additive Property + Bayes
#   X ~ Poisson(4)  Technical Support
#   Y ~ Poisson(6)  Sales
#   X + Y ~ Poisson(10)  (additive property)

# Parameters
lambda_tech  <- 4    # Technical Support
lambda_sales <- 6    # Sales

cat("=== Call Center Analysis ===\n\n")

# i. P(Total = 8) using additive property
lambda_total   <- lambda_tech + lambda_sales   # = 10
prob_total_8   <- dpois(8, lambda_total)
cat(sprintf("i. P(Total = 8 calls) = %.4f\n\n", prob_total_8))

# ii. Conditional probability P(Tech=3 | Total=8)
# P(Tech=k, Sales=8-k) for k = 0,...,8
k_values    <- 0:8
probs_joint <- numeric(9)
for (k in k_values) {
  probs_joint[k + 1] <- dpois(k, lambda_tech) * dpois(8 - k, lambda_sales)
}

prob_tech_3_given_8 <- probs_joint[4] / sum(probs_joint)
cat(sprintf("ii. P(Tech=3 | Total=8) = %.4f\n\n", prob_tech_3_given_8))
cat(sprintf("    Verification: sum(joint probs) = %.4f\n",   sum(probs_joint)))
cat(sprintf("    (should equal P(Total=8) = %.4f)\n\n",      prob_total_8))

# iii. P(Total >= 10)
prob_at_least_10 <- 1 - ppois(9, lambda_total)
cat(sprintf("iii. P(Total >= 10 calls) = %.4f\n\n", prob_at_least_10))

# Visualization
par(mfrow = c(2, 2))

x_tech <- 0:15
plot(x_tech, dpois(x_tech, lambda_tech), type = 'h', lwd = 3,
     col  = 'blue', xlab = 'Number of Calls', ylab = 'Probability',
     main = sprintf('Technical Support\nPoisson(%d)', lambda_tech))
abline(v = lambda_tech, col = 'red', lty = 2, lwd = 2)

x_sales <- 0:20
plot(x_sales, dpois(x_sales, lambda_sales), type = 'h', lwd = 3,
     col  = 'darkgreen', xlab = 'Number of Calls', ylab = 'Probability',
     main = sprintf('Sales\nPoisson(%d)', lambda_sales))
abline(v = lambda_sales, col = 'red', lty = 2, lwd = 2)

x_total <- 0:25
plot(x_total, dpois(x_total, lambda_total), type = 'h', lwd = 3,
     col  = 'purple', xlab = 'Number of Calls', ylab = 'Probability',
     main = sprintf('Total Calls\nPoisson(%d)', lambda_total))
abline(v = lambda_total, col = 'red',    lty = 2, lwd = 2)
abline(v = 8,            col = 'orange', lty = 3, lwd = 2)
legend('topright', legend = c('Mean', 'Total=8'),
       col = c('red', 'orange'), lty = c(2, 3), lwd = 2, cex = 0.8)

# Conditional distribution P(Tech=k | Total=8)
conditional_probs <- probs_joint / sum(probs_joint)
barplot(conditional_probs, names.arg = k_values, col = 'coral',
        xlab = 'Technical Calls (k)', ylab = 'P(Tech=k | Total=8)',
        main = 'Conditional Distribution\nP(Tech=k | Total=8)')

par(mfrow = c(1, 1))

# Results table
cat("\n=== Conditional Probabilities Table ===\n")
cat("k\tP(Tech=k, Sales=8-k)\tP(Tech=k | Total=8)\n")
cat(strrep("-", 60), "\n")
for (k in k_values) {
  cat(sprintf("%d\t%.6f\t\t%.4f\n", k,
              probs_joint[k + 1], conditional_probs[k + 1]))
}
