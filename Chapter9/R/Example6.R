# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 6: Επίδραση Μεγέθους Δείγματος στο Τυπικό Σφάλμα
#   SE = σ/√n, σ=15

library(ggplot2)

# Define different sample sizes to analyze
sample_sizes  <- c(10, 30, 50, 100, 200, 500)
population_sd <- 15  # Known population standard deviation

# Calculate theoretical standard error for each sample size
standard_errors <- population_sd / sqrt(sample_sizes)

# Create a data frame for analysis and visualization
df <- data.frame(
  SampleSize    = sample_sizes,
  StandardError = standard_errors
)

print("Relationship between sample size and standard error:")
print(df)

# Create visualization showing inverse square root relationship
ggplot(df, aes(x = SampleSize, y = StandardError)) +
  geom_line(color = "blue", size = 1) +
  geom_point(color = "red", size = 3) +
  labs(title    = "Effect of Sample Size on Standard Error",
       subtitle = "Standard error decreases with rate 1/sqrt(n)",
       x = "Sample Size (n)",
       y = "Standard Error SE(x)") +
  theme_minimal() +
  scale_x_continuous(breaks = sample_sizes)

# Demonstrate the inverse square root relationship
cat("\nTo reduce standard error by half,",
    "we need a 4-fold increase in sample size:\n")
cat("  n = 10 -> SE =", round(standard_errors[1], 2), "\n")
cat("  n = 40 -> SE =", round(population_sd / sqrt(40), 2),
    "(half of the SE at n=10)\n")
