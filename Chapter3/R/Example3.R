# Chapter 3 - Binomial Distribution
# Example 3: Visualization of B(20, 0.4)

# Parameters
n <- 20
p <- 0.4

# Values of x
x <- 0:n

# Calculate probabilities
pmf <- dbinom(x, n, p)

# Create plot
barplot(pmf, names.arg = x, col = 'steelblue',
        xlab   = 'Number of Successes (k)',
        ylab   = 'Probability P(X = k)',
        main   = paste0('Binomial Distribution B(', n, ', ', p, ')'),
        border = 'black')

# Mark mean value
mean_val <- n * p
abline(v = mean_val + 0.5, col = 'red', lwd = 2, lty = 2)
legend('topright',
       legend = paste('Mean =', mean_val),
       col = 'red', lty = 2, lwd = 2)
