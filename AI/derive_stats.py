import numpy as np
import math

print('Hello enter some values:-\n')
list_of_values = list(map(int, input().split()))

def calculate_stats(arr):
  l = []
  a=0
  b=len(arr)
  for i in range(len(arr)):
    a+=arr[i]
  mean =  a/b
  l.append(mean)
  if b%2==0:
    median = (arr[b/2-1] + arr[b/2]) / 2
  else:
    median = arr[b//2]
  l.append(median)
  c=0
  for i in range(len(arr)):
    c+=(arr[i]**2)
  sd = math.sqrt(c/b - mean**2)
  l.append(sd)
  non_rep = list(set(arr))
  count_dict = {}
  for i in non_rep:
    count_dict[i] = arr.count(i)
  values = list(count_dict.values())
  freq_max = max(values)
  keys = list(count_dict.keys())
  keys = np.array(keys)
  mode = keys[np.array(values)==freq_max]
  l.append(mode)
  return l

stats = calculate_stats(list_of_values)

print('Results:-')
print('1) Mean: ',stats[0])
print('2) Median: ',stats[1])
print('3) Mode: ',stats[3])
print('4) Standard Deviation: ',stats[2])