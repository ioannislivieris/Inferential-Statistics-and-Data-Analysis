# Chapter 11 - Σημειακή Εκτίμηση
# Example 1: Βασικοί Εκτιμητές
#   N(100, 15^2), n=50: x̄, S², σ̂²_MLE, SE(x̄)

# Simulated sample from N(100, 15^2)
set.seed(42)
n           <- 50
sample_data <- rnorm(n, mean = 100, sd = 15)

# Point estimates for mean
mean_estimate <- mean(sample_data)
cat(sprintf("Mean estimate: %.4f\n", mean_estimate))

# Point estimates for variance
# Unbiased estimator S^2 (divides by n-1)
var_unbiased <- var(sample_data)
# MLE estimator (divides by n)
var_mle <- var(sample_data) * (n - 1) / n

cat(sprintf("Unbiased variance (S^2): %.4f\n", var_unbiased))
cat(sprintf("MLE variance:            %.4f\n", var_mle))

# Standard deviation estimates
sd_unbiased <- sd(sample_data)
sd_mle      <- sqrt(var_mle)

cat(sprintf("Unbiased SD: %.4f\n", sd_unbiased))
cat(sprintf("MLE SD:      %.4f\n", sd_mle))

# Standard error of the mean
se_mean <- sd(sample_data) / sqrt(n)
cat(sprintf("SE of mean:  %.4f\n", se_mean))

# Summary comparison
cat("\n--- Comparison of Unbiased vs MLE ---\n")
cat(sprintf("True sigma^2 = 225\n"))
cat(sprintf("S^2 (unbiased) = %.4f  |  bias ≈ 0\n", var_unbiased))
cat(sprintf("MLE var        = %.4f  |  bias = -sigma^2/n = %.4f\n",
            var_mle, -225 / n))
