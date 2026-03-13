# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 6: Σύγκριση Κατανομών χ² (df = 2, 5, 10, 15)

# Compare chi-square distributions with different degrees of freedom
x <- seq(0, 30, length.out = 1000)

# Calculate densities
y_chi2  <- dchisq(x, df = 2)
y_chi5  <- dchisq(x, df = 5)
y_chi10 <- dchisq(x, df = 10)
y_chi15 <- dchisq(x, df = 15)

# Plot
plot(x, y_chi2, type = 'l', lwd = 2, col = 'red',
     main = expression(paste(chi^2,
           '-Distributions with Different Degrees of Freedom')),
     xlab = expression(chi^2), ylab = 'Density',
     ylim = c(0, max(y_chi2) * 1.1))

lines(x, y_chi5,  lwd = 2, col = 'blue')
lines(x, y_chi10, lwd = 2, col = 'green')
lines(x, y_chi15, lwd = 2, col = 'purple')

# Mark means (mean of chi^2(nu) = nu)
abline(v = 2,  col = 'red',    lty = 3)
abline(v = 5,  col = 'blue',   lty = 3)
abline(v = 10, col = 'green',  lty = 3)
abline(v = 15, col = 'purple', lty = 3)

legend('topright',
       legend = c(expression(chi^2*(2)),
                  expression(chi^2*(5)),
                  expression(chi^2*(10)),
                  expression(chi^2*(15))),
       col = c('red', 'blue', 'green', 'purple'),
       lty = 1,
       lwd = 2)

grid()

# Add text annotation
text(20, max(y_chi2) * 0.9,
     expression(paste('Mean = ', nu, ', Var = 2', nu)),
     cex = 0.9)
