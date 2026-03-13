# Chapter 14 - Παραμετρικοί Έλεγχοι για Δύο Πληθυσμούς και ANOVA
# Example 12: Ζευγαρωτός Έλεγχος και Σύγκριση Αναλογιών (Κλινική Μελέτη)

set.seed(101)
n_pair <- 20

# --- Paired t-test ---
before <- round(rnorm(n_pair, mean = 148, sd = 14), 1)
change <- round(rnorm(n_pair, mean = 12.5, sd = 5),  1)
after  <- before - change
d      <- before - after

cat("=== Paired t-test ===\n")
cat(sprintf("Mean before : %.2f mmHg\n", mean(before)))
cat(sprintf("Mean after  : %.2f mmHg\n", mean(after)))
cat(sprintf("Mean diff   : %.3f mmHg\n", mean(d)))
cat(sprintf("SD of diff  : %.3f\n", sd(d)))

sw <- shapiro.test(d)
cat(sprintf("\nShapiro-Wilk (differences): W = %.4f, p = %.4f\n",
            sw$statistic, sw$p.value))
cat("Normality:", ifelse(sw$p.value > 0.05, "Supported", "Violated"), "\n")

t_pair <- t.test(before, after, paired = TRUE, alternative = "greater")
print(t_pair)

# Manual calculation
d_bar   <- mean(d);  s_d <- sd(d);  se_d <- s_d / sqrt(n_pair)
t_man   <- d_bar / se_d
p_man   <- pt(t_man, df = n_pair - 1, lower.tail = FALSE)
t_crit  <- qt(0.975, df = n_pair - 1)
ci_lo   <- d_bar - t_crit * se_d
ci_hi   <- d_bar + t_crit * se_d
cohens_d_pair <- d_bar / s_d

cat(sprintf("\nManual: t = %.4f, df = %d, p (one-sided) = %.4f\n",
            t_man, n_pair - 1, p_man))
cat(sprintf("95%% CI for mu_d: [%.3f, %.3f] mmHg\n", ci_lo, ci_hi))
cat(sprintf("Cohen's d (paired): %.4f\n", cohens_d_pair))
cat("Decision:", ifelse(p_man < 0.05, "Reject H0", "Fail to reject H0"), "\n")

# --- Two-proportion z-test ---
cat("\n=== Two-Proportion Z-test ===\n")
n1_p <- 35;  x1_p <- 22
n2_p <- 30;  x2_p <- 15
p1_hat <- x1_p / n1_p;  p2_hat <- x2_p / n2_p

cat(sprintf("n1*p1 = %.1f,  n1*(1-p1) = %.1f\n",
            n1_p*p1_hat, n1_p*(1-p1_hat)))
cat(sprintf("n2*p2 = %.1f,  n2*(1-p2) = %.1f\n",
            n2_p*p2_hat, n2_p*(1-p2_hat)))

prop_res <- prop.test(c(x1_p, x2_p), c(n1_p, n2_p),
                      alternative = "two.sided", correct = FALSE)
print(prop_res)

# Manual
p_bar    <- (x1_p + x2_p) / (n1_p + n2_p)
se_prop  <- sqrt(p_bar * (1-p_bar) * (1/n1_p + 1/n2_p))
z_prop   <- (p1_hat - p2_hat) / se_prop
p_prop   <- 2 * pnorm(-abs(z_prop))
se_ci    <- sqrt(p1_hat*(1-p1_hat)/n1_p + p2_hat*(1-p2_hat)/n2_p)
ci_prop  <- c((p1_hat - p2_hat) - 1.96*se_ci,
              (p1_hat - p2_hat) + 1.96*se_ci)
h_cohen  <- 2*asin(sqrt(p1_hat)) - 2*asin(sqrt(p2_hat))
h_lbl    <- ifelse(abs(h_cohen) < 0.2, "small",
            ifelse(abs(h_cohen) < 0.5, "medium", "large"))

cat(sprintf("\nPooled p-bar: %.4f\n", p_bar))
cat(sprintf("z-statistic : %.4f,  p-value: %.4f\n", z_prop, p_prop))
cat(sprintf("95%% CI (p1-p2): [%.4f, %.4f]\n", ci_prop[1], ci_prop[2]))
cat(sprintf("Cohen's h   : %.4f (%s effect)\n", h_cohen, h_lbl))
cat("Decision:", ifelse(p_prop < 0.05, "Reject H0", "Fail to reject H0"), "\n")

# --- Visualization ---
library(ggplot2); library(gridExtra)

pair_df <- data.frame(
  Subject = rep(1:n_pair, 2),
  Value   = c(before, after),
  Time    = factor(rep(c("Before","After"), each = n_pair),
                   levels = c("Before","After"))
)
p1 <- ggplot(pair_df, aes(x = Time, y = Value, group = Subject)) +
  geom_line(colour = "steelblue", alpha = 0.45) +
  geom_point(aes(colour = Time), size = 2.5) +
  stat_summary(aes(group = 1), fun = mean, geom = "line",
               colour = "darkred", linewidth = 1.5) +
  stat_summary(aes(group = 1), fun = mean, geom = "point",
               colour = "darkred", size = 4, shape = 18) +
  labs(
    title    = "Blood Pressure: Before vs After",
    subtitle = sprintf("Paired t = %.3f, p = %.4f, d = %.3f",
                       t_man, p_man, cohens_d_pair),
    y = "Systolic BP (mmHg)", x = ""
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "none")

prop_df <- data.frame(
  Group       = c("Treatment A", "Treatment B"),
  Improved    = c(p1_hat, p2_hat),
  NotImproved = c(1-p1_hat, 1-p2_hat)
)
p2_plot <- ggplot(prop_df, aes(x = Group, y = Improved, fill = Group)) +
  geom_col(width = 0.45, alpha = 0.75) +
  geom_errorbar(
    aes(ymin = Improved - 1.96*sqrt(Improved*(1-Improved)/c(n1_p, n2_p)),
        ymax = Improved + 1.96*sqrt(Improved*(1-Improved)/c(n1_p, n2_p))),
    width = 0.12, linewidth = 0.8) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  labs(
    title    = "Proportion Improved by Treatment",
    subtitle = sprintf("z = %.3f, p = %.3f, Cohen's h = %.3f",
                       z_prop, p_prop, h_cohen),
    y = "Proportion Improved", x = ""
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "none")

grid.arrange(p1, p2_plot, ncol = 2)
