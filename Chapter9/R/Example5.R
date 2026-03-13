# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 5: Προσομοίωση Δειγματοληπτικού Σφάλματος
#   N=10000, μ=100, σ=15, n=30, 1000 δείγματα

library(ggplot2)
set.seed(100)

# Create a large population with known parameters
population_mean <- 100
population_sd   <- 15
N               <- 10000

population <- rnorm(N, mean = population_mean, sd = population_sd)

# Calculate actual population parameters
mu    <- mean(population)
sigma <- sd(population)

cat("Population parameters:\n")
cat("  True mean (mu) =", round(mu, 2), "\n")
cat("  True standard deviation (sigma) =", round(sigma, 2), "\n\n")

# Simulation: Draw many samples and calculate their means
num_samples  <- 1000  # Number of samples to draw
sample_size  <- 30    # Size of each sample
sample_means <- numeric(num_samples)

for (i in 1:num_samples) {
  sample_data      <- sample(population, sample_size)
  sample_means[i]  <- mean(sample_data)
}

# Analyse the distribution of sample means
cat("Sampling distribution statistics:\n")
cat("  Mean of sample means:",
    round(mean(sample_means), 2),
    "(theoretical: mu =", mu, ")\n")
cat("  Standard deviation of sample means:",
    round(sd(sample_means), 2), "\n")
cat("  Theoretical standard error (sigma/sqrt(n)):",
    round(sigma / sqrt(sample_size), 2), "\n")

# Create visualization of the sampling distribution
df <- data.frame(SampleMeans = sample_means)

ggplot(df, aes(x = SampleMeans)) +
  geom_histogram(aes(y = ..density..),
                 bins  = 30,
                 fill  = "steelblue",
                 alpha = 0.7) +
  geom_density(color = "red", size = 1) +
  geom_vline(xintercept = mu,
             color    = "darkgreen",
             linetype = "dashed",
             size     = 1) +
  labs(title    = "Distribution of Sample Means (Sampling Distribution)",
       subtitle = paste("Sample size n =", sample_size,
                        ", Number of samples =", num_samples),
       x = "Sample Mean",
       y = "Density") +
  theme_minimal()
