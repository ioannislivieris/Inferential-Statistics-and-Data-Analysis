# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 7: Δειγματοληπτική Κατανομή — Παράδειγμα Ζαριού
#   Πληθυσμός {1..6}, n=2, 10000 επαναλήψεις

library(ggplot2)
library(gridExtra)
set.seed(200)

# Define the population: outcomes of a fair six-sided die
population <- 1:6

# Calculate population parameters
pop_mean <- mean(population)
pop_sd   <- sd(population)
pop_var  <- var(population)

cat("Population (fair die) parameters:\n")
cat("  Population mean (mu) =", pop_mean, "\n")
cat("  Population variance (sigma^2) =", pop_var, "\n")
cat("  Population standard deviation (sigma) =", round(pop_sd, 3), "\n\n")

# Simulation: Roll 2 dice and calculate their mean
num_samples  <- 10000  # Number of simulated experiments
sample_size  <- 2      # Number of dice rolled each time
sample_means <- numeric(num_samples)

for (i in 1:num_samples) {
  dice_rolls      <- sample(population, sample_size, replace = TRUE)
  sample_means[i] <- mean(dice_rolls)
}

# Analyse the sampling distribution
cat("Sampling distribution statistics (n = 2):\n")
cat("  Mean of sample means E[x] =", round(mean(sample_means), 3),
    "(theoretical: mu =", pop_mean, ")\n")
cat("  Variance of sample means Var(x) =", round(var(sample_means), 3),
    "(theoretical: sigma^2/n =", round(pop_var / sample_size, 3), ")\n")
cat("  Standard error SE(x) =", round(sd(sample_means), 3),
    "(theoretical: sigma/sqrt(n) =",
    round(pop_sd / sqrt(sample_size), 3), ")\n")

# Create side-by-side visualization
p1 <- ggplot(data.frame(x = population), aes(x = factor(x))) +
  geom_bar(fill = "steelblue", alpha = 0.7) +
  labs(title = "Population Distribution (Fair Die)",
       x = "Outcome",
       y = "Frequency") +
  theme_minimal()

p2 <- ggplot(data.frame(means = sample_means), aes(x = means)) +
  geom_histogram(aes(y = ..density..),
                 bins  = 20,
                 fill  = "coral",
                 alpha = 0.7) +
  geom_vline(xintercept = pop_mean,
             color    = "darkgreen",
             linetype = "dashed",
             size     = 1) +
  labs(title = "Sampling Distribution of Mean (n=2)",
       x = "Sample Mean",
       y = "Density") +
  theme_minimal()

grid.arrange(p1, p2, ncol = 2)
