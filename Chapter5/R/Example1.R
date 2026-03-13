# Chapter 5 - Other Discrete Distributions
# Example 1: Geometric Distribution  p = 0.3

# Note: R's dgeom/pgeom counts FAILURES before first success.
# To work with TRIALS (X = failures + 1), subtract 1 from the argument.

# Parameter
p <- 0.3

# P(X = 5)  →  5th trial is first success = 4 failures
prob_exact <- dgeom(4, p)
cat(sprintf("P(X = 5) = %.4f\n", prob_exact))

# P(X <= 4)  →  at most 4 trials = at most 3 failures
prob_cumulative <- pgeom(3, p)
cat(sprintf("P(X <= 4) = %.4f\n", prob_cumulative))

# P(X > 6)  →  more than 6 trials = more than 5 failures
prob_greater <- 1 - pgeom(5, p)
cat(sprintf("P(X > 6) = %.4f\n", prob_greater))

# Expected number of trials
expected_trials <- 1 / p
cat(sprintf("Expected trials: %.2f\n", expected_trials))
