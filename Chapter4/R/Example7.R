# Chapter 4 - Poisson Distribution
# Example 7: Insurance Company Risk Analysis  Poisson(3)

# Parameter
lambda <- 3

# i. P(X > 5) = 1 - P(X <= 5)
prob <- 1 - ppois(5, lambda)
cat(sprintf("i. P(X > 5) = %.4f\n", prob))

# ii. Mean and standard deviation
mean_val <- lambda
std_val  <- sqrt(lambda)
cat(sprintf("\nii. Mean:               %d\n", mean_val))
cat(sprintf("    Standard Deviation: %.2f\n", std_val))

# iii. 95% confidence interval
lower <- qpois(0.025, lambda)
upper <- qpois(0.975, lambda)
cat(sprintf("\niii. 95%% Confidence Interval: [%d, %d]\n", lower, upper))

# iv. Probabilities for k = 0, ..., 8
cat("\niv. Probabilities:\n")
for (k in 0:8) {
  cat(sprintf("    P(X = %d) = %.4f\n", k, dpois(k, lambda)))
}

# Visualization
x     <- 0:10
probs <- dpois(x, lambda)
barplot(probs, names.arg = x, col = 'steelblue',
        xlab = 'Number of Claims', ylab = 'Probability',
        main = 'Poisson(3) - Insurance Claims Distribution')
