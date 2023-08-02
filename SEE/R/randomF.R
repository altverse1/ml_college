library(randomForest)
data('iris')

indices <- sample(1:nrow(iris), 0.7*nrow(iris))
train <- iris[indices, ]
test <- iris[-indices, ]


model <- randomForest(Species ~., data = train)
pred  <- predict(model, newdata=test, type='class')

accuracy = sum(pred == test$Species)/nrow(test)
cat(accuracy)