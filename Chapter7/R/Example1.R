# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 1: Υπολογισμός πιθανοτήτων  Z ~ N(0, 1)

# i. P(Z <= 1.5)
prob1 <- pnorm(1.5)
cat(sprintf("P(Z <= 1.5) = %.4f\n", prob1))

# ii. P(Z > -0.8) = 1 - P(Z <= -0.8)
prob2 <- 1 - pnorm(-0.8)
cat(sprintf("P(Z > -0.8) = %.4f\n", prob2))

# iii. P(-1 < Z < 2)
prob3 <- pnorm(2) - pnorm(-1)
cat(sprintf("P(-1 < Z < 2) = %.4f\n", prob3))
