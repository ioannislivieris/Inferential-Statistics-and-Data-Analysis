# Chapter 11 - Σημειακή Εκτίμηση
# Example 3: MLE για Εκθετική Κατανομή
#   Exp(λ=0.5), n=100: λ̂_MLE = 1/x̄, οπτικοποίηση log-likelihood

# Generate sample from exponential distribution
set.seed(42)
true_lambda <- 0.5
n           <- 100
sample_exp  <- rexp(n, rate = true_lambda)

# MLE for lambda: λ̂ = 1 / x̄
lambda_mle <- 1 / mean(sample_exp)
cat(sprintf("True lambda:   %.4f\n", true_lambda))
cat(sprintf("MLE estimate:  %.4f\n", lambda_mle))
cat(sprintf("Sample mean:   %.4f  (= 1/lambda_mle)\n", mean(sample_exp)))

# Log-likelihood function: l(λ) = n*log(λ) - λ*Σx_i
log_likelihood <- function(lambda, data) {
  n <- length(data)
  n * log(lambda) - lambda * sum(data)
}

# Evaluate over a grid to verify MLE maximises log-likelihood
lambda_seq <- seq(0.3, 0.7, by = 0.01)
ll_values  <- sapply(lambda_seq,
                     function(l) log_likelihood(l, sample_exp))

cat(sprintf("\nLog-likelihood at MLE:       %.4f\n",
            log_likelihood(lambda_mle, sample_exp)))
cat(sprintf("Log-likelihood at true lambda: %.4f\n",
            log_likelihood(true_lambda, sample_exp)))

# Plot log-likelihood
plot(lambda_seq, ll_values, type = "l", lwd = 2,
     xlab = expression(lambda),
     ylab = "Log-Likelihood",
     main = "Log-Likelihood Function — Exponential Distribution")
abline(v = lambda_mle,   col = "red",       lty = 2, lwd = 2)
abline(v = true_lambda,  col = "darkgreen", lty = 3, lwd = 2)
legend("topright",
       legend = c(sprintf("MLE = %.4f", lambda_mle),
                  sprintf("True λ = %.4f", true_lambda)),
       col    = c("red", "darkgreen"),
       lty    = c(2, 3), lwd = 2)
