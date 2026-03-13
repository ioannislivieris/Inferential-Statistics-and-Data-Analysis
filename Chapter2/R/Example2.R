# Chapter 2 - Sampling Methods and Basic Concepts
# Example 2: Bayes' Theorem Simulation (Monte Carlo)

# Set seed for reproducibility
set.seed(42)

# Simulation parameters
n_simulations <- 100000

# Factory probabilities
factory_probs <- c(0.50, 0.30, 0.20)
factory_names <- c("A", "B", "C")

# Defect probabilities per factory
defect_probs <- c(0.02, 0.03, 0.04)

# Simulate factory selection
factories <- sample(factory_names, n_simulations,
                    replace = TRUE, prob = factory_probs)

# Simulate defects
defects <- numeric(n_simulations)
for (i in 1:n_simulations) {
  factory_idx <- which(factory_names == factories[i])
  defects[i]  <- rbinom(1, 1, defect_probs[factory_idx])
}

# Calculate probabilities
total_defective <- sum(defects)
p_defective     <- total_defective / n_simulations

cat(sprintf("P(Defective) simulation:   %.4f\n", p_defective))
cat(sprintf("P(Defective) theoretical:  %.4f\n\n",
            sum(factory_probs * defect_probs)))

# Bayes' Theorem: P(Factory C | Defective)
defective_from_c    <- sum(defects == 1 & factories == "C")
p_c_given_defective <- defective_from_c / total_defective

cat(sprintf("P(Factory C | Defective) simulation:  %.4f\n", p_c_given_defective))
cat(sprintf("P(Factory C | Defective) theoretical: %.4f\n",
            (0.20 * 0.04) / 0.027))

# Visualization
defective_counts <- table(factories[defects == 1])
barplot(defective_counts / sum(defective_counts),
        col  = 'coral',
        main = 'Distribution of Defectives by Factory',
        ylab = 'Proportion', xlab = 'Factory')
