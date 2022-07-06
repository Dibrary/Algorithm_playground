
'''
갈 수 있는지를 고려해 보고, 최단거리가 있다면 경로가 있는 것이므로
해당 위치의 값이 숫자일 때 1로만 바꾸면 결과가 나올 듯.

굳이 (0은 없고)1부터 시작한다는 말이 없으므로 그냥 n까지 배열 생성해도 됨.

'''

import sys

n = int(input())
INF = sys.maxsize
graph = [[INF]*(n) for _ in range(n)]

for s in range(n):
    arr = list(map(int, input().split()))
    for idx, k in enumerate(arr):
        if k == 1:
            graph[s][idx] = 1


for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = []
for idx, k in enumerate(graph):
    result.append([])
    for s in k:
        if s == sys.maxsize:
            result[idx].append(0)
        else:
            result[idx].append(1)

for m in result:
    print(" ".join(map(str, m)))


## 여기서 중요한 것은, 플로이드 워셜이 최단거리만을 구하는 데 쓰이는 게 아니라
## 연결되어 있는지 판단하는 용도로도 쓰였다는 점.



### 다른 사람 코드 ###

from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j]:
            graph[i].append(j)

for i in range(n):
    q = deque()
    visited = [False for _ in range(n)]
    for e in graph[i]:
        q.append(e)
        visited[e] = True
    while q:
        x = q.popleft()
        for g in graph[x]:
            if not visited[g]:
                q.append(g)
                visited[g] = True
                graph[i].append(g)
for i in range(n):
    graph[i] = set(graph[i])
    temp = []
    for j in range(n):
        if j not in graph[i]:
            temp.append(0)
        else:
            temp.append(1)
    print(' '.join([str(e) for e in temp]))






from collections import deque

def bfs(data, n, start, end):
    visit = [0] * (n + 1)
    que = deque()
    que.append(start)
    result = '0'
    while que:
        temp = que.popleft()
        for i in data[temp]:
            if visit[i] == 0:
                que.append(i)
                visit[i] = 1
            if i == end:
                result = '1'
                return result
    return result


n = int(input())
data = [[] for _ in range(n + 1)]
for i in range(n):
    a = list(map(int, input().split(' ')))
    for j in range(n):
        if a[j] == 1:
            data[i + 1].append(j + 1)
check = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        temp = bfs(data, n, i + 1, j + 1)
        check[i][j] = temp
for i in range(n):
    print(' '.join(check[i]))