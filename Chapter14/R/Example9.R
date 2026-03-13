# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 9: Post-hoc Αναλύσεις (Tukey HSD, Bonferroni, Scheffé)

advertising <- data.frame(
  Sales    = c(23, 25, 27, 24, 26,
               30, 32, 28, 31, 29,
               20, 22, 19, 21, 20),
  Strategy = factor(rep(c("Television", "Internet", "Print"), each = 5))
)
anova_model <- aov(Sales ~ Strategy, data = advertising)

# 1. Tukey HSD
cat("=== Tukey HSD ===\n")
tukey <- TukeyHSD(anova_model, conf.level = 0.95)
print(tukey)

# Plot Tukey CI
par(mar = c(5, 12, 4, 2))
plot(tukey, las = 1, main = "Tukey HSD 95% Confidence Intervals")

# 2. Bonferroni via pairwise.t.test
cat("\n=== Bonferroni Correction ===\n")
bonf <- pairwise.t.test(advertising$Sales, advertising$Strategy,
                        p.adjust.method = "bonferroni")
print(bonf)

# 3. Scheffe Test
library(agricolae)
scheffe <- scheffe.test(anova_model, "Strategy", alpha = 0.05)
cat("\n=== Scheffe Groups ===\n")
print(scheffe$groups)

# 4. Compact letter display (CLD)
library(multcompView)
library(emmeans)
emm     <- emmeans(anova_model, "Strategy")
cld_res <- multcomp::cld(emm, alpha = 0.05, Letters = letters)
cat("\n=== Compact Letter Display ===\n")
print(cld_res)

# Visualization: bar plot with significance letters
cld_df <- as.data.frame(cld_res)
library(ggplot2)
ggplot(cld_df, aes(x = Strategy, y = emmean, fill = Strategy)) +
  geom_bar(stat = "identity", alpha = 0.7) +
  geom_errorbar(aes(ymin = lower.CL, ymax = upper.CL),
                width = 0.2, linewidth = 0.8) +
  geom_text(aes(label = trimws(.group), y = upper.CL + 0.5),
            size = 5, fontface = "bold") +
  labs(
    title = "Mean Sales with Tukey HSD Groupings",
    y = "Mean Sales (thousands EUR)", x = "Strategy"
  ) +
  theme_minimal(base_size = 13) + theme(legend.position = "none")
