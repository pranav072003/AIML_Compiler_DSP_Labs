import numpy as np
from scipy import stats

print('Hello enter some values:-\n')
list_of_values = list(map(int, input().split()))

arr = np.array(list_of_values)

mean = np.mean(arr) #computing sample mean
median = np.median(arr) #computing sample median
mode = stats.mode(arr) #computing sample mode
arr1 = arr**2 
sd = (np.mean(arr1) - mean*2)/(arr.size - 1) #computing sd for a sample

print('Results:-')
print('1) Mean: ',mean)
print('2) Median: ',median)
print('3) Mode: ',mode[0])
print('4) Standard Deviation: ',sd)