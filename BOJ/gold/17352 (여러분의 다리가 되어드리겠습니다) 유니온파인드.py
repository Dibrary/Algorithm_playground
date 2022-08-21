
'''
check 필요가 없을듯. 반드시 parent에는 2가지 숫자 만 나온다.

'''

import sys
sys.setrecursionlimit(10**5)

# n = int(input())
# if n == 2: print("1 2")
# else:
#     parent = [x for x in range(n+1)]
#     # check = [False for x in range(n+1)]
#
#     def find(a):
#         if a == parent[a]:
#             return a
#         p = find(parent[a])
#         parent[a] = p
#         return parent[a]
#
#     def union(a, b):
#         a = find(a)
#         b = find(b)
#         if a == b:
#             return
#         if a > b:
#             parent[a] = b
#         else:
#             parent[b] = a
#
#     for _ in range(n-2):
#         a, b = map(int, input().split())
#         union(a, b)
#         # check[a], check[b] = True, True
#
#     check = parent[1]
#     idx = 1
#     for k in range(1, len(parent)): # 1번째 것을 비교 대상으로 하면서 range를 1부터 시작하는 것 잘못됨.
#         if parent[k] != check:
#             print(f"{idx} {k}")
#             break

# 위 코드 4%에서 틀림.

n = int(input())
if n == 2: print("1 2")
else:
    parent = [x for x in range(n+1)]

    def find(a):
        if a == parent[a]:
            return a
        parent[a] = find(parent[a])
        return parent[a]


    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    for _ in range(n-2):
        a, b = map(int, input().split())
        union(a, b)

    pivot = find(1)
    for i in range(2, n+1):
        if pivot != find(i): # find(i)는 곧 i의 parent값이 된다. 근데 신기한게 parent[i]로 넣으면 틀림.
            print(pivot, i)
            exit()



## 다른 사람 코드 ##
from collections import deque
from sys import stdin

num = int(stdin.readline().strip())
if num == 2:
    print(1, 2)
    exit(0)

visited = [0] * (num + 1)
visited[0] = 5
graph = dict()

Q = deque()

for i in range(num - 2):
    a, b = map(int, stdin.readline().strip().split())
    if len(Q) == 0:
        Q.append(a)

    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

while Q:
    node = Q.pop()
    if visited[node] == 0:
        Q.extend(graph[node])
        visited[node] = 1

print(visited.index(1), visited.index(0))









from functools import reduce
import sys
input = sys.stdin.readline
N = int(input())
nodes = [i for i in range(N+1)]

def find(x):
    while x != nodes[x]:
        nodes[x] = nodes[nodes[x]]
        x = nodes[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x <= y:
        nodes[y] = x
    else:
        nodes[x] = y

for _ in range(N-2):
    x, y = map(int, input().split(" "))
    union(x, y)

root = find(1)
for curr in range(1, N+1):
    next = find(curr)
    if root != next:
        print(root, next)
        break



