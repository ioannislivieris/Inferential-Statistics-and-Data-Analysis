# Chapter 4 - Poisson Distribution
# Example 5: Comparing Poisson(λ) for λ = 2, 5, 10

# Parameters
lambdas <- c(2, 5, 10)

# Individual plots + comparison
par(mfrow = c(2, 2))

for (lambda in lambdas) {
  x   <- 0:(lambda * 3)
  pmf <- dpois(x, lambda)
  barplot(pmf, names.arg = x, col = 'darkgreen',
          xlab   = 'k', ylab = 'P(X = k)',
          main   = sprintf('Poisson(%d): Mean=%d, SD=%.2f',
                           lambda, lambda, sqrt(lambda)),
          border = 'black')
}

# Overlay comparison
x_max <- max(lambdas) * 3
plot(0:x_max, dpois(0:x_max, lambdas[1]),
     type = 'b', pch = 19, col = 'blue',
     xlab = 'k', ylab = 'P(X = k)',
     main = 'Distribution Comparison',
     ylim = c(0, 0.4), lwd = 2)
lines(0:x_max, dpois(0:x_max, lambdas[2]),
      type = 'b', pch = 19, col = 'red',   lwd = 2)
lines(0:x_max, dpois(0:x_max, lambdas[3]),
      type = 'b', pch = 19, col = 'green', lwd = 2)
legend('topright',
       legend = paste('lambda =', lambdas),
       col    = c('blue', 'red', 'green'), lwd = 2, pch = 19)

par(mfrow = c(1, 1))
