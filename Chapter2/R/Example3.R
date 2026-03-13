# Chapter 2 - Sampling Methods and Basic Concepts
# Example 3: Portfolio Analysis

# Simulate historical returns (in percentages)
set.seed(123)
n_periods <- 100

# Stock A: mean 8%, sd 15%
returns_a <- rnorm(n_periods, mean = 8, sd = 15)

# Stock B: mean 12%, sd 20%
returns_b <- rnorm(n_periods, mean = 12, sd = 20)

# Portfolio weights
weight_a <- 0.6
weight_b <- 0.4

# Portfolio returns
portfolio_returns <- weight_a * returns_a + weight_b * returns_b

# Calculate statistics
cat("Stock A:\n")
cat(sprintf("  Mean Return: %.2f%%\n", mean(returns_a)))
cat(sprintf("  Std Dev:     %.2f%%\n\n", sd(returns_a)))

cat("Stock B:\n")
cat(sprintf("  Mean Return: %.2f%%\n", mean(returns_b)))
cat(sprintf("  Std Dev:     %.2f%%\n\n", sd(returns_b)))

cat("Portfolio (60% A, 40% B):\n")
cat(sprintf("  Mean Return: %.2f%%\n", mean(portfolio_returns)))
cat(sprintf("  Std Dev:     %.2f%%\n", sd(portfolio_returns)))

# Correlation
correlation <- cor(returns_a, returns_b)
cat(sprintf("  Correlation: %.3f\n", correlation))

# Visualization
par(mfrow = c(2, 2))

hist(returns_a, breaks = 20, col = 'skyblue',
     main = 'Stock A Returns', xlab = 'Return (%)')
hist(returns_b, breaks = 20, col = 'lightcoral',
     main = 'Stock B Returns', xlab = 'Return (%)')
hist(portfolio_returns, breaks = 20, col = 'lightgreen',
     main = 'Portfolio Returns', xlab = 'Return (%)')
plot(returns_a, returns_b, pch = 19, col = 'darkblue',
     xlab = 'Stock A Return (%)',
     ylab = 'Stock B Return (%)',
     main = 'Scatter Plot: A vs B')
abline(lm(returns_b ~ returns_a), col = 'red', lwd = 2)

par(mfrow = c(1, 1))
