# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 11: Σχεδιασμός Δειγματοληψίας για Δημοσκόπηση
#   N=50000 ψηφοφόροι, 3 ηλικιακές ομάδες, 3 μέθοδοι δειγματοληψίας

library(dplyr)
set.seed(42)

# === Create the voter population ===
N        <- 50000
n_young  <- round(N * 0.30)              # 15000
n_middle <- round(N * 0.40)             # 20000
n_older  <- N - n_young - n_middle      # 15000

population <- data.frame(
  ID       = 1:N,
  AgeGroup = c(rep("Young", n_young),
               rep("Middle", n_middle),
               rep("Older", n_older)),
  SupportsA = c(
    rbinom(n_young,  1, 0.45),
    rbinom(n_middle, 1, 0.52),
    rbinom(n_older,  1, 0.38)
  )
)

true_support <- mean(population$SupportsA)
cat("True support for Candidate A:",
    round(true_support * 100, 2), "%\n\n")

# === Calculate required sample size ===
Z     <- 1.96    # 95% confidence
E     <- 0.03    # Margin of error = 3%
p_est <- 0.5     # Conservative estimate (maximises n)

n_required <- ceiling(Z^2 * p_est * (1 - p_est) / E^2)
cat("Required sample size for +/- 3% margin:", n_required, "\n\n")

n <- n_required  # Use this as sample size

# Proportional allocation for stratified sampling
n_y <- round(n * 0.30)
n_m <- round(n * 0.40)
n_o <- n - n_y - n_m

# === Monte Carlo: Compare three sampling methods ===
num_sims  <- 1000
srs_est   <- numeric(num_sims)
strat_est <- numeric(num_sims)
sys_est   <- numeric(num_sims)

for (i in 1:num_sims) {
  # 1. Simple Random Sampling
  srs         <- population %>% sample_n(n)
  srs_est[i]  <- mean(srs$SupportsA)

  # 2. Stratified Sampling (by age group)
  strat <- bind_rows(
    population %>% filter(AgeGroup == "Young")  %>% sample_n(n_y),
    population %>% filter(AgeGroup == "Middle") %>% sample_n(n_m),
    population %>% filter(AgeGroup == "Older")  %>% sample_n(n_o)
  )
  strat_est[i] <- mean(strat$SupportsA)

  # 3. Systematic Sampling
  k           <- floor(N / n)
  start       <- sample(1:k, 1)
  sys_indices <- seq(start, N, by = k)[1:n]
  sys_indices <- sys_indices[sys_indices <= N]
  sys         <- population[sys_indices, ]
  sys_est[i]  <- mean(sys$SupportsA)
}

# === Results ===
cat("--- Monte Carlo Comparison (1000 simulations) ---\n")
cat("True support:", round(true_support * 100, 2), "%\n\n")

methods <- c("SRS", "Stratified", "Systematic")
means   <- c(mean(srs_est), mean(strat_est), mean(sys_est))
sds     <- c(sd(srs_est),   sd(strat_est),   sd(sys_est))
bias    <- means - true_support

moe_srs   <- quantile(abs(srs_est   - true_support), 0.95)
moe_strat <- quantile(abs(strat_est - true_support), 0.95)
moe_sys   <- quantile(abs(sys_est   - true_support), 0.95)
moes      <- c(moe_srs, moe_strat, moe_sys)

correct_srs   <- mean((srs_est   > 0.5) == (true_support > 0.5))
correct_strat <- mean((strat_est > 0.5) == (true_support > 0.5))
correct_sys   <- mean((sys_est   > 0.5) == (true_support > 0.5))
correct       <- c(correct_srs, correct_strat, correct_sys)

results <- data.frame(
  Method      = methods,
  Mean        = round(means   * 100, 2),
  SD          = round(sds     * 100, 2),
  Bias        = round(bias    * 100, 2),
  MoE_95      = round(moes    * 100, 2),
  Correct_Pct = round(correct * 100, 1)
)
print(results)

# Visualization
par(mfrow = c(1, 3))

hist(srs_est * 100, breaks = 30, col = "steelblue",
     main = "Simple Random Sampling",
     xlab = "Support for A (%)", xlim = c(35, 60))
abline(v = true_support * 100, col = "red",       lwd = 2, lty = 2)
abline(v = 50,                 col = "darkgreen", lwd = 2, lty = 3)

hist(strat_est * 100, breaks = 30, col = "coral",
     main = "Stratified Sampling",
     xlab = "Support for A (%)", xlim = c(35, 60))
abline(v = true_support * 100, col = "red",       lwd = 2, lty = 2)
abline(v = 50,                 col = "darkgreen", lwd = 2, lty = 3)

hist(sys_est * 100, breaks = 30, col = "gold",
     main = "Systematic Sampling",
     xlab = "Support for A (%)", xlim = c(35, 60))
abline(v = true_support * 100, col = "red",       lwd = 2, lty = 2)
abline(v = 50,                 col = "darkgreen", lwd = 2, lty = 3)

par(mfrow = c(1, 1))
