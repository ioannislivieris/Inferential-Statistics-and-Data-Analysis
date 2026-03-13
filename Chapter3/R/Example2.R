# Chapter 3 - Binomial Distribution
# Example 2: Quality Control - Acceptance Sampling  (n=100, c=3)

# Parameters
n <- 100
c <- 3  # Acceptance number

# i. Probability of acceptance with p = 0.02
p1              <- 0.02
prob_accept_p1  <- pbinom(c, n, p1)
cat(sprintf("i. P(Accept | p=0.02) = %.4f\n", prob_accept_p1))

# ii. Probability of acceptance with p = 0.05
p2              <- 0.05
prob_accept_p2  <- pbinom(c, n, p2)
cat(sprintf("ii. P(Accept | p=0.05) = %.4f\n", prob_accept_p2))

# iii. Defect rate for 50% acceptance probability
# Solve: P(X <= 3) = 0.50
equation <- function(p) pbinom(c, n, p) - 0.50

p_50 <- uniroot(equation, c(0.001, 0.1))$root
cat(sprintf("iii. Defect rate for 50%% acceptance: %.4f\n", p_50))

# Verification
cat(sprintf("Verification: P(Accept | p=%.4f) = %.4f\n",
            p_50, pbinom(c, n, p_50)))
