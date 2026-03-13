# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 3: Κατανομή t Student  T ~ t(10)

# Degrees of freedom
df <- 10

# i. P(T <= 1.5)
prob1 <- pt(1.5, df = df)
cat(sprintf("P(T <= 1.5) = %.4f\n", prob1))

# ii. P(-2 < T < 2)
prob2 <- pt(2, df = df) - pt(-2, df = df)
cat(sprintf("P(-2 < T < 2) = %.4f\n", prob2))

# iii. Critical value t_{0.025, 10}
t_critical <- qt(0.975, df = df)
cat(sprintf("t_{0.025, 10} = %.4f\n", t_critical))

# Compare with standard normal
z_critical <- qnorm(0.975)
cat(sprintf("z_{0.025} = %.4f (for comparison)\n", z_critical))

# Visualization: Compare t(10) with standard normal
x    <- seq(-4, 4, length.out = 1000)
y_t  <- dt(x, df = df)
y_norm <- dnorm(x)

plot(x, y_t, type = 'l', lwd = 2, col = 'blue',
     main = 't-Distribution vs Standard Normal',
     xlab = 't', ylab = 'Density',
     ylim = c(0, max(y_t) * 1.1))

lines(x, y_norm, lwd = 2, col = 'red', lty = 2)

# Mark critical values
abline(v = c(-t_critical, t_critical), col = 'blue', lty = 3)
abline(v = c(-z_critical, z_critical), col = 'red',  lty = 3)

# Shade 95% area for t
x_shade <- x[x >= -t_critical & x <= t_critical]
y_shade  <- dt(x_shade, df = df)
polygon(c(-t_critical, x_shade, t_critical), c(0, y_shade, 0),
        col = rgb(0, 0, 1, 0.2), border = NA)

legend('topright',
       legend = c('t(10)', 'N(0,1)',
                  sprintf('t critical = %.2f', t_critical),
                  sprintf('z critical = %.2f', z_critical)),
       col = c('blue', 'red', 'blue', 'red'),
       lty = c(1, 2, 3, 3),
       lwd = c(2, 2, 1, 1))

grid()
