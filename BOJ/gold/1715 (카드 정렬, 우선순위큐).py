
# import heapq
#
# n = int(input())
#
# q = []
# for _ in range(n):
#     heapq.heappush(q, int(input()))
#
# tmp1 = 0
# tmp2 = 0
# result = 0
#
# for i in range(len(q)):
#     value = heapq.heappop(q)
#     if i == 0:
#         tmp1 = value
#     elif i >= 1:
#         tmp2 = value
#         result = tmp1+tmp2 # 더한 값을 어떻게 다시 계산할 지 몰라서 변수 2개로 구분하려고 했었음.
#         tmp1 = tmp2
#
# print(result+tmp2)

## 위 코드 틀림

'''
최적의 정답이 되기 위해서는 합친 수까지 포함해 가장 작은 두 수를 더해가는 방식을 써야 한다.
'''

import heapq

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

answer = 0
while len(q) != 1:
    value1 = heapq.heappop(q)
    value2 = heapq.heappop(q)

    answer += value1 + value2

    heapq.heappush(q, value1+value2) # 이게 핵심이다. 더한 값을 다시 넣어준다. (다시 계산해야 하므로)

print(answer)

## 다른 사람 코드 ##

import heapq
import sys

n = int(sys.stdin.readline())
h = [int(input()) for _ in range(n)]
heapq.heapify(h)

sum = 0

while len(h) != 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    t = a + b
    sum += t
    heapq.heappush(h, t)

print(sum)