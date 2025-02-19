import numpy as np
import math as np
n = int(input())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = list(map(int,input().split()))
final_arr = list([arr1,arr2,arr3])
# print(final_arr)
for col in range(len(final_arr)):
    for row in range(len(final_arr)):
        # print(final_arr[col][row],end=" ")
        
        diag1 = final_arr[0][0] + final_arr[0][1] + final_arr[0][2]
        diag2 = final_arr[0][2] + final_arr[0][1] + final_arr[0][0]
        diag_sum = diag1 - diag2

print(diag_sum.__abs__())
# print('\n',diag1,'\n',diag2)
