'''
각 점마다 최소 거리 table을 구해놓고,
해당 최소 거리에

X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다는 것이 key-point

'''


import sys
import heapq

INF = sys.maxsize

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

print(graph)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a점에서 b까지 가는데 걸리는 C
    graph[b].append((a, c)) # b점에서 a까지 가는데 걸리는 c

def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now]< dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


result = []

for i in range(1, n+1):
    result += dijkstra(i) # 여기서 나온 result는 도착지점으로 가는 거리만을 의미하는 것일텐데.

print(result)
# 오고 가는 데 가장 오래 걸리는 것은 뭘 의미하는 것일까?
