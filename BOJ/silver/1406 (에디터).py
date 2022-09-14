# from collections import deque
# import sys
# input = sys.stdin.readline
#
# string = deque(input())
# m = int(input())
#
# idx = len(string) # 처음에는 글자 맨 끝에 위치
#
# for _ in range(m):
#     vv = input().split()
#     if vv[0] == "L":
#         if idx > 0:
#             idx -= 1
#     elif vv[0] == "D":
#         if idx < len(string): # 맨 끝 위치보다 작은 경우만 idx를 높인다.
#             idx += 1
#     elif vv[0] == "B":
#         if idx != 0:
#             string.remove(string[idx-1])
#             idx -= 1
#     elif vv[0] == "P":
#         string.insert(idx, vv[1])
#         idx += 1
# print("".join(map(str, string)))

# 위 코드 틀림










