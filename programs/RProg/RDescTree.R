library(rpart)

data(iris)

set.seed(123)
train_indices <- sample(1:nrow(iris),0.7*nrow(iris))
train_data <- iris[train_indices, ]
test_data <- iris[-train_indices, ] #Minus indicates exclude

tree_model <- rpart(Species ~ ., data = train_data) # ~ . says rest all will act as features for training model to target species

predicted_species <- predict(tree_model, newdata = test_data, type = "class") #type = "class" indicates it is a classification

accuracy <- sum(predicted_species==test_data$Species)/nrow(test_data)
cat("Accuracy: ", accuracy)