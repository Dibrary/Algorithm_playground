
'''
음수사이클 유무를 확인하려면 맨 마지막에 모든 엣지를 한 번씩 다시 사용해 업데이트 되는 노드가 있는지 확인해야 한다.
음수사이클이 있다면, 최단거리를 찾을 수 없는 그래프라는 의미다.

음수사이클 판별하는 문제가 더 빈번하게 출제된다.

최단거리를 구하는데, 엣지가 음수가 가능할 때 벨만-포드 알고리즘을 사용하면 된다.
'''








## 다른 사람 코드 ##
import sys
import collections

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 수, 간선 수 입력 받기
edges = [] # 모든 간선에 대한 정보를 담는 리스트 생성
dist = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 그래프 생성
for _ in range(m):
    u, v, w = map(int, input().split()) # 노드, 인접 노드, 가중치
    edges.append((u, v, w))

# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0 # 시작 노드에 대해서 거리를 0으로 초기화

    for i in range(n): # 정점 수만큼 반복
        for j in range(m): # 매 반복 마다 모든 간선 확인

            node = edges[j][0] # 현재 노드 받아오기
            next_node = edges[j][1] # 다음 노드 받아오기
            cost = edges[j][2] # 가중치 받아오기

            # 현재 간선을 거려서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재

                if i == n-1: # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle: # True 나오면 음수순환이 있는 것.
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        if dist[i] == INF: # 도달할 수 없는 경우 -1 출력
            print('-1')
        else: # 도달할 수 있는 겨우 거리를 출력
            print(dist[i])








import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m = map(int, input().split())
costs = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a].append((b, c))
answer = [sys.maxsize] * (n+1)
answer[1] = 0

dq = deque([1])
cyc = [0] * (n+1)
inq = [False] * (n+1)
inq[1] = True
while dq:
    now = dq.popleft()
    inq[now] = False
    for v, w in costs[now]:
        if answer[v] > answer[now] + w:
            answer[v] = answer[now] + w
            if not inq[v]:
                dq.append(v)
                inq[v] = True
                cyc[v] += 1
            if cyc[v] == n:
                print(-1)
                exit(0)

for i in range(2, n+1):
    print(-1) if answer[i] == sys.maxsize else print(answer[i])








import sys
from collections import deque

readline = sys.stdin.readline

INF = 10000 * 500 + 1


def SPFA():
    dist = [INF] * n
    cycle = [0] * n
    on = [False] * n
    q = deque()

    q.append(0)
    dist[0] = 0
    on[0] = True
    while q:
        u = q.popleft()
        on[u] = False

        for v, _w in graph[u]:
            if dist[v] > dist[u] + _w:
                dist[v] = dist[u] + _w
                if not on[v]:
                    q.append(v)
                    on[v] = True
                    cycle[v] += 1

                    if cycle[v] == n:
                        print(-1)
                        return
    all_negative = True
    for i in range(1, n):
        if dist[i] >= 0:
            all_negative = False
    if all_negative:
        print(-1)
        return
    for i in range(1, n):
        print(dist[i] if dist[i] != INF else -1)


if __name__ == "__main__":
    n, m = map(int, readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, readline().split())
        graph[u - 1].append([v - 1, w])

    SPFA()










from sys import stdin
from math import inf
INF = inf

def bellman_ford(graph, start_node):
    distances = {}
    for node in graph:
        distances[node] = INF
    distances[start_node] = 0
    for i in range(len(graph) - 1):  # 0 ~ N
        for node in graph:
            for next_node in graph[node]:
                if distances[next_node] > graph[node][next_node] + distances[node]:
                    distances[next_node] = graph[node][next_node] + distances[node]
    for node in graph:
        for next_node in graph[node]:
            if distances[next_node] > graph[node][next_node] + distances[node]:
                return -1

    return distances

N, M = map(int, stdin.readline().split())

graph = {}
for node in range(1, N + 1):
    graph[str(node)] = {}

for _ in range(M):
    A, B, C = stdin.readline().rstrip().split()
    if graph[A].get(B):
        if graph[A][B] > int(C):
            graph[A][B] = int(C)
    else:
        graph[A][B] = int(C)

distances = bellman_ford(graph, '1')
if distances == -1:
    print("-1")
else:
    for i in range(2, N + 1):
        print(distances[str(i)] if distances[str(i)] != INF else -1)


























































