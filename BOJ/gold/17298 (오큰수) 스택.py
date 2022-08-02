
'''
스택에 새로 들어오는 수가 TOP에 존재하는 수보다 크면 그 수는 오큰수가 된다.

오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력해야 한다.

n은 100만까지 주어질 수 있으므로,
일일이 반복문으로 확인하면 100만 factorial 의 경우 숫자가 나올 수 있음...
'''

# n = int(input())
# arr = list(map(int, input().split()))
# from collections import deque
#
# result = []
#
# for idx, i in enumerate(arr):
#     if len(tmp) == 0:
#         tmp.append(idx)
#         if i == max(arr):
#             result.append(-1)
#     else:
#         cnt = 0
#         while arr[tmp[-1]] < i:
#             tmp.pop()
#             cnt += 1
#             if len(tmp) == 0:
#                 break
#         tmp.append(idx)
#
#         for k in range(cnt):
#             result.append(arr[tmp[-1]])
# print(" ".join(map(str, result + [-1])))

# 이렇게 하면 예제들은 맞는데...


# n = int(input())
# ans = [0 for _ in range(n)]
#
# A = list(map(int, input().split()))
#
# stack = deque()
# stack.append(A[0]) # 여기를 잘못 설정함.
#
# for i in range(n):
#     while len(stack) != 0 and A[stack[-1]] < A[i]:
#         ans[stack.pop()] = A[i]
#     stack.append(i)
#
# while len(stack) != 0:
#     ans[stack.pop()] = -1
#
# print(ans)

# 위 코드는 예제 1번만 맞는다. 2는 list index out of range 나온다.
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
ans = [0 for _ in range(n)]

A = list(map(int, input().split()))

stack = deque()
stack.append(0)  # 시작 인덱스를 넣음.

for i in range(1, n):
    while len(stack) != 0 and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

while len(stack) != 0:
    ans[stack.pop()] = -1

print(" ".join(map(str, ans)))

# 이렇게 수정하면 예제는 모두 맞는다.



## 다른 사람 코드 ##
from _collections import deque
import sys

sequence_size = int(sys.stdin.readline())
stack= []
sequence_deque = deque()
sequence_deque = list(map(int, sys.stdin.readline().split(" ")))

for count_1 in range(0,len(sequence_deque)):
    if count_1 != 0:
        if sequence_deque[count_1 - 1] < sequence_deque[count_1]:
            while stack:
                count_2 = stack[-1]
                if sequence_deque[count_1] > sequence_deque[count_2]:
                    sequence_deque[count_2] = sequence_deque[count_1]
                    stack.pop()
                else:
                    break
    stack.append(count_1)

for count_1 in stack:
    sequence_deque[count_1] = -1

print(*sequence_deque)










N = int(input())
data = list(map(int, input().split(" ")))
result = [-1] * N

stack = [(data[0], 0)]
for i in range(1, N):

    while len(stack) != 0 and data[i] > stack[-1][0]:
        result[stack[-1][1]] = data[i]
        del stack[-1]

    stack.insert(len(stack), (data[i], i))

print(" ".join(str(x) for x in result))










import sys
ttl = int(input())
stg = list(map(int,sys.stdin.readline().split()))
bck = []
rst = [-1]*ttl
for i in range(ttl):
    while len(bck)>0 and stg[bck[-1]]<stg[i]:
        rst[bck.pop()] = stg[i]
    bck.append(i)
print(*rst)
