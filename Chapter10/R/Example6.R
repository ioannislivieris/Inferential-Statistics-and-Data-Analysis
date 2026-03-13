# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 6: Ρυθμός Σύγκλισης ΚΟΘ — Shapiro-Wilk τεστ
#   Σύγκριση 4 κατανομών × 5 μεγέθη δείγματος

set.seed(42)
n_simulations <- 500
sample_sizes  <- c(5, 10, 30, 50, 100)

# Define distributions as named list
distributions <- list(
  "Uniform(0,10)"      = function(n) runif(n, 0, 10),
  "Exponential(l=0.5)" = function(n) rexp(n, rate = 0.5),
  "Chi-square(df=3)"   = function(n) rchisq(n, df = 3),
  "Normal(50,10)"      = function(n) rnorm(n, mean = 50, sd = 10)
)

# For each distribution and sample size, compute
# proportion of Shapiro-Wilk tests that accept normality (p > 0.05)
results <- matrix(NA,
                  nrow = length(distributions),
                  ncol = length(sample_sizes),
                  dimnames = list(names(distributions),
                                  paste0("n=", sample_sizes)))

for (d in seq_along(distributions)) {
  for (s in seq_along(sample_sizes)) {
    n        <- sample_sizes[s]
    p_values <- numeric(n_simulations)
    for (i in 1:n_simulations) {
      means      <- replicate(30, mean(distributions[[d]](n)))
      p_values[i] <- shapiro.test(means)$p.value
    }
    # Proportion where normality is NOT rejected at alpha=0.05
    results[d, s] <- mean(p_values > 0.05)
  }
}

cat("Proportion of Shapiro-Wilk tests accepting normality (p > 0.05):\n\n")
print(round(results, 3))

# Visualization: heatmap-style matrix plot
par(mar = c(5, 10, 4, 2))
image(t(results),
      x    = 1:length(sample_sizes),
      y    = 1:length(distributions),
      axes = FALSE,
      col  = heat.colors(20),
      main = "CLT Convergence: Proportion Accepting Normality",
      xlab = "Sample Size", ylab = "")

axis(1, at = 1:length(sample_sizes),
     labels = paste0("n=", sample_sizes))
axis(2, at = 1:length(distributions),
     labels = names(distributions), las = 2)

# Add text labels to cells
for (i in 1:length(sample_sizes)) {
  for (j in 1:length(distributions)) {
    text(i, j, round(results[j, i], 2), cex = 0.9)
  }
}

par(mar = c(5, 4, 4, 2))  # Reset margins
