# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 4: Σύγκριση Θεωρητικού και Εμπειρικού Τυπικού Σφάλματος
#   N(100, 20), n = 5..200, 1000 προσομοιώσεις

# Population parameters
mu    <- 100
sigma <- 20

# Sample sizes to test
sample_sizes <- seq(5, 200, by = 5)

# Calculate theoretical standard errors
theoretical_se <- sigma / sqrt(sample_sizes)

# Simulate empirical standard errors
set.seed(42)
n_simulations <- 1000
empirical_se  <- sapply(sample_sizes, function(n) {
  sample_means <- replicate(n_simulations,
                             mean(rnorm(n, mean = mu, sd = sigma)))
  sd(sample_means)
})

# Plot
plot(sample_sizes, theoretical_se,
     type = "l", lwd = 2, col = "blue",
     xlab = "Sample Size (n)",
     ylab = "Standard Error",
     main = "Standard Error vs Sample Size",
     ylim = c(0, max(theoretical_se)))

points(sample_sizes, empirical_se,
       pch = 16, col = "red", cex = 0.5)

legend("topright",
       legend = c("Theoretical SE = sigma/sqrt(n)",
                  "Empirical SE (simulated)"),
       col    = c("blue", "red"),
       lwd    = c(2, NA),
       pch    = c(NA, 16))

grid()

# Add annotation showing 1/sqrt(n) relationship
text(150, theoretical_se[1] * 0.8,
     expression(SE == frac(sigma, sqrt(n))),
     cex = 1.5, col = "blue")

# Demonstrate 4x sample size for halving SE
cat("To reduce SE by half, 4x sample size is needed:\n")
cat("  n = 10 -> SE =", round(sigma / sqrt(10), 2), "\n")
cat("  n = 40 -> SE =", round(sigma / sqrt(40), 2), "\n")
