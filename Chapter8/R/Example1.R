# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 1: Ομοιόμορφη Κατανομή  X ~ U(5, 15)

# Parameters
a <- 5
b <- 15

# i. P(X <= 10)
prob1 <- punif(10, min = a, max = b)
cat(sprintf("P(X <= 10) = %.4f\n", prob1))

# ii. P(8 < X < 12)
prob2 <- punif(12, min = a, max = b) - punif(8, min = a, max = b)
cat(sprintf("P(8 < X < 12) = %.4f\n", prob2))

# iii. 75th percentile
q75 <- qunif(0.75, min = a, max = b)
cat(sprintf("75th percentile: %.2f\n", q75))

# Visualization
x <- seq(a - 2, b + 2, length.out = 1000)
y <- dunif(x, min = a, max = b)

plot(x, y, type = 'l', lwd = 2, col = 'blue',
     main = 'Uniform Distribution U(5, 15)',
     xlab = 'x', ylab = 'Density',
     ylim = c(0, max(y) * 1.2))

# Shade area for P(8 < X < 12)
x_shade <- seq(8, 12, length.out = 100)
y_shade  <- dunif(x_shade, min = a, max = b)
polygon(c(8, x_shade, 12), c(0, y_shade, 0),
        col = rgb(0, 0, 1, 0.3), border = NA)

abline(v = c(a, b), col = 'red', lty = 2)
text(10, max(y) * 0.5, sprintf('P(8 < X < 12) = %.2f', prob2))

legend('topright',
       legend = c('PDF', 'Support [a,b]'),
       col    = c('blue', 'red'),
       lty    = c(1, 2),
       lwd    = c(2, 1))

grid()
