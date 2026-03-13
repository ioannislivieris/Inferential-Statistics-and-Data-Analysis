# Chapter 3 - Binomial Distribution
# Example 5: Comparing B(20, p) for p = 0.2, 0.5, 0.8

# Parameters
n     <- 20
probs <- c(0.2, 0.5, 0.8)
x     <- 0:n

# Individual plots + comparison
par(mfrow = c(2, 2))

for (p in probs) {
  pmf      <- dbinom(x, n, p)
  mean_val <- n * p
  sd_val   <- sqrt(n * p * (1 - p))
  barplot(pmf, names.arg = x, col = 'steelblue',
          xlab   = 'k', ylab = 'P(X = k)',
          main   = sprintf('B(%d, %.1f): E(X)=%.1f, SD=%.2f', n, p, mean_val, sd_val),
          border = 'black')
}

# Overlay comparison
plot(x, dbinom(x, n, probs[1]), type = 'b', pch = 19, col = 'blue',
     xlab = 'k', ylab = 'P(X = k)', main = 'Distribution Comparison',
     ylim = c(0, 0.25), lwd = 2)
lines(x, dbinom(x, n, probs[2]), type = 'b', pch = 19, col = 'red',   lwd = 2)
lines(x, dbinom(x, n, probs[3]), type = 'b', pch = 19, col = 'green', lwd = 2)
legend('topright',
       legend = paste('p =', probs),
       col    = c('blue', 'red', 'green'), lwd = 2, pch = 19)

par(mfrow = c(1, 1))
