# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 5: Σύγκριση Κατανομών t (df = 3, 10, 30) vs N(0,1)

# Compare t-distributions with different degrees of freedom
x <- seq(-4, 4, length.out = 1000)

# Calculate densities
y_t3   <- dt(x, df = 3)
y_t10  <- dt(x, df = 10)
y_t30  <- dt(x, df = 30)
y_norm <- dnorm(x)

# Plot
plot(x, y_norm, type = 'l', lwd = 2, col = 'black',
     main = 't-Distributions with Different Degrees of Freedom',
     xlab = 't', ylab = 'Density',
     ylim = c(0, max(y_norm) * 1.1))

lines(x, y_t3,  lwd = 2, col = 'red')
lines(x, y_t10, lwd = 2, col = 'blue')
lines(x, y_t30, lwd = 2, col = 'green')

legend('topright',
       legend = c('N(0,1)', 't(3)', 't(10)', 't(30)'),
       col    = c('black', 'red', 'blue', 'green'),
       lty    = 1,
       lwd    = 2)

grid()

# Add text annotation
text(0, max(y_norm) * 0.9,
     'As df increases,\nt approaches N(0,1)',
     cex = 0.9)
