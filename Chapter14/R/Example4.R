# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 4: Σύγκριση Δύο Διασπορών (F-test και Levene)

set.seed(789)
n1 <- 25; n2 <- 30; target <- 50
machine1 <- rnorm(n1, mean = target, sd = 2.5)
machine2 <- rnorm(n2, mean = target, sd = 1.5)

# F-test for equality of variances
f_test <- var.test(machine1, machine2, alternative = "two.sided")
print(f_test)

# Manual F-test
s1_sq <- var(machine1);  s2_sq <- var(machine2)
f_stat <- s1_sq / s2_sq
df1 <- n1 - 1;  df2 <- n2 - 1
p_val <- 2 * min(pf(f_stat, df1, df2),
                 pf(f_stat, df1, df2, lower.tail = FALSE))

cat("\n--- Manual F-test ---\n")
cat("s1^2:", round(s1_sq, 4), " s2^2:", round(s2_sq, 4), "\n")
cat("F = s1^2/s2^2:", round(f_stat, 4), "\n")
cat("df1 =", df1, ", df2 =", df2, "\n")
cat("p-value (two-sided):", round(p_val, 4), "\n")

# Critical values
f_lo <- qf(0.025, df1, df2);  f_hi <- qf(0.975, df1, df2)
cat("Critical values: [", round(f_lo, 3), ",", round(f_hi, 3), "]\n")

# Levene's test (more robust)
library(car)
combined <- data.frame(
  Length  = c(machine1, machine2),
  Machine = factor(rep(c("M1", "M2"), c(n1, n2)))
)
lev <- leveneTest(Length ~ Machine, data = combined)
cat("\nLevene's test:\n"); print(lev)

# Visualization
library(ggplot2)
ggplot(combined, aes(x = Machine, y = Length, fill = Machine)) +
  geom_boxplot(alpha = 0.7, width = 0.4) +
  geom_jitter(width = 0.1, alpha = 0.4, size = 1.5) +
  labs(
    title    = "Comparison of Machine Variability",
    subtitle = paste("F-test p-value =", round(p_val, 4)),
    y = "Length (mm)", x = "Machine"
  ) +
  theme_minimal(base_size = 13) + theme(legend.position = "none")
