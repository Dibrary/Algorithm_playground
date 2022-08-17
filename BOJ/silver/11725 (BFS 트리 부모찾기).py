
'''
루트 없는 트리가 주어진다. 루트를 1이라 할 때, 각 노드의 부모를 구하자.

재귀를 써야 할 것 같다.
들어갔다가 나오면서 현재 노드의 부모 노드를 기록해놔야 할 듯.
'''
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        for k in graph[node]:
            if result[k] == 0:
                result[k] = node # k라는 노드가 나오게 된 node가 parent이다.
                q.append(k)

bfs(1) # 루트노드는 1이라고 했으므로,

for idx, s in enumerate(result): # 2번째부터 출력하라고 했으므로
    if idx >= 2:
        print(s)




## 다른 사람 코드 ##

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
#
# n = int(input())
#
# tree = [[] for _ in range(n+1)]
# parents = [0 for _ in range(n+1)]
#
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)
#
# def dfs(start, tree, parents):
#     for i in tree[start]:
#         if parents[i] == 0:
#             parents[i] = start
#             dfs(i, tree, parents)
#
# dfs(1, tree, parents)
#
# for i in range(2, n+1):
#     print(parents[i])
#
#
#
#
#
# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
#
# N = int(input())
# visited = [False] * (N + 1)
# answer = [0] * (N + 1)
# E = [[] for _ in range(N + 1)]
# for i in range(N - 1):
#     S, D = map(int, input().split())
#     E[S].append(D)
#     E[D].append(S)
#
#
# def dfs(E, v, visited):
#     visited[v] = True
#     for i in E[v]:
#         if not visited[i]:
#             answer[i] = v
#             dfs(E, i, visited)
#
#
# dfs(E, 1, visited)
#
# for i in range(2, N + 1):
#     print(answer[i])
#
#
#
#
#
# #DFS 스택 사용
# from collections import deque
# import sys
# input=sys.stdin.readline
#
#
# N=int(input())
# visited=[False]*(N+1)
# answer=[0]*(N+1)
# E=[[] for _ in range(N+1)]
# for i in range(N-1):
#     S,D=map(int,input().split())
#     E[S].append(D)
#     E[D].append(S)
#
# #DFS with Stack
# def dfs(E,v,visited):
#     visited[v]=True
#     stack=deque([v])
#     while stack:
#         x=stack.pop()
#         for i in E[x]:
#             if not visited[i]:
#                 stack.append(i)
#                 visited[i]=True
#                 answer[i]=x
# dfs(E,1,visited)
# for i in range(2,N+1):
#         print(answer[i])
