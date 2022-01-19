
'''
이 문제는 찾는데 걸리는 시간을 최소화 해야 한다.

같은 수가 적힌 경우가 없다는게 핵심.
'''
#
# import sys
#
# n = int(input())
# arr1 = set(map(int, sys.stdin.readline().split()))
# m = int(input())
# arr2 = list(map(int, sys.stdin.readline().split()))
#
# result = ""
# for i in arr2: 여기서 O(N)
#     if i in arr1: # 여기서 O(N)
#         result += "1 "
#     else:
#         result += "0 "
# print("%s"%(result[:-1]))

# 위 코드는 시간초과.


# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# stand = list(map(int, input().split()))
#
# for idx, i in enumerate(stand):
#     if idx == len(stand)-1:
#         if i in arr: print("1")
#         else:          print("0")
#     else:
#         if i in arr: print("1", end=" ")
#         else:          print("0", end=" ")
# 위 코드도 시간초과다.





