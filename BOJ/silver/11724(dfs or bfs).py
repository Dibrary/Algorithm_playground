
# 내 생각엔 dfs를 써야 한다고 생각되지만, 질문에는 bfs가 더 많음;;

# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n + 1)]
#
# min_value = 0
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     if u <= min_value:
#         min_value = u
#
# visited = []  # 방문여부 확인 리스트 어케 만들지
#
#
# def bfs(start):
#     # start 지점의 방문여부 어케 알지
#
#     q = []
#     q.append(start)
#     while q:
#         node = pop(q[0])
#         visited[node] = True
#         for k in graph[node]:
#             if visited[k] == False:
#                 q.append(k)
#
#
# print(graph)

# 맨 처음 생각했던 코드.

# import sys
# limit_number = 11000
# sys.setrecursionlimit(limit_number)
#
# n, m = map(int, input().split())
# graphs = [[] for _ in range(n+1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     graphs[u].append(v)
#
# visited = [False for _ in range(n+1)]
#
# def dfs(n):
#     visited[n] = True
#     for w in graphs[n]:
#         if not visited[w]:
#             dfs(w)
#
# cnt = 0
#
# for k in range(1, n + 1):
#     if visited[k] == False:
#         dfs(k)
#         cnt += 1
#
# print(cnt)

# 위 코드는 재귀를 쓰는 방식이다. 시간초과에 걸린다.

# n, m = map(int, input().split())
# graphs = [[] for _ in range(n + 1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     graphs[u].append(v)
#
# from collections import deque
#
# visited = [False for _ in range(n + 1)]
#
#
# def dfs(graph, start_node):
#     need_visit = deque()
#     need_visit.append(start_node)
#     while need_visit:
#         current_node = need_visit.popleft()
#
#         if visited[current_node] == False:
#             visited[current_node] = True
#             for k in graphs[current_node]:
#                 need_visit.append(k) # 여기서 이미 true로 표시한 노드가 들어갈 수도 있다.
#     return visited
#
#
# cnt = 0
#
# for i in range(1, n + 1):
#     if visited[i] == False:
#         dfs(graphs, i)
#         cnt += 1
#
# print(cnt)

# 26%에서 틀림.


# n, m = map(int, input().split())
# graphs = [[] for _ in range(n + 1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     graphs[u].append(v)
#
# from collections import deque
#
# visited = [False for _ in range(n + 1)]
#
#
# def dfs(graph, start_node):
#     need_visit = deque()
#     need_visit.append(start_node)
#     while need_visit:
#         current_node = need_visit.popleft()
#
#         if visited[current_node] == False:
#             visited[current_node] = True
#             for k in graphs[current_node]:
#                 if visited[k] == False:
#                     need_visit.append(k) # 이 부분을 이렇게 바꾸니까 44%에서 틀린다.
#     return visited
#
#
# cnt = 0
#
# for i in range(1, n + 1):
#     if visited[i] == False:
#         dfs(graphs, i)
#         cnt += 1
#
# print(cnt)


n, m = map(int, input().split())
graphs = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u) # 이거 추가하니까 통과됨.

from collections import deque

visited = [False for _ in range(n + 1)]


def dfs(graph, start_node):
    need_visit = deque()
    need_visit.append(start_node)
    while need_visit:
        current_node = need_visit.popleft()

        if visited[current_node] == False:
            visited[current_node] = True
            for k in graphs[current_node]:
                if visited[k] == False: # 이 조건문 없이도 통과 됨. (문제는 위의 node 추가를 초반에 잘못한 것)
                    need_visit.append(k)
    return visited


cnt = 0

for i in range(1, n + 1):
    if visited[i] == False:
        dfs(graphs, i)
        cnt += 1

print(cnt)



