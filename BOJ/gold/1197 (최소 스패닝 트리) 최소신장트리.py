
'''
최소신장트리 = 모든 노드를 연결할 때 사용된 엣지의 가중치 합을 최소로 하는 트리.

모든 엣지 중 가장 가중치가 낮은 것 부터 잇는다.
'''
import heapq
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

v, e = map(int, input().split())

count = 0
q = []

parent = [x for x in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b)) # c라는 가중치를 앞에 놓아서 우선순위가 적용되게 함.

# 그냥 우선순위대로 v-1까지 뽑는다고 되는 게 아니라,
# 간선 뽑아놓고, 해당 간선을 연결하면 사이클이 생성되는지 확인해야 한다.

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p # 부모 테이블 갱신
    return parent[a] # a의 루트 노드 반환

def union(a,b):
    a = find(a); b = find(b)

    if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
        parent[b] = a
    else:
        parent[a] = b

useEdge = 0
result = 0

while useEdge < v-1:
    cost, start, end = heapq.heappop(q) # 가중치가 낮은 것 부터 꺼낸다.
    if find(start) != find(end):
        union(start, end)
        result = result + cost
        useEdge += 1

print(result)


## 다른 사람 코드 ##

V, E = map(int, input().split())
ans = 0
parent = [i for i in range(V+1)]

def findParent(parent, x):
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
for _ in range(E):
    _a, _b, c = map(int, input().split())
    edges.append((c, _a, _b))

edges.sort(key = lambda x:x[0])

for c, _a, _b in edges:
    if findParent(parent, _a) != findParent(parent, _b):
        union(parent, _a, _b)
        ans += c

print(ans)









import sys
from collections import deque
import heapq
import copy

v, e = map(int, input().split())
L = []
cycle = [i for i in range(v + 1)]
ans = 0
n = 0
for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(L, [c, min(a, b), max(a, b)])


def find(u):
    if u != cycle[u]:
        cycle[u] = find(cycle[u])
    return cycle[u]


def union(u, v):
    u = find(u)
    v = find(v)
    cycle[v] = cycle[u]


while n < v - 1:
    c, a, b = heapq.heappop(L)
    if find(a) != find(b):
        ans += c
        union(a, b)
        n += 1
print(ans)









import sys
import heapq as hq
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().rstrip().split())
    edges[A].append([C, B])
    edges[B].append([C, A])

visited = [False for _ in range(V + 1)]
heap = [[0, 1]]

total_weight = 0
cnt = 0

while heap:
    if cnt == V:
        break
    weight, node = hq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        total_weight += weight
        cnt += 1
        for i in edges[node]:
            hq.heappush(heap, i)
print(f"{total_weight}")