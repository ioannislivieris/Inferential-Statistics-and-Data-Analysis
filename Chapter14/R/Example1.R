# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 1: Σύγκριση Δύο Μέσων με Ανεξάρτητα Δείγματα (Welch t-test)

set.seed(123)

# Sample statistics
n1 <- 30; n2 <- 25
x_bar1 <- 82; x_bar2 <- 78
s1 <- 10; s2 <- 12

# Generate data consistent with the given statistics
sample1 <- rnorm(n1, mean = x_bar1, sd = s1)
sample2 <- rnorm(n2, mean = x_bar2, sd = s2)
# Standardize to match exactly the given mean and sd
sample1 <- sample1 * (s1 / sd(sample1)) + (x_bar1 - mean(sample1))
sample2 <- sample2 * (s2 / sd(sample2)) + (x_bar2 - mean(sample2))

# Step 1: F-test for equality of variances
cat("=== F-test for Equality of Variances ===\n")
f_test <- var.test(sample1, sample2)
print(f_test)
cat("Variance ratio:", round(var(sample1)/var(sample2), 3), "\n\n")

# Step 2: Welch's t-test (default - unequal variances)
cat("=== Welch's t-test (Unequal Variances) ===\n")
t_welch <- t.test(sample1, sample2, var.equal = FALSE,
                  alternative = "two.sided", conf.level = 0.95)
print(t_welch)

# Step 3: Pooled t-test (equal variances - for comparison)
cat("=== Pooled t-test (Equal Variances) ===\n")
t_pooled <- t.test(sample1, sample2, var.equal = TRUE,
                   alternative = "two.sided", conf.level = 0.95)
print(t_pooled)

# Manual calculation of Welch t-test
se_welch <- sqrt(s1^2/n1 + s2^2/n2)
t_stat   <- (x_bar1 - x_bar2) / se_welch
num_df   <- (s1^2/n1 + s2^2/n2)^2
den_df   <- (s1^2/n1)^2/(n1-1) + (s2^2/n2)^2/(n2-1)
df_welch <- num_df / den_df
p_value  <- 2 * pt(-abs(t_stat), df = df_welch)

cat("\n--- Manual Welch Calculation ---\n")
cat("SE:", round(se_welch, 4), "\n")
cat("t-statistic:", round(t_stat, 4), "\n")
cat("df (Welch-Satterthwaite):", round(df_welch, 2), "\n")
cat("p-value:", round(p_value, 4), "\n")

# 95% Confidence interval
t_crit  <- qt(0.975, df = df_welch)
ci_lo   <- (x_bar1 - x_bar2) - t_crit * se_welch
ci_hi   <- (x_bar1 - x_bar2) + t_crit * se_welch
cat("95% CI for (mu1 - mu2): [", round(ci_lo, 2), ",", round(ci_hi, 2), "]\n")

# Effect size: Cohen's d
cohens_d <- (x_bar1 - x_bar2) /
  sqrt(((n1-1)*s1^2 + (n2-1)*s2^2) / (n1+n2-2))
cat("Cohen's d:", round(cohens_d, 3), "\n")

# Visualization
library(ggplot2)
data <- data.frame(
  Score  = c(sample1, sample2),
  Method = factor(rep(c("Method A", "Method B"), c(n1, n2)))
)
ggplot(data, aes(x = Method, y = Score, fill = Method)) +
  geom_boxplot(alpha = 0.7, width = 0.5) +
  geom_jitter(width = 0.1, alpha = 0.4, size = 1.5) +
  stat_summary(fun = mean, geom = "point", shape = 23,
               size = 4, fill = "white") +
  labs(
    title    = "Comparison of Two Teaching Methods",
    subtitle = paste("Welch t-test: t =", round(t_stat, 3),
                     ", p-value =", round(p_value, 3)),
    y = "Exam Score", x = "Teaching Method"
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "none")
