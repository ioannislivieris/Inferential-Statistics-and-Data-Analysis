# Chapter 5 - Other Discrete Distributions
# Example 3: Negative Binomial Distribution  r=5, p=0.4

# Note: R's dnbinom counts FAILURES before the r-th success.
# X = total trials = failures + r  →  failures = X - r

# Parameters
r <- 5    # number of successes required
p <- 0.4  # probability of success per trial

# P(X = 12 total trials) → 12 - 5 = 7 failures before 5th success
prob_exact <- dnbinom(7, r, p)
cat(sprintf("P(X = 12 trials) = %.4f\n", prob_exact))

# Expected number of trials
expected_trials <- r / p
cat(sprintf("Expected trials: %.2f\n", expected_trials))

# Variance (for number of trials)
variance <- r * (1 - p) / (p^2)
cat(sprintf("Variance: %.2f\n", variance))
