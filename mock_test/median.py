import numpy as np

n = int(input())

arr = list(map(int,input().split()))

arr.sort()

find_median = sum(arr) / len(arr)
print(int(find_median))