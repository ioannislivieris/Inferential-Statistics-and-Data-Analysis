# Chapter 4 - Poisson Distribution
# Example 6: Poisson Approximation to Binomial  B(100, 0.03) ≈ Poisson(3)

# Parameters
n      <- 100
p      <- 0.03
lambda <- n * p   # lambda = 3

# Range of values
k <- 0:15

# Binomial probabilities
binomial_probs <- dbinom(k, n, p)

# Poisson probabilities
poisson_probs <- dpois(k, lambda)

# Plot comparison
barplot(rbind(binomial_probs, poisson_probs),
        beside    = TRUE, names.arg = k,
        col       = c('skyblue', 'coral'),
        xlab      = 'k', ylab = 'Probability',
        main      = 'Binomial(100, 0.03) vs Poisson(3)',
        legend.text = c('Binomial', 'Poisson'),
        args.legend = list(x = 'topright'))

# Maximum absolute difference
max_diff <- max(abs(binomial_probs - poisson_probs))
cat(sprintf("Maximum difference: %.6f\n", max_diff))

# Comparison table
comparison <- data.frame(
  k          = k,
  Binomial   = round(binomial_probs, 6),
  Poisson    = round(poisson_probs, 6),
  Difference = round(abs(binomial_probs - poisson_probs), 6)
)
print(head(comparison, 10))
