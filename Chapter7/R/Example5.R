# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 5: Πλήρης Επιχειρηματική Ανάλυση Πωλήσεων
#   X ~ N(50.000, 8.000²)

# Parameters
mu    <- 50000
sigma <- 8000

# 1. Probabilities for different ranges
cat("=== Sales Analysis Report ===\n\n")

# Below average
prob_below_avg <- pnorm(mu, mean = mu, sd = sigma)
cat(sprintf("1. Probability of below-average sales: %.2f%%\n",
            prob_below_avg * 100))

# Above 60000
prob_above_60k <- 1 - pnorm(60000, mean = mu, sd = sigma)
cat(sprintf("2. Probability of sales > 60,000: %.2f%%\n",
            prob_above_60k * 100))

# Between 45000 and 55000
prob_middle <- pnorm(55000, mean = mu, sd = sigma) -
  pnorm(45000, mean = mu, sd = sigma)
cat(sprintf("3. Probability of sales between 45K-55K: %.2f%%\n",
            prob_middle * 100))

# 2. Key quantiles
cat("\n=== Performance Quantiles ===\n")
quantiles <- c(0.1, 0.25, 0.5, 0.75, 0.9, 0.95)
values    <- qnorm(quantiles, mean = mu, sd = sigma)

for (i in 1:length(quantiles)) {
  cat(sprintf("%dth percentile: EUR %.0f\n",
              quantiles[i] * 100, values[i]))
}

# 3. Visualization
x <- seq(mu - 4*sigma, mu + 4*sigma, length.out = 1000)
y <- dnorm(x, mean = mu, sd = sigma)

plot(x, y, type = 'l', lwd = 2, col = 'blue',
     main = 'Sales Distribution Analysis',
     xlab = 'Sales (EUR)', ylab = 'Density')

# Shade regions
# Below target (45000)
x_low <- x[x <= 45000]
y_low <- dnorm(x_low, mean = mu, sd = sigma)
polygon(c(min(x), x_low, 45000), c(0, y_low, 0),
        col = rgb(1, 0, 0, 0.3), border = NA)

# Target range (45000-55000)
x_mid <- x[x >= 45000 & x <= 55000]
y_mid <- dnorm(x_mid, mean = mu, sd = sigma)
polygon(c(45000, x_mid, 55000), c(0, y_mid, 0),
        col = rgb(0, 1, 0, 0.3), border = NA)

# Excellent (above 60000)
x_high <- x[x >= 60000]
y_high <- dnorm(x_high, mean = mu, sd = sigma)
polygon(c(60000, x_high, max(x)), c(0, y_high, 0),
        col = rgb(0, 0, 1, 0.3), border = NA)

# Add reference lines
abline(v = mu, col = 'black', lwd = 2, lty = 2)
abline(v = c(45000, 55000, 60000),
       col = 'darkgray', lwd = 1.5, lty = 3)

# Labels
text(mu,    max(y) * 1.05,
     sprintf('Mean = EUR %.0f', mu), col = 'black', cex = 0.9)
text(40000, max(y) * 0.5, 'Below\nTarget',     col = 'red',       cex = 0.8)
text(50000, max(y) * 0.3, 'Target\nRange',     col = 'darkgreen', cex = 0.8)
text(65000, max(y) * 0.5, 'Excellent',         col = 'blue',      cex = 0.8)

legend('topright',
       legend = c('Below Target (<45K)',
                  'Target Range (45K-55K)',
                  'Excellent (>60K)'),
       fill   = c(rgb(1,0,0,0.3), rgb(0,1,0,0.3), rgb(0,0,1,0.3)),
       cex    = 0.8)

grid()
