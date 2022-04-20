#
# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# towers = []
# for _ in range(n):
#     towers.append(int(input()))
#
# cnt = 0
#
# for i in range(0, len(towers)-1):
#     std = towers[i]
#     for j in range(i+1, len(towers)):
#         if towers[j] > std:
#             break
#         else:
#             cnt += 1
# print(cnt)

# 틀렸다고 나온다.
import sys
input = sys.stdin.readline

n = int(input())

towers = []
for _ in range(n):
    towers.append(int(input()))

cnt = 0

for i in range(0, len(towers)-1):
    std = towers[i]
    for j in range(i+1, len(towers)):
        if towers[j] >= std: # = 넣으니 틀렸다는 문구에서, '시간초과'로 변경됨.
            break
        else:
            cnt += 1
print(cnt)



