# Chapter 4 - Poisson Distribution
# Example 1: Basic Probability Calculations  Poisson(5)

# Parameter
lambda <- 5

# P(X = 4)
prob_exact <- dpois(4, lambda)
cat(sprintf("P(X = 4) = %.4f\n", prob_exact))

# P(X <= 6)
prob_cumulative <- ppois(6, lambda)
cat(sprintf("P(X <= 6) = %.4f\n", prob_cumulative))

# P(X >= 3) = 1 - P(X <= 2)
prob_greater <- 1 - ppois(2, lambda)
cat(sprintf("P(X >= 3) = %.4f\n", prob_greater))
