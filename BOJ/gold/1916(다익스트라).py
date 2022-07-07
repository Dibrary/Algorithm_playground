
import sys
import heapq

INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF for _ in range(n+1)]

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])



### 다른 사람 코드 ###


import sys, heapq


def evaluate(now, war):
    if now == war:
        return print(v[war])
    for i, j in d[now]:
        if v[j] > i + v[now]:
            v[j] = i + v[now]
            heapq.heappush(l, (v[j], j))
    d[now] = []
    if l:
        next = heapq.heappop(l)
    else:
        return print(v[war])
    while not d[next[1]]:
        if l:
            next = heapq.heappop(l)
        else:
            return print(v[war])
    return evaluate(next[1], war)


sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
d = {}
v = {}
l = []
for i in range(1, N + 1):
    d[i] = []
    v[i] = 99999999999
for _ in range(M):
    de, ar, c = map(int, sys.stdin.readline().split())
    heapq.heappush(d[de], (c, ar))
wde, war = map(int, sys.stdin.readline().split())
v[wde] = 0
evaluate(wde, war)








import sys
import heapq
n=int(input())
m=int(input())
data=[[] for _ in range(n+1)]
dis=[1e9]*(n+1)
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    data[a].append([b,c])
x,y=map(int,input().split())
def dij(s):
    q=[]
    dis[s]=0
    heapq.heappush(q,[0,s])
    while q:
        d,a=heapq.heappop(q)
        if d>dis[a]:
            continue
        for i in data[a]:
            b=i[0];c=i[1]
            if c+d<dis[b]:
                dis[b]=c+d
                heapq.heappush(q,[c+d,b])
dij(x)
print(dis[y])