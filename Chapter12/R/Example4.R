# Chapter 12 - Διαστήματα Εμπιστοσύνης
# Example 4: Διάστημα για Διαφορά Δύο Μέσων (άνισες διασπορές, Welch)
#   2 εργοστάσια, n1=25, n2=30: F-test + Welch-Satterthwaite df

# Sample data
factory1 <- c(50.2, 48.7, 51.3, 49.8, 52.1, 50.5, 48.9, 51.7,
              49.2, 52.4, 50.8, 49.5, 51.0, 48.6, 52.2,
              50.1, 49.7, 51.4, 50.3, 48.8, 51.9, 49.4,
              52.0, 50.6, 49.1)

factory2 <- c(51.1, 52.5, 50.8, 52.9, 51.4, 52.2, 50.6, 53.1,
              51.7, 52.8, 51.2, 52.6, 50.9, 53.0, 51.5,
              52.3, 51.0, 52.7, 51.8, 52.4, 51.3, 52.1,
              50.7, 52.9, 51.6, 52.5, 51.1, 52.8, 51.4, 52.2)

n1    <- length(factory1)
n2    <- length(factory2)
xbar1 <- mean(factory1)
xbar2 <- mean(factory2)
s1    <- sd(factory1)
s2    <- sd(factory2)
conf_level <- 0.95

# F-test for equal variances
f_stat  <- s1^2 / s2^2
f_pval  <- 2 * min(pf(f_stat, n1 - 1, n2 - 1),
                   1 - pf(f_stat, n1 - 1, n2 - 1))

cat("F-test for equal variances:\n")
cat(sprintf("  F-statistic: %.3f\n", f_stat))
cat(sprintf("  p-value:     %.4f\n", f_pval))
cat(sprintf("  Variances equal? %s\n\n",
            ifelse(f_pval > 0.05, "Yes (use pooled)", "No (use Welch)")))

# Welch's method
cat("Welch's t-interval (unequal variances):\n")
cat(sprintf("  Factory 1: n=%d, mean=%.2f, sd=%.2f\n", n1, xbar1, s1))
cat(sprintf("  Factory 2: n=%d, mean=%.2f, sd=%.2f\n", n2, xbar2, s2))

# Standard error (no pooling)
se <- sqrt(s1^2 / n1 + s2^2 / n2)

# Welch-Satterthwaite degrees of freedom
df_welch <- (s1^2 / n1 + s2^2 / n2)^2 /
  ((s1^2 / n1)^2 / (n1 - 1) + (s2^2 / n2)^2 / (n2 - 1))

alpha        <- 1 - conf_level
t_crit       <- qt(1 - alpha / 2, df_welch)
diff         <- xbar1 - xbar2
margin_error <- t_crit * se
ci_lower     <- diff - margin_error
ci_upper     <- diff + margin_error

cat(sprintf("  Welch df:       %.2f\n", df_welch))
cat(sprintf("  Difference:     %.3f\n", diff))
cat(sprintf("  Standard error: %.3f\n", se))
cat(sprintf("  %.0f%% CI: [%.3f, %.3f]\n",
            conf_level * 100, ci_lower, ci_upper))

# Verify using t.test (var.equal = FALSE)
result <- t.test(factory1, factory2, var.equal = FALSE,
                 conf.level = conf_level)
cat(sprintf("\nUsing t.test (Welch's method):\n"))
cat(sprintf("  %.0f%% CI: [%.3f, %.3f]\n",
            conf_level * 100, result$conf.int[1], result$conf.int[2]))
