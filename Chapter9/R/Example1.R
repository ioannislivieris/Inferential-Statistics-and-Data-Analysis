# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 1: Υπολογισμός Δειγματικών Στατιστικών
#   n=10 μισθοί (χιλιάδες ευρώ)

# Create a sample of salaries for 10 employees (in thousands of euros)
salaries <- c(28, 32, 35, 29, 41, 33, 30, 27, 38, 31)

# Calculate the sample size (number of observations)
n <- length(salaries)
cat("Sample size (number of employees):", n, "\n")

# Calculate the sample mean (average salary)
x_bar <- mean(salaries)
cat("Sample mean (x):", round(x_bar, 2), "thousand Euros\n")

# Calculate the sample variance (measure of dispersion)
s_squared <- var(salaries)
cat("Sample variance (s^2):", round(s_squared, 2), "\n")

# Calculate the sample standard deviation (square root of variance)
s <- sd(salaries)
cat("Sample standard deviation (s):", round(s, 2), "thousand Euros\n")

# Calculate the median (middle value when sorted)
median_salary <- median(salaries)
cat("Sample median:", median_salary, "thousand Euros\n")
