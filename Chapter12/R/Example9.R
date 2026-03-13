# Chapter 12 - Διαστήματα Εμπιστοσύνης
# Example 9: Οπτικοποίηση Πολλαπλών Διαστημάτων Εμπιστοσύνης
#   Monte Carlo: 100 δείγματα n=30 από N(100,15), 95% CI
#   Επίδειξη ότι ~95% των διαστημάτων περιέχουν τη μ=100

set.seed(123)

# True population parameters
mu_true    <- 100
sigma_true <- 15
n          <- 30
conf_level <- 0.95
n_sim      <- 100

# Critical value
alpha  <- 1 - conf_level
z_crit <- qnorm(1 - alpha / 2)
se_pop <- sigma_true / sqrt(n)   # known σ → use z

# Simulate n_sim confidence intervals
lower       <- numeric(n_sim)
upper       <- numeric(n_sim)
contains_mu <- logical(n_sim)

for (i in 1:n_sim) {
  samp        <- rnorm(n, mean = mu_true, sd = sigma_true)
  xbar        <- mean(samp)
  margin      <- z_crit * se_pop
  lower[i]    <- xbar - margin
  upper[i]    <- xbar + margin
  contains_mu[i] <- lower[i] <= mu_true & mu_true <= upper[i]
}

coverage <- mean(contains_mu)
cat(sprintf("True μ:             %.1f\n", mu_true))
cat(sprintf("Confidence level:   %.0f%%\n", conf_level * 100))
cat(sprintf("Number of CIs:      %d\n", n_sim))
cat(sprintf("CIs containing μ:   %d\n", sum(contains_mu)))
cat(sprintf("Empirical coverage: %.1f%%\n", coverage * 100))

# Plot all CIs
x_range <- range(c(lower, upper))
plot(NULL,
     xlim = x_range,
     ylim = c(1, n_sim),
     xlab = "Value",
     ylab = "Simulation number",
     main = sprintf("%d Confidence Intervals — %.0f%% Confidence Level",
                    n_sim, conf_level * 100))

abline(v = mu_true, col = "red", lwd = 2, lty = 2)

for (i in 1:n_sim) {
  col_i <- ifelse(contains_mu[i], "steelblue", "darkorange")
  segments(lower[i], i, upper[i], i, col = col_i, lwd = 0.8)
  points((lower[i] + upper[i]) / 2, i,
         pch = 20, cex = 0.4, col = col_i)
}

legend("topright",
       legend = c("True μ", "Contains μ", "Misses μ"),
       col    = c("red", "steelblue", "darkorange"),
       lty    = c(2, 1, 1), lwd = 2, cex = 0.9)

text(x_range[1] + 0.3, n_sim - 3,
     sprintf("Coverage: %.1f%%", coverage * 100),
     pos = 4, cex = 1.1, font = 2)
