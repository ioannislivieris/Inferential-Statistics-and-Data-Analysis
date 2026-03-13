# Chapter 4 - Poisson Distribution
# Example 9: Defect Analysis — Multiple Production Lines & Bayes
#   Line A (30%): Poisson(2)
#   Line B (45%): Poisson(3)
#   Line C (25%): Poisson(5)

# Parameters
lambda_A <- 2;  lambda_B <- 3;  lambda_C <- 5
p_A      <- 0.30; p_B <- 0.45; p_C <- 0.25

cat("=== Defects Analysis Multiple Lines ===\n\n")

# i. P(E1 ∪ E2) where E1={X>=4}, E2={X<=3}
# Note: E1 and E2 are complementary → P(E1 ∪ E2) = 1
prob_ge4_A <- 1 - ppois(3, lambda_A)
prob_ge4_B <- 1 - ppois(3, lambda_B)
prob_ge4_C <- 1 - ppois(3, lambda_C)
prob_ge4   <- prob_ge4_A * p_A + prob_ge4_B * p_B + prob_ge4_C * p_C

cat("i. Union of events:\n")
cat(sprintf("   P(X >= 4|A) = %.4f\n", prob_ge4_A))
cat(sprintf("   P(X >= 4|B) = %.4f\n", prob_ge4_B))
cat(sprintf("   P(X >= 4|C) = %.4f\n", prob_ge4_C))
cat(sprintf("   P(X >= 4)   = %.4f\n", prob_ge4))
cat(sprintf("   P(X <= 3)   = %.4f\n", 1 - prob_ge4))
cat(sprintf("   P(E1 ∪ E2)  = %.4f\n\n", prob_ge4 + (1 - prob_ge4)))

# ii. P(Line C | X = 4) — Bayes' Theorem
prob_4_A <- dpois(4, lambda_A)
prob_4_B <- dpois(4, lambda_B)
prob_4_C <- dpois(4, lambda_C)
prob_4   <- prob_4_A * p_A + prob_4_B * p_B + prob_4_C * p_C

prob_C_given_4 <- (prob_4_C * p_C) / prob_4

cat("ii. Bayes' Theorem:\n")
cat(sprintf("   P(X=4|A) = %.4f\n", prob_4_A))
cat(sprintf("   P(X=4|B) = %.4f\n", prob_4_B))
cat(sprintf("   P(X=4|C) = %.4f\n", prob_4_C))
cat(sprintf("   P(X=4)   = %.4f\n", prob_4))
cat(sprintf("   P(C | X=4) = %.4f\n\n", prob_C_given_4))

# iii. P(X=2 and all from A)
prob_2_A      <- dpois(2, lambda_A)
prob_2_all_A  <- prob_2_A * p_A
prob_2        <- dpois(2, lambda_A)*p_A + dpois(2, lambda_B)*p_B + dpois(2, lambda_C)*p_C

cat("iii. Poisson combined with binomial:\n")
cat(sprintf("   P(X=2|A) = %.4f\n", prob_2_A))
cat(sprintf("   P(X=2)   = %.4f\n", prob_2))
cat(sprintf("   P(X=2 and all from A) = %.4f\n\n", prob_2_all_A))

# Visualization
par(mfrow = c(2, 2))
x_vals     <- 0:12
colors     <- c('blue', 'darkgreen', 'red')
line_names <- c('Line A', 'Line B', 'Line C')
lambdas    <- c(lambda_A, lambda_B, lambda_C)

for (i in 1:3) {
  plot(x_vals, dpois(x_vals, lambdas[i]), type = 'h', lwd = 3,
       col  = colors[i], xlab = 'Defects', ylab = 'Probability',
       main = sprintf('%s: Poisson(%d)', line_names[i], lambdas[i]))
  abline(v = lambdas[i], col = 'orange', lty = 2, lwd = 2)
}

plot(x_vals, dpois(x_vals, lambda_A), type = 'b', pch = 19,
     col = 'blue', lwd = 2, xlab = 'Defects', ylab = 'Probability',
     main = 'Production Lines Comparison', ylim = c(0, 0.3))
lines(x_vals, dpois(x_vals, lambda_B), type = 'b', pch = 19, col = 'darkgreen', lwd = 2)
lines(x_vals, dpois(x_vals, lambda_C), type = 'b', pch = 19, col = 'red',       lwd = 2)
legend('topright',
       legend = c('A (λ=2)', 'B (λ=3)', 'C (λ=5)'),
       col = colors, lwd = 2, pch = 19)

par(mfrow = c(1, 1))

# Summary table
cat("\n=== Results Table ===\n")
cat("k\tP(X=k|A)\tP(X=k|B)\tP(X=k|C)\tP(X=k)\n")
cat(strrep("-", 65), "\n")
for (k in 0:8) {
  pa <- dpois(k, lambda_A); pb <- dpois(k, lambda_B); pc <- dpois(k, lambda_C)
  pk <- pa*p_A + pb*p_B + pc*p_C
  cat(sprintf("%d\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f\n", k, pa, pb, pc, pk))
}
