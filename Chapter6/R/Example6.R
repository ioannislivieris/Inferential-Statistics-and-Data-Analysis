# Chapter 6 - Κανονική Κατανομή
# Example 6: Quality Control  X ~ N(25, 0.5²)
#   LSL = 24 mm,  USL = 26 mm

# Parameters
mu    <- 25
sigma <- 0.5
LSL   <- 24   # Lower Specification Limit
USL   <- 26   # Upper Specification Limit

# i. Percentage within specifications
prob_within_spec <- pnorm(USL, mu, sigma) -
  pnorm(LSL, mu, sigma)
cat(sprintf("i. Percentage within specs: %.2f%%\n",
            prob_within_spec * 100))

# ii. Process capability index Cp
Cp <- (USL - LSL) / (6 * sigma)
cat(sprintf("\nii. Process capability Cp: %.3f\n", Cp))

if (Cp >= 1.33) {
  cat("Process is capable (Cp >= 1.33)\n")
} else if (Cp >= 1) {
  cat("Process is minimally capable (1 <= Cp < 1.33)\n")
} else {
  cat("Process is not capable (Cp < 1)\n")
}

# iii. Required sigma for Cp = 1.33
target_Cp      <- 1.33
required_sigma <- (USL - LSL) / (6 * target_Cp)
cat(sprintf("\niii. Required SD for Cp=1.33: %.4f mm\n",
            required_sigma))
cat(sprintf("Current SD: %.4f mm\n", sigma))
cat(sprintf("Reduction needed: %.2f%%\n",
            (1 - required_sigma / sigma) * 100))

# Visualization
x <- seq(mu - 4*sigma, mu + 4*sigma, length.out = 1000)
y <- dnorm(x, mu, sigma)

plot(x, y, type = 'l', lwd = 2, col = 'blue',
     xlab = 'Diameter (mm)', ylab = 'Density',
     main = 'Process Distribution vs Specifications')

# Specification limits
abline(v = c(LSL, USL), col = 'red', lwd = 2, lty = 2)

# Shade area within specs
x_within <- x[x >= LSL & x <= USL]
y_within  <- y[x >= LSL & x <= USL]
polygon(c(LSL, x_within, USL), c(0, y_within, 0),
        col = rgb(0, 1, 0, 0.3), border = NA)

legend('topright',
       legend = c('Process Distribution', 'Specification Limits',
                  'Within Specs'),
       col    = c('blue', 'red', 'green'),
       lty    = c(1, 2, NA),
       fill   = c(NA, NA, rgb(0, 1, 0, 0.3)),
       lwd    = c(2, 2, NA))
