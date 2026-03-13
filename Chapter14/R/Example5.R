# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 5: One-Way ANOVA — Πλήρης Ανάλυση (διαφήμιση)

# Dataset
advertising <- data.frame(
  Sales    = c(23, 25, 27, 24, 26,
               30, 32, 28, 31, 29,
               20, 22, 19, 21, 20),
  Strategy = factor(rep(c("Television", "Internet", "Print"), each = 5))
)

# --- Descriptive statistics ---
library(dplyr)
desc <- advertising %>%
  group_by(Strategy) %>%
  summarise(
    n    = n(),
    Mean = mean(Sales),
    SD   = sd(Sales),
    Min  = min(Sales),
    Max  = max(Sales)
  )
print(desc)

# --- Visualization ---
library(ggplot2)
ggplot(advertising, aes(x = Strategy, y = Sales, fill = Strategy)) +
  geom_boxplot(alpha = 0.7, width = 0.5) +
  geom_jitter(width = 0.1, alpha = 0.5, size = 2) +
  stat_summary(fun = mean, geom = "point", shape = 23,
               size = 4, fill = "white") +
  labs(
    title    = "Sales by Advertising Strategy",
    subtitle = "Diamonds indicate group means",
    y = "Sales (thousands EUR)", x = "Strategy"
  ) +
  theme_minimal(base_size = 13) + theme(legend.position = "none")

# --- One-Way ANOVA ---
anova_model   <- aov(Sales ~ Strategy, data = advertising)
anova_summary <- summary(anova_model)
print(anova_summary)

# Extract key values
f_stat  <- anova_summary[[1]]$`F value`[1]
p_value <- anova_summary[[1]]$`Pr(>F)`[1]
SSB     <- anova_summary[[1]]$`Sum Sq`[1]
SST     <- sum(anova_summary[[1]]$`Sum Sq`)
cat("\nF-statistic:", round(f_stat, 3), "\n")
cat("p-value    :", format(p_value, scientific = TRUE), "\n")

# --- Effect size ---
eta_sq  <- SSB / SST
omega_sq <- (SSB - (2-1)*anova_summary[[1]]$`Mean Sq`[2]) /
            (SST + anova_summary[[1]]$`Mean Sq`[2])
cat("eta-squared  :", round(eta_sq, 4),
    "(", ifelse(eta_sq < 0.06, "small",
         ifelse(eta_sq < 0.14, "medium", "large")), ")\n")
cat("omega-squared:", round(omega_sq, 4), "\n")

# --- Decision ---
if (p_value < 0.05) {
  cat("\nDecision: Reject H0. At least one group mean differs.\n")
} else {
  cat("\nDecision: Fail to reject H0.\n")
}
