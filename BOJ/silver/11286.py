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