# Chapter 9 - Μέθοδοι Δειγματοληψίας και Βασικές Έννοιες
# Example 4: Δειγματοληψία Κατά Συστάδες
#   50 καταστήματα, 100 πελάτες/κατάστημα, επιλογή 5 καταστημάτων

library(dplyr)
set.seed(321)

# Create a population organized in clusters (e.g., retail stores)
stores               <- 50   # Total number of stores (clusters)
customers_per_store  <- 100  # Customers per store

population <- data.frame(
  StoreID    = rep(1:stores, each = customers_per_store),
  CustomerID = 1:(stores * customers_per_store),
  Spending   = rnorm(stores * customers_per_store, mean = 100, sd = 30)
)

cat("Total population size:", nrow(population), "customers\n")
cat("Number of clusters (stores):", stores, "\n")

# Perform cluster sampling: Randomly select 5 stores
num_clusters    <- 5
selected_stores <- sample(1:stores, num_clusters, replace = FALSE)
cat("Selected store IDs:", selected_stores, "\n")

# Include all customers from selected stores in the sample
cluster_sample <- population %>%
  filter(StoreID %in% selected_stores)

cat("\nTotal sample size:", nrow(cluster_sample), "customers\n")
cat("Sample mean spending:",
    round(mean(cluster_sample$Spending), 2), "Euros\n")
cat("Population mean spending (true parameter):",
    round(mean(population$Spending), 2), "Euros\n")

# Perform simple random sampling of same size for comparison
srs_sample <- population %>%
  sample_n(nrow(cluster_sample))

cat("\nSimple random sampling - Mean spending:",
    round(mean(srs_sample$Spending), 2), "Euros\n")

# Create boxplot visualization for selected stores
boxplot(Spending ~ StoreID,
        data  = population[population$StoreID %in% selected_stores, ],
        main  = "Customer Spending Distribution by Selected Store",
        xlab  = "Store ID",
        ylab  = "Spending (Euros)",
        col   = "lightblue")
