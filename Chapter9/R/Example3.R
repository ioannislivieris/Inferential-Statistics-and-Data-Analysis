# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 3: Στρωματοποιημένη Δειγματοληψία
#   N=1000 υπάλληλοι, 4 τμήματα, n=100

library(dplyr)
set.seed(456)

# Create a population with strata defined by departments
population <- data.frame(
  ID           = 1:1000,
  Department   = sample(c("Sales", "IT", "HR", "Finance"),
                        1000, replace = TRUE,
                        prob = c(0.4, 0.3, 0.2, 0.1)),
  Satisfaction = rnorm(1000, mean = 7, sd = 1.5)
)

# Display the department distribution in the population
cat("Department distribution in population:\n")
print(table(population$Department))

# Perform proportional stratified sampling
sample_size <- 100

stratified_sample <- population %>%
  group_by(Department) %>%
  sample_frac(sample_size / nrow(population)) %>%
  ungroup()

# Display sample size per department (should be proportional)
cat("\nSample size per department:\n")
print(table(stratified_sample$Department))

# Perform simple random sampling for comparison
srs_sample <- population %>%
  sample_n(sample_size)

# Compare results from both sampling methods
cat("\n--- Comparison of Sampling Methods ---\n")
cat("Stratified sampling - Mean satisfaction score:",
    round(mean(stratified_sample$Satisfaction), 2), "\n")
cat("Simple random sampling - Mean satisfaction score:",
    round(mean(srs_sample$Satisfaction), 2), "\n")
cat("Population - True mean satisfaction score:",
    round(mean(population$Satisfaction), 2), "\n")
