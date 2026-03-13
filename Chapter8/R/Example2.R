# Chapter 8 - Άλλες Σημαντικές Συνεχείς Κατανομές
# Example 2: Εκθετική Κατανομή  X ~ Exp(λ = 0.5)

# Parameter (rate)
lambda <- 0.5

# i. P(X <= 2)
prob1 <- pexp(2, rate = lambda)
cat(sprintf("P(X <= 2) = %.4f\n", prob1))

# ii. P(X > 3)
prob2 <- 1 - pexp(3, rate = lambda)
cat(sprintf("P(X > 3) = %.4f\n", prob2))

# iii. Median
median_x         <- qexp(0.5, rate = lambda)
median_theoretical <- log(2) / lambda
cat(sprintf("Median: %.4f\n", median_x))
cat(sprintf("Theoretical median: %.4f\n", median_theoretical))

# Mean
mean_x <- 1 / lambda
cat(sprintf("Mean: %.4f\n", mean_x))

# Visualization
x <- seq(0, 10, length.out = 1000)
y <- dexp(x, rate = lambda)

plot(x, y, type = 'l', lwd = 2, col = 'blue',
     main = expression(paste('Exponential Distribution, ',
                             lambda, ' = 0.5')),
     xlab = 'x', ylab = 'Density')

# Mark mean and median
abline(v = mean_x,   col = 'red',   lwd = 2, lty = 2)
abline(v = median_x, col = 'green', lwd = 2, lty = 3)

# Shade area for P(X > 3)
x_shade <- x[x >= 3]
y_shade  <- dexp(x_shade, rate = lambda)
polygon(c(3, x_shade, max(x)), c(0, y_shade, 0),
        col = rgb(1, 0, 0, 0.2), border = NA)

legend('topright',
       legend = c('PDF',
                  sprintf('Mean = %.2f',   mean_x),
                  sprintf('Median = %.2f', median_x),
                  sprintf('P(X > 3) = %.2f', prob2)),
       col  = c('blue', 'red', 'green', rgb(1,0,0,0.2)),
       lty  = c(1, 2, 3, NA),
       lwd  = c(2, 2, 2, NA),
       fill = c(NA, NA, NA, rgb(1,0,0,0.2)))

grid()
