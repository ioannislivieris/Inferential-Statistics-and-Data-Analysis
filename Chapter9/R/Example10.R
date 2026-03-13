# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 10: Μεροληψία Μη Απόκρισης — Ανίχνευση και Διόρθωση
#   N=5000, ικανοποίηση~N(55,18), P(απόκριση) εξαρτάται από ικανοποίηση

set.seed(456)

# === Create the population ===
N          <- 5000
population <- data.frame(
  ID           = 1:N,
  Satisfaction = rnorm(N, mean = 55, sd = 18)
)
population$Satisfaction <- pmin(pmax(population$Satisfaction, 1), 100)

true_mean <- mean(population$Satisfaction)
cat("True population mean satisfaction:", round(true_mean, 2), "\n\n")

# === Model response probability as function of satisfaction ===
# Higher satisfaction -> higher probability of responding
population$ResponseProb <- 0.2 + 0.6 *
  (population$Satisfaction - 1) / 99

# === Draw sample and simulate non-response ===
n          <- 500
sample_ids <- sample(1:N, n, replace = FALSE)
sample_data <- population[sample_ids, ]

# Determine who responds based on their response probability
sample_data$Responds <- rbinom(n, 1, sample_data$ResponseProb)

respondents <- sample_data[sample_data$Responds == 1, ]
cat("Original sample size:", n, "\n")
cat("Number of respondents:", nrow(respondents), "\n")
cat("Response rate:", round(nrow(respondents) / n * 100, 1), "%\n\n")

# === Calculate bias ===
naive_estimate <- mean(respondents$Satisfaction)
bias           <- naive_estimate - true_mean
cat("Naive estimate (respondents only):", round(naive_estimate, 2), "\n")
cat("True population mean:", round(true_mean, 2), "\n")
cat("Bias:", round(bias, 2), "\n\n")

# === Show that increasing sample size does NOT reduce bias ===
sample_sizes <- c(100, 200, 500, 1000, 2000)
cat("--- Effect of sample size on bias ---\n")

for (sz in sample_sizes) {
  biases <- numeric(200)
  for (j in 1:200) {
    ids  <- sample(1:N, min(sz, N), replace = FALSE)
    s    <- population[ids, ]
    s$Responds <- rbinom(nrow(s), 1, s$ResponseProb)
    resp <- s[s$Responds == 1, ]
    biases[j] <- mean(resp$Satisfaction) - true_mean
  }
  cat("n =", sz, ": Mean bias =", round(mean(biases), 2),
      ", SD of estimates =", round(sd(biases), 2), "\n")
}

# === Weighted estimation to correct for non-response ===
cat("\n--- Weighted estimation (correction) ---\n")

respondents$Weight <- 1 / respondents$ResponseProb
weighted_estimate  <- weighted.mean(respondents$Satisfaction,
                                    respondents$Weight)

cat("Naive (unweighted) estimate:", round(naive_estimate, 2), "\n")
cat("Weighted estimate:", round(weighted_estimate, 2), "\n")
cat("True mean:", round(true_mean, 2), "\n")
cat("Bias (naive):", round(naive_estimate - true_mean, 2), "\n")
cat("Bias (weighted):", round(weighted_estimate - true_mean, 2), "\n")

# Visualization
par(mfrow = c(1, 2))

hist(population$Satisfaction, breaks = 30, col = "lightgray",
     main = "Population vs Respondents", xlab = "Satisfaction",
     freq = FALSE)
hist(respondents$Satisfaction, breaks = 30,
     col = rgb(1, 0, 0, 0.4), add = TRUE, freq = FALSE)
abline(v = true_mean,      col = "blue", lwd = 2, lty = 2)
abline(v = naive_estimate, col = "red",  lwd = 2, lty = 2)
legend("topright",
       legend = c("Population", "Respondents", "True mean", "Naive est."),
       fill   = c("lightgray", rgb(1, 0, 0, 0.4), NA, NA),
       border = c("black", "black", NA, NA),
       lty    = c(NA, NA, 2, 2),
       col    = c(NA, NA, "blue", "red"),
       lwd    = c(NA, NA, 2, 2), cex = 0.8)

plot(population$Satisfaction, population$ResponseProb,
     pch = 20, cex = 0.3, col = "gray",
     main = "Response Probability vs Satisfaction",
     xlab = "Satisfaction", ylab = "P(Response)")
points(respondents$Satisfaction, respondents$ResponseProb,
       pch = 20, cex = 0.5, col = "red")
legend("bottomright",
       c("Population", "Respondents"),
       col = c("gray", "red"), pch = 20, cex = 0.8)
par(mfrow = c(1, 1))
