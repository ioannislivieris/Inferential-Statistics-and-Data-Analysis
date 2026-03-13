# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 4: Κατανομές χ² και F
#   χ²(10) και F(5, 10)

# Chi-square distribution
df_chi <- 10

# i. P(chi^2 > 15) for chi^2(10)
prob_chi <- 1 - pchisq(15, df = df_chi)
cat(sprintf("P(chi^2 > 15) for chi^2(10) = %.4f\n", prob_chi))

# Critical value
chi_critical <- qchisq(0.95, df = df_chi)
cat(sprintf("chi^2_{0.05, 10} = %.4f\n", chi_critical))

# F distribution
df1 <- 5
df2 <- 10

# ii. P(F > 2.5) for F(5, 10)
prob_f <- 1 - pf(2.5, df1 = df1, df2 = df2)
cat(sprintf("P(F > 2.5) for F(5,10) = %.4f\n", prob_f))

# Critical value
f_critical <- qf(0.95, df1 = df1, df2 = df2)
cat(sprintf("F_{0.05, 5, 10} = %.4f\n", f_critical))

# Visualization
par(mfrow = c(1, 2))

# Chi-square plot
x_chi <- seq(0, 25, length.out = 1000)
y_chi  <- dchisq(x_chi, df = df_chi)

plot(x_chi, y_chi, type = 'l', lwd = 2, col = 'blue',
     main = expression(paste(chi^2, '(10) Distribution')),
     xlab = expression(chi^2), ylab = 'Density')

abline(v = chi_critical, col = 'red', lwd = 2, lty = 2)

x_shade <- x_chi[x_chi >= chi_critical]
y_shade  <- dchisq(x_shade, df = df_chi)
polygon(c(chi_critical, x_shade, max(x_chi)), c(0, y_shade, 0),
        col = rgb(1, 0, 0, 0.3), border = NA)

legend('topright',
       legend = c('PDF',
                  sprintf('Critical value = %.2f', chi_critical)),
       col = c('blue', 'red'),
       lty = c(1, 2),
       lwd = c(2, 2))
grid()

# F plot
x_f <- seq(0, 5, length.out = 1000)
y_f  <- df(x_f, df1 = df1, df2 = df2)

plot(x_f, y_f, type = 'l', lwd = 2, col = 'blue',
     main = 'F(5, 10) Distribution',
     xlab = 'F', ylab = 'Density')

abline(v = f_critical, col = 'red', lwd = 2, lty = 2)

x_shade <- x_f[x_f >= f_critical]
y_shade  <- df(x_shade, df1 = df1, df2 = df2)
polygon(c(f_critical, x_shade, max(x_f)), c(0, y_shade, 0),
        col = rgb(1, 0, 0, 0.3), border = NA)

legend('topright',
       legend = c('PDF',
                  sprintf('Critical value = %.2f', f_critical)),
       col = c('blue', 'red'),
       lty = c(1, 2),
       lwd = c(2, 2))
grid()

par(mfrow = c(1, 1))
