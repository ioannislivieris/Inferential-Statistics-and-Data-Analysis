# Chapter 3 - Binomial Distribution
# Example 7: Comparing Two Production Lines  A~B(50,0.08), B~B(60,0.05)

# Parameters
n_A <- 50;  p_A <- 0.08
n_B <- 60;  p_B <- 0.05

# i. P(X_A = 4 and X_B = 3)  — independent lines
prob_A_4  <- dbinom(4, n_A, p_A)
prob_B_3  <- dbinom(3, n_B, p_B)
prob_both <- prob_A_4 * prob_B_3
cat(sprintf("i. P(X_A=4 and X_B=3) = %.6f\n", prob_both))

# ii. P(X_A > 5 or X_B > 5)
prob_A_gt5    <- 1 - pbinom(5, n_A, p_A)
prob_B_gt5    <- 1 - pbinom(5, n_B, p_B)
prob_both_gt5 <- prob_A_gt5 * prob_B_gt5
prob_union    <- prob_A_gt5 + prob_B_gt5 - prob_both_gt5
cat(sprintf("\nii. P(X_A>5 or X_B>5) = %.6f\n", prob_union))
cat(sprintf("    P(X_A>5) = %.6f\n", prob_A_gt5))
cat(sprintf("    P(X_B>5) = %.6f\n", prob_B_gt5))

# iii. Expected total defects and standard deviation
mean_A    <- n_A * p_A;  mean_B <- n_B * p_B
var_A     <- n_A * p_A * (1 - p_A);  var_B <- n_B * p_B * (1 - p_B)
mean_total <- mean_A + mean_B
sd_total   <- sqrt(var_A + var_B)

cat(sprintf("\niii. Expected defects:\n"))
cat(sprintf("     Line A: %.2f\n", mean_A))
cat(sprintf("     Line B: %.2f\n", mean_B))
cat(sprintf("     Total:  %.2f\n", mean_total))
cat(sprintf("     Std Dev: %.2f\n", sd_total))

# iv. Comparison plots
par(mfrow = c(1, 2))

x_A   <- 0:n_A
pmf_A <- dbinom(x_A, n_A, p_A)
barplot(pmf_A, names.arg = x_A, col = 'steelblue',
        xlab = 'Number of Defects', ylab = 'Probability',
        main = paste0('Line A: B(', n_A, ', ', p_A, ')'),
        border = 'black', las = 1, cex.names = 0.7)
abline(v = mean_A + 0.5, col = 'red', lwd = 2, lty = 2)

x_B   <- 0:n_B
pmf_B <- dbinom(x_B, n_B, p_B)
barplot(pmf_B, names.arg = x_B, col = 'coral',
        xlab = 'Number of Defects', ylab = 'Probability',
        main = paste0('Line B: B(', n_B, ', ', p_B, ')'),
        border = 'black', las = 1, cex.names = 0.7)
abline(v = mean_B + 0.5, col = 'red', lwd = 2, lty = 2)

par(mfrow = c(1, 1))

# Overlay comparison
plot(x_A, pmf_A, type = 'b', pch = 19, col = 'steelblue', lwd = 2,
     xlim = c(0, max(n_A, n_B) * p_A * 3),
     xlab = 'Number of Defects', ylab = 'Probability',
     main = 'Comparison of Two Production Lines')
lines(x_B, pmf_B, type = 'b', pch = 19, col = 'coral', lwd = 2)
legend('topright',
       legend = c(paste('Line A: B(', n_A, ',', p_A, ')'),
                  paste('Line B: B(', n_B, ',', p_B, ')')),
       col = c('steelblue', 'coral'), lwd = 2, pch = 19)
