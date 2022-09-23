import sys
input = sys.stdin.readline
from collections import deque

# n, k = map(int, input().split())
# value = int(input())
#
# stack = []
# result = ""
#
# for x in value:
#     if len(stack) == 0:
#         stack.append(x)
#     else:
#         if k != 0:
#             if stack[-1] > x:
#                 result += "".join(map(str, stack))
#                 k -= len(stack)
#                 stack = [x] # 스택 초기화
#             elif stack[-1] < x:
#                 while len(stack) > 0 and stack[-1] < x and k != 0:
#                     stack.pop()
#                     k -= 1
#                 stack.append(x)
#         else:
#             stack.append(x)

## 결과가 맞는것도 있고 다른것도 있다.

n, k = map(int, input().split())
value = list(input())

stack = []

for x in value:
    if len(stack) == 0:
        stack.append(x)
    else:
        while len(stack) > 0 and stack[-1] < x and k != 0:
            stack.pop()
            k -= 1
        stack.append(x)
print(''.join(map(str, stack)))

# 75%에서 틀린다.




## 다른 사람 코드 ##

import sys

N, K = [int(x) for x in sys.stdin.readline().rstrip().split()]

num = list(sys.stdin.readline().rstrip())
stack = []
delete_count = K

for i in range(N):
    while delete_count and stack:
        if stack[-1] < num[i]:
            stack.pop()
            delete_count -= 1
        else:
            break
    stack.append(num[i])

print(''.join(stack[:N-K]))


## 책 풀이 ##

n, k = map(int, input().split())
number = list(input())

answer = []
cnt = k

for num in number:
    while answer and cnt > 0 and answer[-1] < num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

print(''.join(answer[:n-k]))








