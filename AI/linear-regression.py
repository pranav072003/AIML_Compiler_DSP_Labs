import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import math

diabetes = datasets.load_diabetes()

print(diabetes.keys())

diabetes_x = diabetes.data[: , np.newaxis, 2]

diabetes_x_train = diabetes_x[:-30]
diabetes_x_test = diabetes_x[-30:]

diabetes_y_train = diabetes.target[:-30, np.newaxis]
diabetes_y_test = diabetes.target[-30:, np.newaxis]

xy = diabetes_x_train * diabetes_y_train
sum_xy = sum(xy)
sum_x = sum(diabetes_x_train)
sum_y = sum(diabetes_y_train)
n = len(diabetes_x_train)
x2 = diabetes_x_train**2
y2 = diabetes_y_train**2
sum_x2 = sum(x2)
sum_y2 = sum(y2)
corr_r = (n*sum_xy - sum_x*sum_y)/math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))  #calculating correlation for regression line
sigma_x = math.sqrt((np.mean(diabetes_x_train**2) - np.mean(diabetes_x_train)**2)/(n-1)) #sd for a sample 
sigma_y = math.sqrt((np.mean(diabetes_y_train**2) - np.mean(diabetes_y_train)**2)/(n-1)) #sd for a sample
byx = corr_r * sigma_y / sigma_x;
ybar = np.mean(diabetes_y_train)

def model(x,ybar,byx):
  xbar = np.mean(x)
  t = byx * (x - xbar)
  y = t + ybar
  return y

diabetes_y_predicted = model(diabetes_x_test,ybar,byx) #using regression model

plt.scatter(diabetes_x_test, diabetes_y_test) #plotting the testing data
plt.plot(diabetes_x_test, diabetes_y_predicted) 
