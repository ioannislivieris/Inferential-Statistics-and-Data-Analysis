# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 5: Οπτικοποίηση σφαλμάτων τύπου I και II και ισχύος

library(ggplot2)
library(gridExtra)
library(pwr)

# Parameters
mu0 <- 100
sigma <- 15
n <- 36
alpha <- 0.05
se <- sigma / sqrt(n)

# ============ TYPE I AND TYPE II ERRORS ============
# Critical values
z_crit <- qnorm(1 - alpha/2)
x_crit_lower <- mu0 - z_crit * se
x_crit_upper <- mu0 + z_crit * se

# Plot 1: Type I error (H0 true)
x_vals <- seq(mu0 - 4*se, mu0 + 4*se, length.out = 500)
y_h0 <- dnorm(x_vals, mu0, se)

df1 <- data.frame(x = x_vals, y = y_h0)
p1 <- ggplot(df1, aes(x, y)) +
  geom_line(size = 1) +
  geom_area(data = subset(df1, x <= x_crit_lower),
            fill = "red", alpha = 0.3) +
  geom_area(data = subset(df1, x >= x_crit_upper),
            fill = "red", alpha = 0.3) +
  geom_vline(xintercept = c(x_crit_lower, x_crit_upper),
             linetype = "dashed", color = "red", size = 1) +
  labs(title = "Type I Error (alpha)",
       subtitle = sprintf("P(Reject H0 | H0 true) = %.3f", alpha),
       x = "Sample Mean", y = "Density") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 12))

# Plot 2: Type II error and Power (H1 true)
mu1 <- 108  # Alternative mean
y_h1 <- dnorm(x_vals, mu1, se)

df2 <- data.frame(x = x_vals, y_h1 = y_h1, y_h0 = y_h0)
beta_val <- pnorm(x_crit_upper, mu1, se) - pnorm(x_crit_lower, mu1, se)
power_val <- 1 - beta_val

p2 <- ggplot(df2) +
  geom_line(aes(x, y_h0), linetype = "dashed", color = "gray", size = 0.8) +
  geom_line(aes(x, y_h1), size = 1, color = "blue") +
  geom_area(data = subset(df2, x >= x_crit_lower & x <= x_crit_upper),
            aes(x, y_h1), fill = "orange", alpha = 0.3) +
  geom_area(data = subset(df2, x < x_crit_lower | x > x_crit_upper),
            aes(x, y_h1), fill = "green", alpha = 0.3) +
  geom_vline(xintercept = c(x_crit_lower, x_crit_upper),
             linetype = "dashed", color = "red", size = 1) +
  labs(title = "Type II Error (beta) and Power (1-beta)",
       subtitle = sprintf("beta = %.3f, Power = %.3f", beta_val, power_val),
       x = "Sample Mean", y = "Density") +
  annotate("text", x = mu0, y = max(y_h1) * 0.5,
           label = "Type II Error", color = "orange", size = 4) +
  annotate("text", x = mu1 + se, y = max(y_h1) * 0.8,
           label = "Power", color = "darkgreen", size = 4) +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 12))

# ============ POWER CURVES ============
# Effect of sample size
n_vals <- seq(10, 100, by = 5)
effect_size <- 0.5
powers_n <- sapply(n_vals, function(n) {
  pwr.t.test(n = n, d = effect_size, sig.level = alpha,
             type = "one.sample", alternative = "two.sided")$power
})

df3 <- data.frame(n = n_vals, power = powers_n)
p3 <- ggplot(df3, aes(n, power)) +
  geom_line(size = 1, color = "blue") +
  geom_hline(yintercept = 0.80, linetype = "dashed", color = "red") +
  labs(title = "Power vs Sample Size",
       subtitle = sprintf("Effect size d = %.1f, alpha = %.2f",
                          effect_size, alpha),
       x = "Sample Size (n)", y = "Power (1-beta)") +
  scale_y_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 12))

# Effect of effect size
d_vals <- seq(0.1, 1.2, by = 0.05)
powers_d <- sapply(d_vals, function(d) {
  pwr.t.test(n = 36, d = d, sig.level = alpha,
             type = "one.sample", alternative = "two.sided")$power
})

df4 <- data.frame(d = d_vals, power = powers_d)
p4 <- ggplot(df4, aes(d, power)) +
  geom_line(size = 1, color = "darkgreen") +
  geom_hline(yintercept = 0.80, linetype = "dashed", color = "red") +
  geom_vline(xintercept = c(0.2, 0.5, 0.8), linetype = "dotted") +
  labs(title = "Power vs Effect Size",
       subtitle = sprintf("n = %d, alpha = %.2f", n, alpha),
       x = "Effect Size (Cohen's d)", y = "Power (1-beta)") +
  scale_y_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2)) +
  annotate("text", x = c(0.2, 0.5, 0.8), y = 0.05,
           label = c("Small", "Medium", "Large"), size = 3) +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 12))

# ============ ONE-TAILED VS TWO-TAILED ============
z_obs <- 1.8
p_two <- 2 * pnorm(-abs(z_obs))
p_one <- pnorm(-abs(z_obs))

x_z <- seq(-4, 4, length.out = 500)
y_z <- dnorm(x_z)

df5 <- data.frame(x = x_z, y = y_z)
p5 <- ggplot(df5, aes(x, y)) +
  geom_line(size = 1) +
  geom_area(data = subset(df5, x <= -abs(z_obs)),
            fill = "blue", alpha = 0.3) +
  geom_area(data = subset(df5, x >= abs(z_obs)),
            fill = "blue", alpha = 0.3) +
  geom_vline(xintercept = c(-z_obs, z_obs),
             linetype = "dashed", color = "blue", size = 1) +
  labs(title = "Two-tailed Test",
       subtitle = sprintf("z = %.2f, p-value = %.4f", z_obs, p_two),
       x = "z", y = "Density") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 12))

p6 <- ggplot(df5, aes(x, y)) +
  geom_line(size = 1) +
  geom_area(data = subset(df5, x >= z_obs),
            fill = "red", alpha = 0.3) +
  geom_vline(xintercept = z_obs,
             linetype = "dashed", color = "red", size = 1) +
  labs(title = "One-tailed Test (Right)",
       subtitle = sprintf("z = %.2f, p-value = %.4f", z_obs, p_one),
       x = "z", y = "Density") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 12))

# Arrange plots
grid.arrange(p1, p2, p3, p4, p5, p6, ncol = 2)

# Print summary
cat("\n=== SUMMARY ===\n")
cat(sprintf("Type I Error (alpha): %.3f\n", alpha))
cat(sprintf("Type II Error (beta): %.3f\n", beta_val))
cat(sprintf("Power (1-beta): %.3f\n", power_val))
cat(sprintf("\nFor z = %.2f:\n", z_obs))
cat(sprintf("  Two-tailed p-value: %.4f\n", p_two))
cat(sprintf("  One-tailed p-value: %.4f\n", p_one))
cat(sprintf("  One-tailed has %.1f%% lower p-value\n",
            (1 - p_one/p_two) * 100))
