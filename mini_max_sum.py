
arr = list(map(int,input().split()))
# print(arr)
arr.sort()

minimum_sum = arr[:-1]
maximum_sum = arr[1:]
print(sum(minimum_sum),sum(maximum_sum))