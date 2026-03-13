# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 3: Οπτικοποίηση τυπικής κανονικής  Z ~ N(0, 1)
#   Κρίσιμες τιμές ±1.96 (95%) και ±1 (68%)

# Generate z values
z <- seq(-4, 4, length.out = 1000)
y <- dnorm(z)

# Create plot
plot(z, y, type = 'l', lwd = 2, col = 'blue',
     xlab = 'z', ylab = expression(phi(z)),
     main = 'Standard Normal Distribution')

# Add critical values
abline(v = c(-1.96, 1.96), col = 'red', lwd = 2, lty = 2)
abline(v = c(-1, 0, 1),   col = 'gray', lwd = 1, lty = 3)

# Shade areas
z_shade1 <- z[z >= -1.96 & z <= 1.96]
y_shade1  <- dnorm(z_shade1)
polygon(c(-1.96, z_shade1, 1.96), c(0, y_shade1, 0),
        col = rgb(0, 0, 1, 0.2), border = NA)

# Add labels
text(0, max(y) * 0.9,
     '95% of data\nbetween -1.96 and 1.96', col = 'red')
text(0, max(y) * 0.5, expression(mu == 0), cex = 1.2)
text(1, max(y) * 0.3, expression(sigma == 1), cex = 1.2)

# Add legend
legend('topright',
       legend = c('PDF', '+/-1.96 (95%)', '+/-1 (68%)'),
       col    = c('blue', 'red', 'gray'),
       lty    = c(1, 2, 3),
       lwd    = c(2, 2, 1))

grid()
