# Chapter 13 - Έλεγχοι Υποθέσεων
# Example 4: Οπτικοποίηση p-value

# Parameters for visualization
mu0 <- 100
xbar <- 105
s <- 15
n <- 36
alpha <- 0.05

# Calculate test statistic
se <- s / sqrt(n)
t_stat <- (xbar - mu0) / se
df <- n - 1

# p-value
p_value <- 2 * pt(-abs(t_stat), df)

# Create visualization
t_vals <- seq(-4, 4, length.out = 1000)
density_vals <- dt(t_vals, df)

# Plot
par(mfrow = c(1, 1))
plot(t_vals, density_vals, type = 'l', lwd = 2,
     xlab = 't', ylab = 'Density',
     main = sprintf('t-distribution (df=%d) with Test Statistic', df))

# Shade rejection regions (two-tailed)
t_crit <- qt(1 - alpha/2, df)
t_left <- t_vals[t_vals <= -t_crit]
t_right <- t_vals[t_vals >= t_crit]

polygon(c(min(t_left), t_left, -t_crit, -t_crit),
        c(0, dt(t_left, df), dt(-t_crit, df), 0),
        col = rgb(1, 0, 0, 0.3), border = NA)
polygon(c(t_crit, t_crit, t_right, max(t_right)),
        c(0, dt(t_crit, df), dt(t_right, df), 0),
        col = rgb(1, 0, 0, 0.3), border = NA)

# Mark observed t-statistic
abline(v = t_stat, col = 'blue', lwd = 2, lty = 2)
abline(v = -t_stat, col = 'blue', lwd = 2, lty = 2)

# Mark critical values
abline(v = c(-t_crit, t_crit), col = 'red', lwd = 2, lty = 3)

# Add legend
legend('topright',
       legend = c('t-distribution',
                  sprintf('Observed t = %.2f', t_stat),
                  sprintf('Critical values = +/- %.2f', t_crit),
                  sprintf('Rejection region (alpha=%.2f)', alpha)),
       col = c('black', 'blue', 'red', rgb(1, 0, 0, 0.3)),
       lty = c(1, 2, 3, NA),
       lwd = c(2, 2, 2, NA),
       fill = c(NA, NA, NA, rgb(1, 0, 0, 0.3)),
       border = c(NA, NA, NA, 'black'))

# Add text
text(0, max(density_vals) * 0.9,
     sprintf('p-value = %.4f', p_value),
     col = 'blue', font = 2, cex = 1.2)

if (p_value < alpha) {
  text(0, max(density_vals) * 0.8,
       'Decision: Reject H0',
       col = 'red', font = 2, cex = 1.1)
} else {
  text(0, max(density_vals) * 0.8,
       'Decision: Fail to reject H0',
       col = 'darkgreen', font = 2, cex = 1.1)
}
