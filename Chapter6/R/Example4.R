# Chapter 6 - Κανονική Κατανομή
# Example 4: Προσομοίωση και Επαλήθευση  X ~ N(100, 15²), n = 10.000

# Parameters
mu    <- 100
sigma <- 15
n     <- 10000

# Simulation
set.seed(42)
samples <- rnorm(n, mean = mu, sd = sigma)

# Verify empirical rule
within_1sd <- sum(samples >= mu - sigma &
                    samples <= mu + sigma) / n
within_2sd <- sum(samples >= mu - 2*sigma &
                    samples <= mu + 2*sigma) / n
within_3sd <- sum(samples >= mu - 3*sigma &
                    samples <= mu + 3*sigma) / n

cat("Empirical Rule Verification:\n")
cat(sprintf("Within 1 SD: %.2f%% (Expected: 68%%)\n",
            within_1sd * 100))
cat(sprintf("Within 2 SD: %.2f%% (Expected: 95%%)\n",
            within_2sd * 100))
cat(sprintf("Within 3 SD: %.2f%% (Expected: 99.7%%)\n",
            within_3sd * 100))

# Summary statistics
cat(sprintf("\nSample Mean: %.2f (True: %.2f)\n",
            mean(samples), mu))
cat(sprintf("Sample SD: %.2f (True: %.2f)\n",
            sd(samples), sigma))

# Histogram with overlay
hist(samples, breaks = 50, freq = FALSE,
     col = 'lightblue', border = 'black',
     main = paste0('Simulation: N(', mu, ', ', sigma, '^2)'),
     xlab = 'x', ylab = 'Density')

# Theoretical density curve
x_theory <- seq(min(samples), max(samples), length.out = 200)
y_theory  <- dnorm(x_theory, mean = mu, sd = sigma)
lines(x_theory, y_theory, col = 'red', lwd = 2)

legend('topright',
       legend = c('Simulated Data', 'Theoretical Density'),
       fill   = c('lightblue', NA),
       border = c('black', NA),
       col    = c(NA, 'red'),
       lwd    = c(NA, 2))
