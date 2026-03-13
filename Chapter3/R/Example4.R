# Chapter 3 - Binomial Distribution
# Example 4: Simulation  B(50, 0.3) — 1000 experiments

# Parameters
n               <- 50
p               <- 0.3
num_simulations <- 1000

# Simulation
set.seed(42)
simulated_data <- rbinom(num_simulations, n, p)

# Theoretical distribution
x               <- 0:n
theoretical_pmf <- dbinom(x, n, p)

# Plot
hist(simulated_data, breaks = seq(-0.5, n + 0.5, 1),
     freq   = FALSE, col = 'lightblue', border = 'black',
     xlab   = 'Number of Successes',
     ylab   = 'Frequency / Probability',
     main   = paste0('Simulation vs Theoretical Distribution: B(', n, ', ', p, ')'))

# Overlay theoretical line
lines(x, theoretical_pmf, col = 'red', lwd = 2, type = 'b', pch = 19)

legend('topright',
       legend = c('Simulation', 'Theoretical Distribution'),
       fill   = c('lightblue', NA), border = c('black', NA),
       col    = c(NA, 'red'), lwd = c(NA, 2), pch = c(NA, 19))

# Statistics comparison
cat(sprintf("Simulation Mean:       %.2f\n", mean(simulated_data)))
cat(sprintf("Theoretical Mean:      %.2f\n", n * p))
cat(sprintf("Simulation Std Dev:    %.2f\n", sd(simulated_data)))
cat(sprintf("Theoretical Std Dev:   %.2f\n", sqrt(n * p * (1 - p))))
