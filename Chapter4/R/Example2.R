# Chapter 4 - Poisson Distribution
# Example 2: Call Center Traffic Analysis  Poisson(30)

# Parameter
lambda <- 30

# i. P(X = 25)
prob_exact <- dpois(25, lambda)
cat(sprintf("i. P(X = 25) = %.4f\n", prob_exact))

# ii. P(X > 35) = 1 - P(X <= 35)
prob_greater <- 1 - ppois(35, lambda)
cat(sprintf("ii. P(X > 35) = %.4f\n", prob_greater))

# iii. 95th percentile
percentile_95 <- qpois(0.95, lambda)
cat(sprintf("iii. 95th percentile: %d calls\n", percentile_95))

# Verification
cat(sprintf("Verification: P(X <= %d) = %.4f\n",
            percentile_95, ppois(percentile_95, lambda)))
