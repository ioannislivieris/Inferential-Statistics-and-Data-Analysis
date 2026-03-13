# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 2: Τυποποίηση και υπολογισμοί  X ~ N(100, 15²)

# Parameters
mu    <- 100
sigma <- 15

# i. Z-score for X = 120
x       <- 120
z_score <- (x - mu) / sigma
cat(sprintf("Z-score for X = 120: %.2f\n", z_score))

# ii. P(X <= 120)
prob <- pnorm(x, mean = mu, sd = sigma)
cat(sprintf("P(X <= 120) = %.4f\n", prob))

# Alternatively using z-score
prob_z <- pnorm(z_score)
cat(sprintf("P(X <= 120) using z-score = %.4f\n", prob_z))

# iii. Find x such that P(X <= x) = 0.90
x_90 <- qnorm(0.90, mean = mu, sd = sigma)
cat(sprintf("X value at 90th percentile: %.2f\n", x_90))

# Verify using z-score
z_90       <- qnorm(0.90)
x_90_manual <- mu + z_90 * sigma
cat(sprintf("X value using z-score: %.2f\n", x_90_manual))
