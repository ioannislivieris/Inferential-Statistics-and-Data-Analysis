# Chapter 5 - Other Discrete Distributions
# Example 4: Hypergeometric vs Binomial — Sampling from Finite Population
#   N=100, K=30, n=20

# Parameters
N <- 100   # population size
K <- 30    # successes in population
n <- 20    # sample size
p <- K/N   # probability for binomial approximation

# Values
x <- 0:n

# Calculate probabilities
hypergeom_probs <- dhyper(x, K, N - K, n)
binom_probs     <- dbinom(x, n, p)

# Plot comparison
barplot(rbind(hypergeom_probs, binom_probs),
        beside      = TRUE, names.arg = x,
        col         = c('steelblue', 'coral'),
        xlab        = 'Number of Successes',
        ylab        = 'Probability',
        main        = 'Hypergeometric vs Binomial',
        legend.text = c('Hypergeometric', 'Binomial'),
        args.legend = list(x = 'topright'))

# Maximum absolute difference
max_diff <- max(abs(hypergeom_probs - binom_probs))
cat(sprintf("Maximum difference: %.6f\n", max_diff))
