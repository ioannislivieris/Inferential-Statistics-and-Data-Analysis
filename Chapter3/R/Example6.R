# Chapter 3 - Binomial Distribution
# Example 6: Customer Satisfaction Survey — Event Analysis  B(20, 0.65)

# Parameters
n <- 20
p <- 0.65

# Events:
#   A: X >= 15  (at least 15 satisfied customers)
#   B: X <= 17  (at most 17 satisfied customers)
#   A ∩ B: 15 <= X <= 17

# i. Calculate probabilities
prob_A       <- 1 - pbinom(14, n, p)
prob_B       <- pbinom(17, n, p)
prob_A_and_B <- pbinom(17, n, p) - pbinom(14, n, p)
prob_A_or_B  <- prob_A + prob_B - prob_A_and_B

cat("i. Probabilities:\n")
cat(sprintf("   P(A) = P(X >= 15)          = %.4f\n", prob_A))
cat(sprintf("   P(B) = P(X <= 17)          = %.4f\n", prob_B))
cat(sprintf("   P(A ∩ B) = P(15<=X<=17)    = %.4f\n", prob_A_and_B))
cat(sprintf("   P(A ∪ B)                   = %.4f\n", prob_A_or_B))

# ii. Conditional probability P(A|B)
prob_A_given_B <- prob_A_and_B / prob_B
cat(sprintf("\nii. P(A|B) = %.4f\n", prob_A_given_B))
cat("    Interpretation: Given that at most 17 customers are satisfied,\n")
cat(sprintf("    there is a %.2f%% probability that at least 15 are satisfied.\n",
            prob_A_given_B * 100))

# iii. Test independence
prob_A_times_B <- prob_A * prob_B
is_independent  <- abs(prob_A_and_B - prob_A_times_B) < 0.0001

cat("\niii. Independence test:\n")
cat(sprintf("     P(A ∩ B)   = %.4f\n", prob_A_and_B))
cat(sprintf("     P(A)·P(B)  = %.4f\n", prob_A_times_B))
cat(sprintf("     Events A and B are %s\n",
            ifelse(is_independent, "independent", "NOT independent")))

# iv. Visualization
x   <- 0:n
pmf <- dbinom(x, n, p)

par(mfrow = c(1, 2))

# Bar plot with highlighted regions
barplot(pmf, names.arg = x, col = 'lightgray', border = 'black',
        xlab = 'Number of Satisfied Customers (X)',
        ylab = 'Probability',
        main = 'Events A and B on Binomial Distribution',
        cex.names = 0.8)
rect( 0 - 0.5, 0, 14.5,      max(pmf) * 1.1, col = rgb(0, 0, 1, 0.1),  border = NA)
rect(14.5,     0, 17.5,      max(pmf) * 1.1, col = rgb(1, 0, 1, 0.2),  border = NA)
rect(17.5,     0, n + 0.5,   max(pmf) * 1.1, col = rgb(1, 0, 0, 0.1),  border = NA)
legend('topleft',
       legend = c('B only (X<=14)', 'A∩B (15<=X<=17)', 'A only (X>=18)'),
       fill   = c(rgb(0,0,1,0.2), rgb(1,0,1,0.3), rgb(1,0,0,0.2)),
       cex    = 0.7)

# Probability summary
region_probs   <- c(prob_A_and_B,
                    prob_A - prob_A_and_B,
                    prob_B - prob_A_and_B,
                    1 - prob_A_or_B)
region_labels  <- c('A∩B', 'A only', 'B only', 'Neither')
region_colors  <- c(rgb(1,0,1,0.5), rgb(1,0,0,0.3), rgb(0,0,1,0.3), 'lightgray')

barplot(region_probs, names.arg = region_labels, col = region_colors,
        border = 'black', ylab = 'Probability',
        main   = 'Probability Regions', ylim = c(0, max(region_probs) * 1.2))
text(x      = seq(0.7, by = 1.2, length.out = 4),
     y      = region_probs + 0.02,
     labels = sprintf("%.4f", region_probs), cex = 0.9)

par(mfrow = c(1, 1))
