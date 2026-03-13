# Chapter 7 - Τυπική Κανονική Κατανομή
# Example 4: Επαλήθευση Εμπειρικού Κανόνα (68-95-99.7)

# Calculate exact probabilities
prob_1sd <- pnorm(1)  - pnorm(-1)
prob_2sd <- pnorm(2)  - pnorm(-2)
prob_3sd <- pnorm(3)  - pnorm(-3)

# Display results
cat("Empirical Rule Verification:\n")
cat(sprintf("Within +/-1 SD: %.4f (%.2f%%) [Expected: 68%%]\n",
            prob_1sd, prob_1sd * 100))
cat(sprintf("Within +/-2 SD: %.4f (%.2f%%) [Expected: 95%%]\n",
            prob_2sd, prob_2sd * 100))
cat(sprintf("Within +/-3 SD: %.4f (%.2f%%) [Expected: 99.7%%]\n",
            prob_3sd, prob_3sd * 100))

# Create visualization
z <- seq(-4, 4, length.out = 1000)
y <- dnorm(z)

plot(z, y, type = 'l', lwd = 2, col = 'blue',
     main = 'Empirical Rule Visualization',
     xlab = 'Standard Deviations from Mean',
     ylab = 'Density')

# Shade regions
colors <- c(rgb(1,0,0,0.2), rgb(0,1,0,0.2), rgb(0,0,1,0.2))
limits <- list(c(-1,1), c(-2,2), c(-3,3))
labels <- c('68.27%', '95.45%', '99.73%')

for (i in 1:3) {
  z_region <- z[z >= limits[[i]][1] & z <= limits[[i]][2]]
  y_region <- dnorm(z_region)
  polygon(c(limits[[i]][1], z_region, limits[[i]][2]),
          c(0, y_region, 0), col = colors[i], border = NA)
}

# Add vertical lines
abline(v = c(-3,-2,-1,0,1,2,3), lty = 2, col = 'gray')

legend('topright',
       legend = labels,
       fill   = colors,
       title  = 'Within:')

grid()
