# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 7: Ανάλυση Κατανομής F — Σύγκριση Μεταβλητότητας Πωλήσεων
#   Κατάστημα Α: n1=20, s1=1200 EUR
#   Κατάστημα Β: n2=25, s2=800  EUR

# Data
n1 <- 20; s1 <- 1200
n2 <- 25; s2 <- 800

# Degrees of freedom
df1 <- n1 - 1   # 19
df2 <- n2 - 1   # 24

# F-statistic
F_stat <- (s1^2) / (s2^2)
cat(sprintf("F-statistic: %.4f\n", F_stat))
cat(sprintf("Degrees of freedom: df1 = %d, df2 = %d\n", df1, df2))

# Critical values (two-tailed, alpha = 0.05)
F_upper <- qf(0.975, df1, df2)
F_lower <- qf(0.025, df1, df2)
cat(sprintf("F_lower (0.025): %.4f\n", F_lower))
cat(sprintf("F_upper (0.975): %.4f\n", F_upper))
cat(sprintf("Observed F = %.4f lies %s the critical region\n",
            F_stat,
            ifelse(F_stat > F_upper || F_stat < F_lower,
                   "inside", "outside")))

# Visualization
x <- seq(0, 5, length.out = 1000)
y <- df(x, df1, df2)

plot(x, y, type = 'l', lwd = 2, col = 'blue',
     main = sprintf('F(%d, %d) Distribution', df1, df2),
     xlab = 'F', ylab = 'Density')

# Shade critical regions
x_upper <- x[x >= F_upper]
polygon(c(F_upper, x_upper, max(x)),
        c(0, df(x_upper, df1, df2), 0),
        col = rgb(1, 0, 0, 0.3), border = NA)

x_lower <- x[x <= F_lower]
polygon(c(0, x_lower, F_lower),
        c(0, df(x_lower, df1, df2), 0),
        col = rgb(1, 0, 0, 0.3), border = NA)

abline(v = F_stat,          col = 'darkgreen', lwd = 3, lty = 2)
abline(v = c(F_lower, F_upper), col = 'red',   lwd = 2, lty = 3)

legend('topright',
       legend = c('F distribution',
                  sprintf('Observed F = %.2f', F_stat),
                  sprintf('Critical values = %.2f, %.2f',
                          F_lower, F_upper),
                  'Critical regions (2.5% each)'),
       col  = c('blue', 'darkgreen', 'red', rgb(1,0,0,0.3)),
       lty  = c(1, 2, 3, NA),
       lwd  = c(2, 3, 2, NA),
       fill = c(NA, NA, NA, rgb(1,0,0,0.3)))
grid()
