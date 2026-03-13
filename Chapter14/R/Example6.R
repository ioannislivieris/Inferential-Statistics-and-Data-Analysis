# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 6: Έλεγχος Κανονικότητας Υπολοίπων ANOVA (Shapiro-Wilk, Q-Q plot)

# Fit ANOVA model (χρησιμοποιούμε το advertising dataset από το Ex5)
advertising <- data.frame(
  Sales    = c(23, 25, 27, 24, 26,
               30, 32, 28, 31, 29,
               20, 22, 19, 21, 20),
  Strategy = factor(rep(c("Television", "Internet", "Print"), each = 5))
)

anova_model <- aov(Sales ~ Strategy, data = advertising)
res         <- residuals(anova_model)

# Shapiro-Wilk on residuals (preferred over per-group testing)
sw <- shapiro.test(res)
cat("Shapiro-Wilk on residuals: W =", round(sw$statistic, 4),
    ", p =", round(sw$p.value, 4), "\n")
cat("Conclusion:", ifelse(sw$p.value > 0.05,
    "Normality assumption is supported.",
    "Normality assumption may be violated."), "\n")

# Per-group Shapiro-Wilk
cat("\nPer-group Shapiro-Wilk:\n")
for (s in levels(advertising$Strategy)) {
  g  <- advertising$Sales[advertising$Strategy == s]
  sw <- shapiro.test(g)
  cat(sprintf("  %-12s: W = %.4f, p = %.4f\n", s,
              sw$statistic, sw$p.value))
}

# Q-Q plot of residuals
library(ggplot2)
ggplot(data.frame(res = res), aes(sample = res)) +
  stat_qq() + stat_qq_line(color = "red", linewidth = 1) +
  labs(title = "Q-Q Plot of ANOVA Residuals",
       x = "Theoretical Quantiles",
       y = "Sample Quantiles") +
  theme_minimal(base_size = 13)
