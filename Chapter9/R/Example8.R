# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 8: Στρωματοποιημένη Δειγματοληψία — Έλεγχος Ποιότητας
#   3 γραμμές παραγωγής (A:50%, B:30%, C:20%), ελαττωματικά 2/5/8%

library(dplyr)
set.seed(42)

# === Create the population ===
N_A <- 5000; N_B <- 3000; N_C <- 2000
N   <- N_A + N_B + N_C  # Total population = 10000

population <- data.frame(
  ID        = 1:N,
  Line      = c(rep("A", N_A), rep("B", N_B), rep("C", N_C)),
  Defective = c(
    rbinom(N_A, 1, 0.02),  # Line A: 2% defect rate
    rbinom(N_B, 1, 0.05),  # Line B: 5% defect rate
    rbinom(N_C, 1, 0.08)   # Line C: 8% defect rate
  )
)

# True population defect rate
true_rate <- mean(population$Defective)
cat("True population defect rate:",
    round(true_rate * 100, 2), "%\n\n")

# === Proportional stratified sampling (n = 200) ===
n   <- 200
n_A <- round(n * N_A / N)  # 100
n_B <- round(n * N_B / N)  # 60
n_C <- round(n * N_C / N)  # 40

cat("Sample allocation: A =", n_A, ", B =", n_B, ", C =", n_C, "\n")

stratified_sample <- bind_rows(
  population %>% filter(Line == "A") %>% sample_n(n_A),
  population %>% filter(Line == "B") %>% sample_n(n_B),
  population %>% filter(Line == "C") %>% sample_n(n_C)
)

# Estimated defect rate from stratified sample
strat_rate <- mean(stratified_sample$Defective)
cat("Stratified sample defect rate:",
    round(strat_rate * 100, 2), "%\n")

# Standard error of the proportion
strat_se <- sqrt(strat_rate * (1 - strat_rate) / n)
cat("Standard error:", round(strat_se, 4), "\n\n")

# === Monte Carlo comparison: Stratified vs SRS ===
num_simulations <- 1000
strat_estimates <- numeric(num_simulations)
srs_estimates   <- numeric(num_simulations)

for (i in 1:num_simulations) {
  # Stratified sampling
  s <- bind_rows(
    population %>% filter(Line == "A") %>% sample_n(n_A),
    population %>% filter(Line == "B") %>% sample_n(n_B),
    population %>% filter(Line == "C") %>% sample_n(n_C)
  )
  strat_estimates[i] <- mean(s$Defective)

  # Simple random sampling
  srs               <- population %>% sample_n(n)
  srs_estimates[i]  <- mean(srs$Defective)
}

cat("--- Monte Carlo Comparison (1000 simulations) ---\n")
cat("True defect rate:", round(true_rate * 100, 2), "%\n")
cat("Stratified: Mean =", round(mean(strat_estimates) * 100, 2),
    "%, SD =", round(sd(strat_estimates) * 100, 2), "%\n")
cat("SRS:        Mean =", round(mean(srs_estimates) * 100, 2),
    "%, SD =", round(sd(srs_estimates) * 100, 2), "%\n")
cat("Efficiency gain (variance ratio):",
    round(var(srs_estimates) / var(strat_estimates), 2), "\n")

# Visualization
par(mfrow = c(1, 2))
hist(strat_estimates * 100, breaks = 30, col = "steelblue",
     main = "Stratified Sampling", xlab = "Defect Rate (%)",
     xlim = c(0, 10))
abline(v = true_rate * 100, col = "red", lwd = 2, lty = 2)

hist(srs_estimates * 100, breaks = 30, col = "coral",
     main = "Simple Random Sampling", xlab = "Defect Rate (%)",
     xlim = c(0, 10))
abline(v = true_rate * 100, col = "red", lwd = 2, lty = 2)
par(mfrow = c(1, 1))
