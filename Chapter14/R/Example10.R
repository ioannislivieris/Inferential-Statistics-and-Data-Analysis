# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 10: Πλήρης Ανάλυση Δύο Ανεξάρτητων Δειγμάτων
#   (Z-test, Welch, Pooled, Cohen's d, Power)

set.seed(2024)

# Known parameters
n1 <- 35;  n2 <- 30
sigma1 <- 8;  sigma2 <- 10
mu0_diff <- 0   # H0: mu1 - mu2 = 0

# Generate samples
sample1 <- rnorm(n1, mean = 12.5, sd = sigma1)
sample2 <- rnorm(n2, mean = 9.0,  sd = sigma2)
x_bar1 <- mean(sample1);  x_bar2 <- mean(sample2)
s1     <- sd(sample1);    s2     <- sd(sample2)

cat("=== Descriptive Statistics ===\n")
cat(sprintf("Group A: n=%d, mean=%.3f, sd=%.3f\n", n1, x_bar1, s1))
cat(sprintf("Group B: n=%d, mean=%.3f, sd=%.3f\n", n2, x_bar2, s2))
cat(sprintf("Observed difference (A - B): %.3f\n", x_bar1 - x_bar2))

# 1. Z-test (known sigmas)
cat("\n=== Z-test (known sigma) ===\n")
se_z    <- sqrt(sigma1^2/n1 + sigma2^2/n2)
z_stat  <- (x_bar1 - x_bar2 - mu0_diff) / se_z
p_z     <- 2 * pnorm(-abs(z_stat))
z_crit  <- qnorm(0.975)
ci_z_lo <- (x_bar1 - x_bar2) - z_crit * se_z
ci_z_hi <- (x_bar1 - x_bar2) + z_crit * se_z

cat(sprintf("SE              : %.4f\n", se_z))
cat(sprintf("z-statistic     : %.4f\n", z_stat))
cat(sprintf("p-value         : %.4f\n", p_z))
cat(sprintf("95%% CI (mu1-mu2): [%.3f, %.3f]\n", ci_z_lo, ci_z_hi))
cat("Decision:", ifelse(p_z < 0.05, "Reject H0", "Fail to reject H0"), "\n")

# 2. Equality of variances: F-test + Levene
cat("\n=== Equality of Variances ===\n")
f_test <- var.test(sample1, sample2)
cat(sprintf("F-test: F = %.4f, p = %.4f\n",
            f_test$statistic, f_test$p.value))
cat("Variances are", ifelse(f_test$p.value > 0.05, "equal", "unequal"),
    "(alpha = 0.05)\n")

library(car)
combined <- data.frame(
  Value = c(sample1, sample2),
  Group = factor(rep(c("A","B"), c(n1, n2)))
)
lev <- leveneTest(Value ~ Group, data = combined)
cat(sprintf("Levene: F = %.4f, p = %.4f\n",
            lev$`F value`[1], lev$`Pr(>F)`[1]))

# 3. Welch t-test (default - unequal variances)
cat("\n=== Welch t-test (unequal variances) ===\n")
t_welch <- t.test(sample1, sample2, var.equal = FALSE,
                  alternative = "two.sided", conf.level = 0.95)
print(t_welch)

# Manual Welch
se_w      <- sqrt(s1^2/n1 + s2^2/n2)
t_w_stat  <- (x_bar1 - x_bar2 - mu0_diff) / se_w
num_df    <- (s1^2/n1 + s2^2/n2)^2
den_df    <- (s1^2/n1)^2/(n1-1) + (s2^2/n2)^2/(n2-1)
df_welch  <- num_df / den_df
p_welch   <- 2 * pt(-abs(t_w_stat), df = df_welch)
t_crit_w  <- qt(0.975, df = df_welch)
ci_w_lo   <- (x_bar1 - x_bar2) - t_crit_w * se_w
ci_w_hi   <- (x_bar1 - x_bar2) + t_crit_w * se_w

cat(sprintf("\nManual Welch: t = %.4f, df = %.2f, p = %.4f\n",
            t_w_stat, df_welch, p_welch))
cat(sprintf("95%% CI: [%.3f, %.3f]\n", ci_w_lo, ci_w_hi))

# 4. Pooled t-test (equal variances - for reference)
cat("\n=== Pooled t-test (equal variances) ===\n")
t_pool <- t.test(sample1, sample2, var.equal = TRUE,
                 alternative = "two.sided", conf.level = 0.95)
print(t_pool)

sp2      <- ((n1-1)*s1^2 + (n2-1)*s2^2) / (n1 + n2 - 2)
sp       <- sqrt(sp2)
se_pool  <- sp * sqrt(1/n1 + 1/n2)
t_p_stat <- (x_bar1 - x_bar2 - mu0_diff) / se_pool
cat(sprintf("Pooled SD (sp): %.4f\n", sp))

# 5. Effect size and power
cohens_d <- (x_bar1 - x_bar2) / sp
d_label  <- ifelse(abs(cohens_d) < 0.2, "small",
            ifelse(abs(cohens_d) < 0.5, "medium",
            ifelse(abs(cohens_d) < 0.8, "medium-large", "large")))
cat(sprintf("\nCohen's d : %.4f (%s effect)\n", cohens_d, d_label))

library(pwr)
pwr_res <- pwr.t2n.test(n1 = n1, n2 = n2,
                        d = cohens_d, sig.level = 0.05,
                        alternative = "two.sided")
cat(sprintf("Power (1-beta): %.4f\n", pwr_res$power))

# Power curve
d_seq  <- seq(0.1, 1.5, by = 0.05)
pwr_seq <- sapply(d_seq, function(d)
  pwr.t2n.test(n1=n1, n2=n2, d=d, sig.level=0.05)$power)

# 6. Visualization
library(ggplot2)
library(gridExtra)

p1 <- ggplot(combined, aes(x = Group, y = Value, fill = Group)) +
  geom_boxplot(alpha = 0.65, width = 0.4, outlier.shape = NA) +
  geom_jitter(width = 0.1, alpha = 0.45, size = 1.8) +
  stat_summary(fun = mean, geom = "point", shape = 23,
               size = 4, fill = "white") +
  labs(
    title    = "Blood Pressure Reduction by Treatment",
    subtitle = sprintf("Welch t = %.3f, p = %.3f, Cohen's d = %.3f",
                       t_w_stat, p_welch, cohens_d),
    y = "BP Reduction (mmHg)", x = "Treatment"
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "none")

p2 <- ggplot(data.frame(d = d_seq, power = pwr_seq),
             aes(x = d, y = power)) +
  geom_line(colour = "steelblue", linewidth = 1.2) +
  geom_hline(yintercept = 0.80, linetype = "dashed",
             colour = "red", linewidth = 0.9) +
  geom_vline(xintercept = abs(cohens_d), linetype = "dotted",
             colour = "orange", linewidth = 0.9) +
  annotate("text", x = abs(cohens_d) + 0.08, y = 0.15,
           label = sprintf("d = %.2f", abs(cohens_d)),
           colour = "orange", size = 4) +
  labs(
    title    = "Power Curve (n1=35, n2=30)",
    subtitle = "Red dashed line: 80% power threshold",
    x = "Cohen's d", y = "Power (1 - beta)"
  ) +
  theme_minimal(base_size = 13)

grid.arrange(p1, p2, ncol = 2)
