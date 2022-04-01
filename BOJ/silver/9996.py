import sys
input = sys.stdin.readline
#
# n = int(input())
#
# pattern = list(input())[:-1]
#
# for _ in range(n):
#     pattern_idx = 0
#     string = list(input())[:-1]
#
#     for s in string:
#         if s == pattern[pattern_idx]:
#             pattern_idx += 1
#         if pattern_idx < len(pattern) and pattern[pattern_idx] == "*":
#             pattern_idx += 1
#         if pattern_idx == len(pattern):
#             break
#     if pattern_idx == len(pattern):
#         print("DA")
#     else:
#         print("NE")

# 틀림

# n = int(input())
#
# pattern = input()
#
# for _ in range(n):
#     pattern_idx = 0
#     string = list(input())
#     index = 0
#     for idx, s in enumerate(string):
#         if s == pattern[pattern_idx]:
#             pattern_idx += 1
#         elif pattern[pattern_idx] == "*":
#             pattern_idx += 1
#         if pattern_idx == len(pattern):
#             index = idx
#             break
#     if index == len(string)-1:
#         print("DA")
#     else:
#         print("NE")

# 틀림. 맨 끝에가 일치 해야 하는듯
# h*n일 때 habndk 이래도 DA가 나오면 안되는데.


