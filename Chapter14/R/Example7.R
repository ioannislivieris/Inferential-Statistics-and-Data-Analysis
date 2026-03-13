# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 7: Έλεγχος Ομοσκεδαστικότητας (Levene, Bartlett)

advertising <- data.frame(
  Sales    = c(23, 25, 27, 24, 26,
               30, 32, 28, 31, 29,
               20, 22, 19, 21, 20),
  Strategy = factor(rep(c("Television", "Internet", "Print"), each = 5))
)
anova_model <- aov(Sales ~ Strategy, data = advertising)

library(car)

# Levene's test
lev <- leveneTest(Sales ~ Strategy, data = advertising)
cat("Levene's test: F =", round(lev$`F value`[1], 4),
    ", p =", round(lev$`Pr(>F)`[1], 4), "\n")

# Bartlett's test
bart <- bartlett.test(Sales ~ Strategy, data = advertising)
cat("Bartlett's test: K^2 =", round(bart$statistic, 4),
    ", p =", round(bart$p.value, 4), "\n")

# Variance ratio check
vars  <- tapply(advertising$Sales, advertising$Strategy, var)
ratio <- max(vars) / min(vars)
cat("Max/Min variance ratio:", round(ratio, 2),
    "(< 3 is acceptable)\n")

# Residuals vs. Fitted plot
plot(anova_model, which = 1,
     main = "Residuals vs Fitted (ANOVA)")
