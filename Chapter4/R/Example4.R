# Chapter 4 - Poisson Distribution
# Example 4: Simulation  Poisson(6) — 1000 observations

# Parameter
lambda          <- 6
num_simulations <- 1000

# Simulation
set.seed(42)
simulated_data <- rpois(num_simulations, lambda)

# Theoretical distribution
x               <- 0:20
theoretical_pmf <- dpois(x, lambda)

# Plot
hist(simulated_data, breaks = seq(-0.5, 20.5, 1),
     freq   = FALSE, col = 'lightgreen', border = 'black',
     xlab   = 'Number of Events',
     ylab   = 'Frequency / Probability',
     main   = paste0('Simulation vs Theoretical: Poisson(', lambda, ')'))

# Overlay theoretical line
lines(x, theoretical_pmf, col = 'red', lwd = 2, type = 'b', pch = 19)

legend('topright',
       legend = c('Simulation', 'Theoretical Distribution'),
       fill   = c('lightgreen', NA), border = c('black', NA),
       col    = c(NA, 'red'), lwd = c(NA, 2), pch = c(NA, 19))

# Statistics comparison
cat(sprintf("Simulation Mean:       %.2f\n", mean(simulated_data)))
cat(sprintf("Theoretical Mean:      %.2f\n", lambda))
cat(sprintf("Simulation Std Dev:    %.2f\n", sd(simulated_data)))
cat(sprintf("Theoretical Std Dev:   %.2f\n", sqrt(lambda)))
