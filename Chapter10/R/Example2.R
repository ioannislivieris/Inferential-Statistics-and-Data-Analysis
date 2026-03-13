# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 2: ΚΟΘ με Εκθετική Κατανομή (Exp λ=0.5)
#   Έντονα ασύμμετρη — n = 5, 10, 30, 100

set.seed(42)
n_simulations <- 10000
lambda        <- 0.5
sample_sizes  <- c(5, 10, 30, 100)

# Population parameters
pop_mean <- 1 / lambda  # = 2
pop_sd   <- 1 / lambda  # = 2

par(mfrow = c(2, 3))

# Plot original exponential distribution
x_exp <- seq(0, 10, length.out = 200)
y_exp <- dexp(x_exp, rate = lambda)
plot(x_exp, y_exp, type = "l", lwd = 2, col = "blue",
     main = "Original Exponential Distribution",
     xlab = "x", ylab = "Density")

# Plot sampling distributions for each sample size
for (n in sample_sizes) {
  sample_means <- replicate(n_simulations, {
    mean(rexp(n, rate = lambda))
  })

  se <- pop_sd / sqrt(n)

  hist(sample_means, breaks = 50, freq = FALSE,
       col    = "lightblue", border = "black",
       main   = paste("n =", n),
       xlab   = "Sample Mean",
       ylab   = "Density",
       xlim   = c(0, 5))

  x <- seq(min(sample_means), max(sample_means), length.out = 200)
  y <- dnorm(x, mean = pop_mean, sd = se)
  lines(x, y, col = "red", lwd = 2)

  abline(v = pop_mean, col = "darkgreen", lwd = 2, lty = 2)
}

par(mfrow = c(1, 1))
