# Chapter 2 - Sampling Methods and Basic Concepts
# Example 1: Discrete Distribution Calculations

# Define values and probabilities
values <- c(10, 20, 30, 40, 50)
probs  <- c(0.15, 0.25, 0.30, 0.20, 0.10)

# Expected value
expected_value <- sum(values * probs)
cat(sprintf("Expected Value: %.2f\n", expected_value))

# Variance
expected_x2 <- sum(values^2 * probs)
variance     <- expected_x2 - expected_value^2
cat(sprintf("Variance: %.2f\n", variance))

# Standard deviation
std_dev <- sqrt(variance)
cat(sprintf("Standard Deviation: %.2f\n", std_dev))

# Visualization
barplot(probs, names.arg = values, col = 'steelblue',
        xlab  = 'Values', ylab = 'Probability',
        main  = 'Probability Distribution',
        ylim  = c(0, max(probs) * 1.2))
abline(v = expected_value / 10 + 0.5, col = 'red', lwd = 2, lty = 2)
legend('topright',
       legend = sprintf('E(X) = %.2f', expected_value),
       col = 'red', lty = 2, lwd = 2)
