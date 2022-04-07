
# n, m = map(int, input().split())
#
# first_count = [] # 최대 n*10000 개 들어갈 수 있음..
#
# for s in range(n):
#     left_x, left_y, right_x, right_y = map(int, input().split())
#
#     for i in range(left_x, right_x+1):
#         for j in range(left_y, right_y+1):
#             first_count.append((i, j))
#
# shading_count = set(first_count)
#
# result = 0
# for i in shading_count:
#     if first_count.count(i) > m:
#         result += 1
#
# print(result)

# 너무 느리게 채점된다.. 85% 즘 에서 시간초과 걸림

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

first_count = dict() # 최대 n*10000 개 들어갈 수 있음..

for s in range(n):
    left_x, left_y, right_x, right_y = map(int, input().split())

    for i in range(left_x, right_x+1):
        for j in range(left_y, right_y+1):
            if (i,j) in first_count: first_count[(i,j)] += 1
            else:                    first_count[(i,j)] = 1

result = 0
for k in first_count:
    if first_count[k] > m:
        result += 1

print(result)

# 이렇게 바꾸니 매우 채점 속도 빨라짐.

