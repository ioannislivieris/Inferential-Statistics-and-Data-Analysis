# Chapter 4 - Poisson Distribution
# Example 3: Visualization of Poisson(7)

# Parameter
lambda <- 7

# Values (0 to 20 covers most of the distribution)
x <- 0:20

# Calculate probabilities
pmf <- dpois(x, lambda)

# Create plot
barplot(pmf, names.arg = x, col = 'darkgreen',
        xlab   = 'Number of Events (k)',
        ylab   = 'Probability P(X = k)',
        main   = paste0('Poisson Distribution with lambda = ', lambda),
        border = 'black')

# Mark mean value (= lambda)
abline(v = lambda + 0.5, col = 'red', lwd = 2, lty = 2)
legend('topright',
       legend = paste('Mean = lambda =', lambda),
       col = 'red', lty = 2, lwd = 2)
