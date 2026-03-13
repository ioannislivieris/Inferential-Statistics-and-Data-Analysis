# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 5: Δειγματοληπτική Κατανομή Αναλογίας
#   p=0.3, n = 20, 50, 100, 500 — 10000 προσομοιώσεις

# Parameters
p            <- 0.3  # Population proportion
sample_sizes <- c(20, 50, 100, 500)

set.seed(42)
n_simulations <- 10000
par(mfrow = c(2, 2))

for (n in sample_sizes) {
  # Generate sample proportions
  sample_props <- replicate(n_simulations, {
    sum(rbinom(n, 1, p)) / n
  })

  # Theoretical parameters
  se <- sqrt(p * (1 - p) / n)

  # Check conditions for normal approximation
  np_val    <- n * p
  n_1_p_val <- n * (1 - p)
  conditions_met <- (np_val >= 10 & n_1_p_val >= 10)

  # Histogram
  hist(sample_props, breaks = 30, freq = FALSE,
       col  = "lightblue", border = "black",
       main = paste0("n = ", n,
                     ifelse(conditions_met,
                            " (Normal approx. valid)",
                            " (Normal approx. questionable)")),
       xlab = "Sample Proportion",
       ylab = "Density")

  # Overlay normal curve
  x <- seq(min(sample_props), max(sample_props), length.out = 200)
  y <- dnorm(x, mean = p, sd = se)
  lines(x, y, col = "red", lwd = 2)

  # Add vertical line at p
  abline(v = p, col = "darkgreen", lwd = 2, lty = 2)

  # Add text with conditions check
  legend("topright",
         legend = c(paste("np =", np_val),
                    paste("n(1-p) =", n_1_p_val)),
         bty = "n", cex = 0.9)
}

par(mfrow = c(1, 1))
