import pandas as pd
from math import sqrt

df = pd.read_excel("linear_reg_tut1.xls")       # Read the dataset
print(df.describe())

###### Step 1: Calculate the mean, variance and co-variance
def mean(values):
    return sum(values)/float(len(values))

def variance(values, meanVal):
    return sum((values - meanVal)**2)

def covariance(x,x_mean,y,y_mean):
    return sum((x-x_mean)*(y-y_mean))

#x_mean, y_mean = mean(df["Horsepower"]), mean(df["Price"])
#x_var = variance(df["Horsepower"], x_mean)
#xy_covar = covariance(df["Horsepower"], x_mean ,df["Price"], y_mean)


###### Step 2: Find the coefficients
def cal_coefficient(X, Y):
    x_mean, y_mean = mean(X), mean(Y)
    x_var = variance(X, x_mean)
    xy_covar = covariance(X, x_mean ,Y, y_mean)

    m = xy_covar/x_var
    c = y_mean - m * x_mean
    return m,c

#slope, y_intercept = cal_coefficient(df["Horsepower"], df["Price"])

###### Step 3: Make Prediction
def predict_y(train_dataset, test_dataset):        # Predict Using Linear Regression
    prediction = list()
    slope, y_intercept = cal_coefficient(train_dataset["Horsepower"], train_dataset["Price"])
    prediction =  [round((slope * x + y_intercept),3)  for x in test_dataset["Horsepower"]]

    return prediction

prediction = predict_y( df[:-100], df[-100:])

###### Step 4: Calculate Error
def rms(calculated_y, expected_y):              # Root Mean Square Error
    mean_error = sum((calculated_y - expected_y)**2)
    return round(sqrt(mean_error),3)

print("Error = ",rms(prediction, df["Price"][-100:]))

###### Step 5: Display Graph
from matplotlib import pyplot
pyplot.scatter(df[:-100]["Horsepower"], df[:-100]["Price"],color='red',label='expected')
pyplot.plot(df[-100:]["Horsepower"],prediction,color='black',label = 'predicted')
pyplot.legend()
pyplot.show()
