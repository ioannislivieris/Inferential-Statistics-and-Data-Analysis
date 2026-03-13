# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 2: Ανάλυση Ζευγαρωτών Δεδομένων (Paired t-test)

set.seed(456)
n <- 12

# Simulate weight data
before       <- round(rnorm(n, mean = 85, sd = 12), 1)
weight_loss  <- round(rnorm(n, mean = 3.5, sd = 2), 1)
after        <- before - weight_loss

weight_data <- data.frame(
  Subject    = 1:n,
  Before     = before,
  After      = after,
  Difference = before - after
)
print(weight_data)

cat("Mean before:", round(mean(weight_data$Before), 2), "kg\n")
cat("Mean after :", round(mean(weight_data$After),  2), "kg\n")
cat("Mean diff  :", round(mean(weight_data$Difference), 2), "kg\n\n")

# Paired t-test (one-sided: loss > 0 means before > after)
paired_test <- t.test(weight_data$Before, weight_data$After,
                      paired = TRUE, alternative = "greater")
print(paired_test)

# Manual calculation
d_bar  <- mean(weight_data$Difference)
s_d    <- sd(weight_data$Difference)
se_d   <- s_d / sqrt(n)
t_stat <- d_bar / se_d
df     <- n - 1
p_val  <- pt(t_stat, df = df, lower.tail = FALSE)

cat("\n--- Manual Calculation ---\n")
cat("d-bar:", round(d_bar, 3), "kg\n")
cat("s_d  :", round(s_d, 3),   "kg\n")
cat("SE_d :", round(se_d, 3),  "kg\n")
cat("t    :", round(t_stat, 3), "\n")
cat("df   :", df, "\n")
cat("p-value (one-sided):", round(p_val, 4), "\n")

# 95% Confidence interval
t_crit <- qt(0.975, df = df)
ci_lo  <- d_bar - t_crit * se_d
ci_hi  <- d_bar + t_crit * se_d
cat("95% CI for mu_d: [", round(ci_lo, 2), ",", round(ci_hi, 2), "] kg\n")

# Normality check on differences
sw <- shapiro.test(weight_data$Difference)
cat("\nShapiro-Wilk on differences: W =", round(sw$statistic, 4),
    ", p =", round(sw$p.value, 4), "\n")

# Visualization: paired plot
library(ggplot2)
library(tidyr)

plot_long <- pivot_longer(weight_data, cols = c(Before, After),
                          names_to = "Time", values_to = "Weight")
plot_long$Time <- factor(plot_long$Time, levels = c("Before", "After"))

ggplot(plot_long, aes(x = Time, y = Weight, group = Subject)) +
  geom_line(color = "steelblue", alpha = 0.5) +
  geom_point(aes(color = Time), size = 3) +
  labs(
    title    = "Individual Weight Changes",
    subtitle = paste("Mean loss:", round(d_bar, 2), "kg,",
                     "p-value =", round(p_val, 4)),
    y = "Weight (kg)", x = ""
  ) +
  theme_minimal(base_size = 13) + theme(legend.position = "right")
