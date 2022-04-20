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
#         if towers[j] >= std: # = 넣으니 틀렸다는 문구에서, '시간초과'로 변경됨.
#             break
#         else:
#             cnt += 1
# print(cnt)

# 인터넷으로 확인 해 보니 스택을 이용해야 한다고 함.


import sys

n = int(input())
towers = [int(input()) for _ in range(n)] # 이렇게 한 번에 받을 수 있다.

stack, res = [], 0

for i in range(n): # 맨 앞에서부터 확인해 나가되
    while stack != [] and stack[-1] <= towers[i]: # 스택이 비어있거나, i번째 towers보다 작으면
        stack.pop() # 스택에서 해당 건물(층)을 제거한다
    stack.append(towers[i]) # i번째 타워 스택에 추가
    res += len(stack)-1 # 스택 길이의 -1개가 곧 해당 빌딩을 바라볼 수 있는 관리자의 수다.
print(res)




