
'''
BFS로도 해결할 수 있다.

임의의 두 사람이 최소 몇 단계만에 이어질 수 있는가. (최소단계)

친구 관계가 있는 경우 비용 1로 계산할 수 있다.
'''
import sys
input = sys.stdin.readline

INF = 10e9

n, m = map(int, input().split())

distance = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            distance[i][j] = 0
        else:
            distance[i][j] = INF

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1 # 양방향으로 저장.

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > (distance[i][k] + distance[k][j]): # 누군가를 거쳐갔을 때 가장 짧은 거리가 있다면, 
                distance[i][j] = distance[i][k] + distance[k][j] # 짧은 거리로 대체

values = []

for idx, x in enumerate(distance):
    if idx == 0:
        continue
    else:
        values.append((idx, sum(x[1:])))
values.sort(key = lambda x:(x[1], x[0]))
print(values[0][0])



## 다른 사람 코드 ##
import sys
from collections import deque

_ = sys.stdin.readline().strip().split()
N, M = int(_[0]), int(_[1])

graph = []
for _ in range(N + 1):
    graph.append([])

for _ in range(M):
    _l = sys.stdin.readline().strip().split()
    A, B = int(_l[0]), int(_l[1])

    if B not in graph[A]:
        graph[A].append(B)

    if A not in graph[B]:
        graph[B].append(A)

bacon = []
for c in range(1, N + 1):
    dist = [0 if i == c else 9999999 for i in range(N + 1)]

    visited = [False] * (N + 1)
    visited[0] = True
    q = deque()

    current = graph[c]
    level = 1
    while len(current) != 0:
        next = []
        for i in current:
            if visited[i] == False:
                dist[i] = level
                visited[i] = True
                next.extend(graph[i])

        level += 1
        current = next

    bacon.append(sum(dist[1:]))
print(bacon.index(min(bacon)) + 1)








from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split(" "))
graph = [[]for i in range(n+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split(" "))
    if b not in graph[a]:
        graph[a].append(b)
        graph[b].append(a)

def bfs(srt):
    global count
    q = deque([srt])
    visited[srt] = 1
    while q:
        curr = q.popleft()
        for adj in graph[curr]:
            if visited[adj] == 0:
                q.append(adj)
                visited[adj] = visited[curr] + 1
res = 10000
idx = 0
for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs(i)
    if res > sum(visited)-n:
        idx = i
        res = sum(visited)-n
print(idx)









import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = [(start, 0)]
    visited = [0] * (n + 1)
    while q:
        cur, cnt = q.pop(0)
        for x in graph[cur]:
            if not visited[x]:
                visited[x] = cnt + 1
                q.append((x, cnt + 1))

    return sum(visited)


min_value = 1e9
ans = -1
for i in range(1, n + 1):
    sum_value = bfs(i)
    if sum_value < min_value:
        min_value = sum_value
        ans = i

print(ans)