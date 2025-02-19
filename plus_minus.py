# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# # import arrpy as np
# def min_max():
#     list1 = []
#     list2 = []
#     list3 = []
#     n = int(input("Enter arrber of elements: "))
#     arr = list(map(int, input(f"Enter {n} space-separated integers: ").split()))
#     print(arr)
    
#     print(len(arr))
#     for i in arr:
#         if i > 0:
#             list1.append(i)
#         elif i < 0:
#             list2.append(i)
#         else:
#             list3.append(i)

#     # print(list1,list2,list3)
#     plusMinus1 = len(list1) / len(arr)
#     plusMinus2 = len(list2) / len(arr)
#     plusMinus3 = len(list3) / len(arr)
#     print(f"{float(plusMinus1):.6f}\n{float(plusMinus2):.6f}\n{float(plusMinus3):.6f}")

# min_max()
    

#!/bin/python3

import math
import os
import random
import re
import sys
# import arrpy as np
def min_max():
    list1 = []
    list2 = []
    list3 = []
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    
    print(len(arr))
    for i in arr:
        if i > 0:
            list1.append(i)
        elif i < 0:
            list2.append(i)
        else:
            list3.append(i)

    # print(list1,list2,list3)
    plusMinus1 = len(list1) / len(arr)
    plusMinus2 = len(list2) / len(arr)
    plusMinus3 = len(list3) / len(arr)
    print(f"{plusMinus1:.6f}")
    print(f"{plusMinus2:.6f}")
    print(f"{plusMinus3:.6f}")

min_max()
