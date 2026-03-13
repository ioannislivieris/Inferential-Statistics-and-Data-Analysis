# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 9: Δειγματοληψία Κατά Συστάδες vs Στρωματοποιημένη
#   80 καταστήματα, 4 περιφέρειες, 10 επιλεγμένα, 30 πελάτες/κατάστημα

library(dplyr)
set.seed(123)

# === Create the population ===
stores_per_region    <- 20
customers_per_store  <- 50
regions              <- c("North", "South", "East", "West")
region_means         <- c(7.5, 6.8, 7.2, 6.5)
sigma                <- 1.5

population <- data.frame()
store_id   <- 1

for (r in 1:length(regions)) {
  for (s in 1:stores_per_region) {
    store_data <- data.frame(
      StoreID      = store_id,
      Region       = regions[r],
      Satisfaction = rnorm(customers_per_store, region_means[r], sigma)
    )
    population <- bind_rows(population, store_data)
    store_id   <- store_id + 1
  }
}

# Clip satisfaction scores to [1, 10]
population$Satisfaction <- pmin(pmax(population$Satisfaction, 1), 10)

true_mean <- mean(population$Satisfaction)
cat("Total population size:", nrow(population), "customers\n")
cat("True mean satisfaction:", round(true_mean, 3), "\n\n")

# === Cluster Sampling: Select 10 stores, survey 30 customers each ===
num_clusters       <- 10
customers_sampled  <- 30

selected_stores <- sample(1:80, num_clusters, replace = FALSE)
cat("Selected stores:", selected_stores, "\n")

cluster_sample <- population %>%
  filter(StoreID %in% selected_stores) %>%
  group_by(StoreID) %>%
  sample_n(customers_sampled) %>%
  ungroup()

cat("Sample size:", nrow(cluster_sample), "customers\n")
cat("Cluster estimate:", round(mean(cluster_sample$Satisfaction), 3), "\n")

# Check regional representation
cat("\nRegions represented in cluster sample:\n")
print(table(cluster_sample$Region))

# === Stratified Sampling for comparison ===
n_total      <- nrow(cluster_sample)  # Same total sample size
n_per_region <- round(n_total / length(regions))

stratified_sample <- population %>%
  group_by(Region) %>%
  sample_n(n_per_region) %>%
  ungroup()

cat("\nStratified estimate:",
    round(mean(stratified_sample$Satisfaction), 3), "\n")

# === Monte Carlo Comparison ===
num_sims   <- 1000
cluster_est <- numeric(num_sims)
strat_est   <- numeric(num_sims)

for (i in 1:num_sims) {
  sel <- sample(1:80, num_clusters, replace = FALSE)
  cs  <- population %>%
    filter(StoreID %in% sel) %>%
    group_by(StoreID) %>%
    sample_n(customers_sampled) %>%
    ungroup()
  cluster_est[i] <- mean(cs$Satisfaction)

  ss <- population %>%
    group_by(Region) %>%
    sample_n(n_per_region) %>%
    ungroup()
  strat_est[i] <- mean(ss$Satisfaction)
}

cat("\n--- Monte Carlo Comparison (1000 simulations) ---\n")
cat("True mean:", round(true_mean, 3), "\n")
cat("Cluster:     Mean =", round(mean(cluster_est), 3),
    ", SD =", round(sd(cluster_est), 4), "\n")
cat("Stratified:  Mean =", round(mean(strat_est), 3),
    ", SD =", round(sd(strat_est), 4), "\n")
cat("Cluster/Stratified variance ratio:",
    round(var(cluster_est) / var(strat_est), 2), "\n")

# Visualization
par(mfrow = c(1, 2))
hist(cluster_est, breaks = 30, col = "steelblue",
     main = "Cluster Sampling", xlab = "Mean Satisfaction",
     xlim = range(c(cluster_est, strat_est)))
abline(v = true_mean, col = "red", lwd = 2, lty = 2)

hist(strat_est, breaks = 30, col = "coral",
     main = "Stratified Sampling", xlab = "Mean Satisfaction",
     xlim = range(c(cluster_est, strat_est)))
abline(v = true_mean, col = "red", lwd = 2, lty = 2)
par(mfrow = c(1, 1))
