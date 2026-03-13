# Chapter 1 - Introduction to Inferential Statistics
# Example 1: Basic Operations & Data Manipulation

# ── Basic Arithmetic ──────────────────────────────────────────────────────────
2 + 3
10 / 2
2^3

# Creating variables
x <- 5
y <- 10
z <- x + y

# Creating vectors
numbers <- c(1, 2, 3, 4, 5)
names <- c("Alice", "Bob", "Charlie")

# Basic statistics
mean(numbers)      # Mean
median(numbers)    # Median
sd(numbers)        # Standard deviation
var(numbers)       # Variance

# ── Data Frame Creation & Manipulation ───────────────────────────────────────
students <- data.frame(
  Name  = c("Alice", "Bob", "Charlie", "David"),
  Age   = c(20, 22, 21, 23),
  Grade = c(85, 90, 78, 92)
)

# Viewing the data
print(students)
head(students)
summary(students)

# Accessing columns
students$Name
students$Grade

# Basic statistics by group
mean(students$Grade)
max(students$Age)

# ── Basic Visualization ───────────────────────────────────────────────────────
data <- c(23, 25, 28, 30, 32, 28, 26, 24, 27, 29)

# Histogram
hist(data,
     main   = "Distribution of Data",
     xlab   = "Values",
     col    = "lightblue",
     border = "black")

# Box plot
boxplot(data, main = "Box Plot of Data", ylab = "Values", col = "green")

# Line plot with ggplot2
library(ggplot2)

df <- data.frame(x = 1:10, y = data)

ggplot(df, aes(x = x, y = y)) +
  geom_line(color = "blue", size = 1) +
  geom_point(color = "red", size = 3) +
  labs(title = "Time Series Plot", x = "Time", y = "Value") +
  theme_minimal()
