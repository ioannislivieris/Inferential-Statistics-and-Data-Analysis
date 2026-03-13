# Chapter 6 - Κανονική Κατανομή
# Example 3: Οπτικοποίηση Κατανομής  X ~ N(70, 12²)

# Parameters
mu <- 70
sigma <- 12

# x values
x <- seq(mu - 4*sigma, mu + 4*sigma, length.out = 1000)
y <- dnorm(x, mean = mu, sd = sigma)

# Plot
plot(x, y, type = 'l', lwd = 2, col = 'blue',
     xlab = 'x', ylab = 'f(x)',
     main = paste0('Normal Distribution N(', mu, ', ',
                   sigma, '^2)'))

# Mean line
abline(v = mu, col = 'red', lwd = 2, lty = 2)

# Standard deviation lines
abline(v = c(mu - sigma, mu + sigma), col = 'orange',
       lwd = 1.5, lty = 3)
abline(v = c(mu - 2*sigma, mu + 2*sigma), col = 'green',
       lwd = 1.5, lty = 3)

# Legend
legend('topright',
       legend = c('PDF', 'Mean', '+/-1 SD', '+/-2 SD'),
       col    = c('blue', 'red', 'orange', 'green'),
       lty    = c(1, 2, 3, 3),
       lwd    = c(2, 2, 1.5, 1.5))

# Add text annotations
text(mu, max(y) * 0.9,
     paste0('Mean = ', mu), col = 'red')
text(mu + sigma, max(y) * 0.5,
     paste0('+1 SD\n68%'), col = 'orange')
text(mu + 2*sigma, max(y) * 0.3,
     paste0('+2 SD\n95%'), col = 'green')
