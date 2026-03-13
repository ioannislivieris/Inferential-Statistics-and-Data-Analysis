# Chapter 5 - Other Discrete Distributions
# Example 5: Geometric Distribution Simulation  p = 0.2  (1000 observations)

# Parameter
p               <- 0.2
num_simulations <- 1000

# Simulation — rgeom returns failures, add 1 to convert to trials
set.seed(42)
simulated_data <- rgeom(num_simulations, p) + 1

# Theoretical distribution (trials)
x               <- 1:20
theoretical_pmf <- dgeom(x - 1, p)

# Plot
hist(simulated_data, breaks = seq(0.5, 20.5, 1),
     freq   = FALSE, col = 'lightblue', border = 'black',
     xlab   = 'Number of Trials',
     ylab   = 'Frequency / Probability',
     main   = paste0('Simulation vs Theoretical: Geom(', p, ')'),
     xlim   = c(0, 20))

# Overlay theoretical line
lines(x, theoretical_pmf, col = 'red', lwd = 2, type = 'b', pch = 19)

legend('topright',
       legend = c('Simulation', 'Theoretical'),
       fill   = c('lightblue', NA), border = c('black', NA),
       col    = c(NA, 'red'), lwd = c(NA, 2), pch = c(NA, 19))

# Statistics comparison
cat(sprintf("Simulation Mean:       %.2f\n", mean(simulated_data)))
cat(sprintf("Theoretical Mean:      %.2f\n", 1 / p))
cat(sprintf("Simulation Std Dev:    %.2f\n", sd(simulated_data)))
cat(sprintf("Theoretical Std Dev:   %.2f\n", sqrt((1 - p) / p^2)))
