
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False]*(n+1) # 방문 여부

def bfs(start, k):
    result = []

    q = deque()
    q.append((start, 0)) # 시작지점, 거리 (처음은 0)
    visited[start] = True

    while q:
        node, level = q.popleft()
        if level == k:
            result.append(node)
        for s in graph[node]:
            if visited[s] == False:
                visited[s] = True
                q.append((s, level+1))
    return result

result = bfs(x, k)
if result == []:
    print(-1)
else:
    result.sort()
    for s in result:
        print(s)

# pypy로 제출했음에도 채점 속도가 아주 빠른건 아니다.


## 다른 사람 코드 ##

import sys
from collections import deque

input = sys.stdin.readline

# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
N, M, K, X = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b =  map(int, input().split(' '))
    graph[a].append(b)

distance = [-1] *(N+1)
distance[X] = 0

# BFS 부분
q = deque([X])
while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now]+1
            q.append(next)

# K값이 distance에 있다면 i값출력 없다면 -1 출력
if K in distance:
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
            check = True
else:
    print(-1)










import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

list = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    list[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])

while queue:
    v = queue.popleft()

    for i in list[v]:
        if distance[i] == -1:
            queue.append(i)
            distance[i] = distance[v] + 1

for i in range(len(distance)):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)







import collections
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

routes = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    routes[a].append(b)

visited = [False] * (n + 1)
dist = [0] * (n + 1)

dq = collections.deque()
dq.append([x, 0])
visited[x] = True

while dq:
    tmp, cnt = dq.popleft()
    for i in routes[tmp]:
        if not visited[i]:
            dq.append([i, cnt + 1])
            visited[i] = True
            dist[i] = cnt + 1

tmp = [print(i) for i in range(1, n + 1) if dist[i] == k]
if len(tmp) == 0:
    print(-1)