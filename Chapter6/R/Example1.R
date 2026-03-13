# Chapter 6 - Κανονική Κατανομή
# Example 1: Υπολογισμός πιθανοτήτων  X ~ N(100, 15²)

# Parameters
mu <- 100
sigma <- 15

# P(X <= 120)
prob1 <- pnorm(120, mean = mu, sd = sigma)
cat(sprintf("P(X <= 120) = %.4f\n", prob1))

# P(X > 90) = 1 - P(X <= 90)
prob2 <- 1 - pnorm(90, mean = mu, sd = sigma)
cat(sprintf("P(X > 90) = %.4f\n", prob2))

# P(85 < X < 110) = P(X < 110) - P(X < 85)
prob3 <- pnorm(110, mean = mu, sd = sigma) -
  pnorm(85, mean = mu, sd = sigma)
cat(sprintf("P(85 < X < 110) = %.4f\n", prob3))
