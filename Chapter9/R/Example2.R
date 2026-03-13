# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 2: Απλή Τυχαία Δειγματοληψία
#   N=500 υπάλληλοι, n=50 δείγμα

set.seed(123)  # Set seed for reproducibility of random results

# Create population: Employee IDs numbered from 1 to 500
population <- 1:500

# Perform simple random sampling without replacement
sample_size <- 50
simple_random_sample <- sample(population, sample_size, replace = FALSE)

# Display the first 10 selected employee IDs
cat("First 10 selected employees:",
    head(simple_random_sample, 10), "\n")

# Alternative approach using the dplyr package for data manipulation
library(dplyr)

# Create a data frame with employee characteristics
employees <- data.frame(
  ID         = 1:500,
  Age        = sample(22:65, 500, replace = TRUE),
  Salary     = rnorm(500, mean = 35000, sd = 8000),
  Department = sample(c("Sales", "IT", "HR", "Finance"),
                      500, replace = TRUE)
)

# Perform simple random sampling using dplyr
srs_sample <- employees %>%
  sample_n(50)

# Calculate and display sample statistics
cat("\nSample mean age:",    round(mean(srs_sample$Age), 1),    "years\n")
cat("Sample mean salary:", round(mean(srs_sample$Salary), 2), "Euros\n")

# Department distribution in sample
cat("\nDepartment distribution in the sample:\n")
print(table(srs_sample$Department))
