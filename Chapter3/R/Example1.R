# Chapter 3 - Binomial Distribution
# Example 1: Basic Probability Calculations  B(10, 0.3)

# Parameters
n <- 10
p <- 0.3

# P(X = 3)
prob_exact <- dbinom(3, n, p)
cat(sprintf("P(X = 3) = %.4f\n", prob_exact))

# P(X <= 5)
prob_cumulative <- pbinom(5, n, p)
cat(sprintf("P(X <= 5) = %.4f\n", prob_cumulative))

# P(X >= 4) = 1 - P(X <= 3)
prob_greater <- 1 - pbinom(3, n, p)
cat(sprintf("P(X >= 4) = %.4f\n", prob_greater))
