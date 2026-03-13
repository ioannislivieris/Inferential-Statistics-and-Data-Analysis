# Chapter 6 - Κανονική Κατανομή
# Example 5: Σύγκριση Κατανομών
#   N(50, 5²), N(50, 10²), N(60, 5²)

# x range
x <- seq(20, 80, length.out = 1000)

# Three distributions
y1 <- dnorm(x, mean = 50, sd = 5)
y2 <- dnorm(x, mean = 50, sd = 10)
y3 <- dnorm(x, mean = 60, sd = 5)

# Plot
plot(x, y1, type = 'l', lwd = 2, col = 'blue',
     xlab = 'x', ylab = 'f(x)',
     main = 'Comparison of Normal Distributions',
     ylim = c(0, max(c(y1, y2, y3))))

lines(x, y2, lwd = 2, col = 'red')
lines(x, y3, lwd = 2, col = 'green')

legend('topright',
       legend = c('N(50, 5^2)', 'N(50, 10^2)', 'N(60, 5^2)'),
       col    = c('blue', 'red', 'green'),
       lwd    = 2)

grid()
