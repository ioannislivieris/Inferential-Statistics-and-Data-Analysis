# Chapter 10 - Δειγματοληπτικές Κατανομές και Κεντρικό Οριακό Θεώρημα
# Example 3: Επαλήθευση ΚΟΘ με Q-Q Plots
#   4 αρχικές κατανομές, n=30, 1000 δείγματα ανά κατανομή

set.seed(42)
n_simulations <- 1000
n             <- 30  # Sample size

# Generate sample means from different distributions
distributions <- list(
  "Uniform(0,10)"       = function() runif(n, 0, 10),
  "Exponential(l=0.5)"  = function() rexp(n, rate = 0.5),
  "Chi-square(df=3)"    = function() rchisq(n, df = 3),
  "Normal(50,10)"       = function() rnorm(n, mean = 50, sd = 10)
)

par(mfrow = c(2, 2))

for (dist_name in names(distributions)) {
  # Generate sample means
  sample_means <- replicate(n_simulations,
                             mean(distributions[[dist_name]]()))

  # Q-Q plot
  qqnorm(sample_means,
         main = paste("Q-Q Plot:", dist_name),
         pch  = 16, col = "blue", cex = 0.5)
  qqline(sample_means, col = "red", lwd = 2)

  legend("topleft",
         legend = paste("n =", n),
         bty    = "n", cex = 1.1, font = 2)
}

par(mfrow = c(1, 1))
