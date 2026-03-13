# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 1: ΚΟΘ με Ομοιόμορφη Κατανομή U(0,10)
#   n = 5, 10, 30, 100 — 10000 προσομοιώσεις ανά μέγεθος

set.seed(42)
n_simulations <- 10000
sample_sizes  <- c(5, 10, 30, 100)

# Theoretical parameters for U(0,10)
mu    <- 5
sigma <- sqrt((10 - 0)^2 / 12)

# Create layout for plots
par(mfrow = c(2, 2))

for (n in sample_sizes) {
  # Generate sample means from uniform distribution
  sample_means <- replicate(n_simulations, {
    mean(runif(n, min = 0, max = 10))
  })

  se <- sigma / sqrt(n)

  # Histogram
  hist(sample_means, breaks = 50, freq = FALSE,
       col    = "lightblue", border = "black",
       main   = paste("Sample Size n =", n),
       xlab   = "Sample Mean",
       ylab   = "Density")

  # Overlay theoretical normal curve
  x <- seq(min(sample_means), max(sample_means), length.out = 200)
  y <- dnorm(x, mean = mu, sd = se)
  lines(x, y, col = "red", lwd = 2)

  # Add vertical line at population mean
  abline(v = mu, col = "darkgreen", lwd = 2, lty = 2)

  legend("topright",
         legend = c("Simulated", "Theoretical N", "Pop. Mean"),
         col    = c("lightblue", "red", "darkgreen"),
         lwd    = c(NA, 2, 2),
         lty    = c(NA, 1, 2),
         fill   = c("lightblue", NA, NA))
}

par(mfrow = c(1, 1))
