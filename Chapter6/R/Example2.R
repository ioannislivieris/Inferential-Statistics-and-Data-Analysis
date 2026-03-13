# Chapter 6 - Κανονική Κατανομή
# Example 2: Υπολογισμός Κβαντιλίων  X ~ N(50, 10²)

# Parameters
mu <- 50
sigma <- 10

# Quantiles
q25 <- qnorm(0.25, mean = mu, sd = sigma)
q50 <- qnorm(0.50, mean = mu, sd = sigma)
q75 <- qnorm(0.75, mean = mu, sd = sigma)

cat(sprintf("First quartile (Q1): %.2f\n", q25))
cat(sprintf("Median (Q2): %.2f\n", q50))
cat(sprintf("Third quartile (Q3): %.2f\n", q75))
cat(sprintf("Interquartile Range (IQR): %.2f\n", q75 - q25))
