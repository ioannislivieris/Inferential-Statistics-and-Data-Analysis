# Chapter 5 - Other Discrete Distributions
# Example 2: Hypergeometric Distribution
#   Population N=100, defective K=15, sample n=20

# Parameters
# m = K = defective items in population
# n = N - K = non-defective items
# k = sample size
m <- 15   # defective
n <- 85   # non-defective  (100 - 15)
k <- 20   # sample size

# P(X = 3)
prob_exact <- dhyper(3, m, n, k)
cat(sprintf("P(X = 3) = %.4f\n", prob_exact))

# P(X <= 2)
prob_cumulative <- phyper(2, m, n, k)
cat(sprintf("P(X <= 2) = %.4f\n", prob_cumulative))

# Expected value
expected_value <- k * (m / (m + n))
cat(sprintf("Expected defective: %.2f\n", expected_value))
