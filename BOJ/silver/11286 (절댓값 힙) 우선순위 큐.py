#
# from queue import PriorityQueue
#
# n = int(input())
# q = PriorityQueue()
#
# for _ in range(n):
#     value = int(input())
#     if value == 0:
#         if q.qsize() == 0:
#             print(0)
#         else:
#             print(q.get())
#     else:
#         q.put(value)

# 근데 이렇게 하면 절대값에 따른 출력이 불가능

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# table = []
#
# for _ in range(n):
#     value = int(input())
#     if value == 0:
#         if len(table) == 0:
#             print(0)
#         else:
#             table.sort(key=lambda x:(x[0], x[1]))
#             print(table.pop(0)[1])
#     else:
#         table.append((abs(value), value))

# 이렇게 하면 시간초과 됨.


from queue import PriorityQueue
import sys
input = sys.stdin.readline


q= PriorityQueue()
n = int(input())
for _ in range(n):
    value = int(input())
    if value == 0:
        if q.qsize() == 0:
            print(0)
        else:
            print(q.get()[1])
    else:
        q.put((abs(value), value))


## 다른 사람 코드 ##

from heapq import heappush, heappop
import sys

input = lambda: sys.stdin.readline().rstrip()

hq = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heappop(hq)[1] if len(hq) else 0)
    else:
        heappush(hq, (abs(x), x))






import sys
import heapq

min_heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    comm = int(sys.stdin.readline())
    if comm != 0:
        heapq.heappush(min_heap, (abs(comm), comm))
    else:
        if len(min_heap):
            print(heapq.heappop(min_heap)[1])
        else:
            print(0)
