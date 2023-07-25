#install.packages("ggplot2")

library(ggplot2)

#Sample dataset
sales <- c(1000,12000,8000,15000)
expenses <- c(4000,3000,5000,6000)
quarters <- c("Q1","Q2","Q3","Q4")

#Creating dataframe
business_data <- data.frame(Quarter = quarters, Sales = sales, Expenses = expenses)


#Prints summary we can also use business_data.head
print(summary(business_data))


#Data Visualization
ggplot(business_data, aes(x=Quarter))+#aes = asthetic, + is concatination
  geom_bar(aes(y=Sales, fill = "sales"),stat = "identity")+
  geom_bar(aes(y=-Expenses, fill="Expenses"),stat = "identity")+
  labs(title = "sales and expenses by quarter",
       y = "Amount",
       fill = "category")+
    theme_minimal()