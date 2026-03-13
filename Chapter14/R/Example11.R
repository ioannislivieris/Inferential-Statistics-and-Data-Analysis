# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 11: Πλήρης ANOVA με Post-hoc (Τρεις Μέθοδοι Διδασκαλίας)

set.seed(42)
n_per_group <- 8

# 1. Simulate data
education <- data.frame(
  Score  = c(rnorm(n_per_group, mean = 72, sd = 8),
             rnorm(n_per_group, mean = 81, sd = 7),
             rnorm(n_per_group, mean = 85, sd = 9)),
  Method = factor(rep(c("Traditional", "Interactive", "Flipped"),
                      each = n_per_group))
)

# 2. Descriptive statistics
library(dplyr)
desc <- education %>%
  group_by(Method) %>%
  summarise(
    n    = n(),
    Mean = round(mean(Score), 2),
    SD   = round(sd(Score), 2),
    Min  = round(min(Score), 2),
    Max  = round(max(Score), 2)
  )
cat("=== Descriptive Statistics ===\n"); print(desc)

# 3. Check assumptions
anova_model <- aov(Score ~ Method, data = education)

sw <- shapiro.test(residuals(anova_model))
cat("\nShapiro-Wilk (residuals): W =", round(sw$statistic, 4),
    ", p =", round(sw$p.value, 4), "\n")
cat("Normality:", ifelse(sw$p.value > 0.05, "Supported", "Violated"), "\n")

library(car)
lev <- leveneTest(Score ~ Method, data = education)
cat("\nLevene test: F =", round(lev$`F value`[1], 4),
    ", p =", round(lev$`Pr(>F)`[1], 4), "\n")
cat("Homoscedasticity:", ifelse(lev$`Pr(>F)`[1] > 0.05,
    "Supported", "Violated"), "\n")

# 4. One-Way ANOVA
anova_sum <- summary(anova_model)
cat("\n=== ANOVA Table ===\n"); print(anova_sum)

SSB     <- anova_sum[[1]]$`Sum Sq`[1]
SST     <- sum(anova_sum[[1]]$`Sum Sq`)
f_stat  <- anova_sum[[1]]$`F value`[1]
p_value <- anova_sum[[1]]$`Pr(>F)`[1]

eta_sq <- SSB / SST
cat("\neta-squared:", round(eta_sq, 4),
    "->", ifelse(eta_sq < 0.06, "small",
          ifelse(eta_sq < 0.14, "medium", "large")), "effect\n")
cat("Decision:", ifelse(p_value < 0.05,
    "Reject H0 - at least one mean differs.", "Fail to reject H0."), "\n")

# 5. Post-hoc: Tukey HSD
cat("\n=== Tukey HSD Post-hoc ===\n")
tukey <- TukeyHSD(anova_model, conf.level = 0.95)
print(tukey)

library(emmeans)
emm     <- emmeans(anova_model, "Method")
cld_res <- multcomp::cld(emm, alpha = 0.05, Letters = letters,
                         reversed = TRUE)
cat("\n=== Compact Letter Display ===\n"); print(cld_res)

# 6. Visualization
library(ggplot2)
cld_df <- as.data.frame(cld_res)

p1 <- ggplot(education, aes(x = Method, y = Score, fill = Method)) +
  geom_boxplot(alpha = 0.65, width = 0.45, outlier.shape = NA) +
  geom_jitter(width = 0.12, alpha = 0.55, size = 2, colour = "grey30") +
  stat_summary(fun = mean, geom = "point", shape = 23,
               size = 4, fill = "white") +
  geom_text(data = cld_df,
            aes(x = Method, y = upper.CL + 2,
                label = trimws(.group)),
            size = 5, fontface = "bold", inherit.aes = FALSE) +
  labs(
    title    = "Exam Scores by Teaching Method",
    subtitle = paste0("One-Way ANOVA: F(2,",
                      nrow(education) - 3, ") = ",
                      round(f_stat, 2), ", p = ",
                      round(p_value, 3),
                      ", eta^2 = ", round(eta_sq, 3)),
    y = "Exam Score", x = "Teaching Method",
    caption = "Letters indicate Tukey HSD groupings (alpha = 0.05)"
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "none")

print(p1)

p2 <- ggplot(data.frame(res = residuals(anova_model)),
             aes(sample = res)) +
  stat_qq() + stat_qq_line(color = "red", linewidth = 1) +
  labs(title = "Q-Q Plot of Residuals",
       x = "Theoretical Quantiles", y = "Sample Quantiles") +
  theme_minimal(base_size = 13)
print(p2)
