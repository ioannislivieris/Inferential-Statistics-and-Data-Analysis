# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 8: Welch's ANOVA και Kruskal-Wallis (Εναλλακτικές Μέθοδοι)

advertising <- data.frame(
  Sales    = c(23, 25, 27, 24, 26,
               30, 32, 28, 31, 29,
               20, 22, 19, 21, 20),
  Strategy = factor(rep(c("Television", "Internet", "Print"), each = 5))
)

# Welch's ANOVA (robust to unequal variances)
welch_anova <- oneway.test(Sales ~ Strategy, data = advertising,
                           var.equal = FALSE)
cat("Welch's ANOVA: F =", round(welch_anova$statistic, 3),
    ", df =", round(welch_anova$parameter, 2),
    ", p =", round(welch_anova$p.value, 4), "\n")

# Kruskal-Wallis test (non-parametric alternative)
kw <- kruskal.test(Sales ~ Strategy, data = advertising)
cat("\nKruskal-Wallis: chi^2 =", round(kw$statistic, 3),
    ", df =", kw$parameter,
    ", p =", round(kw$p.value, 4), "\n")
