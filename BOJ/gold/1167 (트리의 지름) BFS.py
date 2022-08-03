
'''
처음에 노드와의 거리를 같이 저장하는 방법이 의문.

임의의 노드에서 가장 긴 경로로 연결돼 있는 노드는 트리의 지름에 해당하는 두 노드 중 하나.
'''

# from collections import deque
#
# def bfs(start):
#     distance = [0 for _ in range(v + 1)]
#     visited = [False for _ in range(v + 1)]
#     visited[start[0]] = True
#     q = deque()
#     q.append(start)
#
#     while q:
#         node, length = q.popleft()
#         print(node, distance)
#         if node == start:
#             pass
#         else:
#             for i in tree[node]:
#                 if visited[i[0]] == False:
#                     visited[i[0]] = True
#                     distance[i[0]] += i[1]
#                     q.append(i)
#     return distance
#
#
#
# v = int(input())
# tree = [[] for _ in range(v+1)]
#
# for _ in range(v):
#     a, *k = list(map(int, input().split()))
#     for i in range(0, len(k[:-1]), 2):
#         tree[a].append(tuple(k[i:i+2]))
#
# result = []
# for k in range(1, v+1):
#     vv = bfs((k, 0))
#     result.append(vv)
#     print("====================")

# 위 코드 처럼만 하니 그저 간 곳의 거리만 나온다.

from collections import deque

def bfs(start):
    distance = [0 for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    visited[start[0]] = True
    q = deque()
    q.append(start)

    while q:
        node, length = q.popleft()
        if node == start:
            pass
        else:
            for i in tree[node]:
                if visited[i[0]] == False:
                    visited[i[0]] = True
                    distance[i[0]] += (i[1] + distance[node])
                    q.append(i)
    return distance


v = int(input())
tree = [[] for _ in range(v + 1)]

for _ in range(v):
    a, *k = list(map(int, input().split()))
    for i in range(0, len(k[:-1]), 2):
        tree[a].append(tuple(k[i:i + 2]))

result = []
for k in range(1, v + 1):
    vv = bfs((k, 0))
    result.append(max(vv))
print(max(result))

## 위 코드는 시간초과 걸린다.



## 다른 사람 코드 ##
from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, read().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e
    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)

# 이 코드는 시간초과 안걸린다. 왜?








from collections import deque
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    i = 1
    while i != len(tmp) - 1:
        tree[tmp[0]].append([tmp[i], tmp[i + 1]])
        i += 2


def bfs(start):
    queue = deque()
    queue.append([start, 0])
    visited = [0 for _ in range(n + 1)]
    maxd = 0
    maxi = start
    visited[start] = 1
    while queue:
        nowi, nowd = queue.popleft()
        if maxd < nowd:
            maxd = nowd
            maxi = nowi
        for e, d in tree[nowi]:
            if visited[e] == 0:
                queue.append([e, nowd + d])
                visited[e] = 1
    return maxi, maxd


tmpindex, tmpmax = bfs(1)
finalindex, finalmax = bfs(tmpindex)
print(finalmax)










from collections import deque
import random
DBG = False
n = int(input())
# 입력처리를 어떻게 해야 할까?
tree = [[] for _ in range(n+1)]
for _ in range(n):
	line = list(map(int, input().split()))
	# 인접리스트 만들어 주기
	for i in range(1, len(line)//2):
		tree[line[0]].append([line[2*i-1], line[2*i]])
# print("tree = {}".format(tree))
# tree = [[],
# 				[[3, 2]],
# 				[[4, 4]],
# 				[[1, 2], [4, 3]],
# 				[[2, 4], [3, 3], [5, 6]],
# 				[[4, 6]]]

def bfs(node):
	dist = [-1] * (n+1)
	q = deque()
	dist[node] = 0
	q.append(node)
	while q:
		x = q.popleft()
		for e, d in tree[x]:
			if dist[e] != -1: continue
			dist[e] = dist[x] + d
			q.append(e)
	max_node = dist.index(max(dist))
	max_dist = max(dist)
	return max_node, max_dist

node, dist = bfs(random.randrange(1, n+1))
if DBG: print("node = {}, dist = {}".format(node, dist))
node, dist = bfs(node)
if DBG: print("node = {}, dist = {}".format(node, dist))
print(dist)











import sys
from collections import deque
input = sys.stdin.readline

def bfs(root):
    q = deque()
    visited = [False] * (v+1)
    dist = [0] * (v+1)
    q.append(root)
    visited[root] = True
    while q:
        node = q.popleft()
        for child, weight in tree[node]:
            if not visited[child]:
                dist[child] = dist[node] + weight
                visited[child] = True
                q.append(child)
    max_dist = max(dist)
    return dist.index(max_dist),max_dist

v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    datas = list(map(int,input().split()))
    n1 = datas[0]
    for i in range(1,len(datas)-1,2):
        tree[n1].append([datas[i],datas[i+1]]) # 노드,weight 순으로 저장

a, _ = bfs(1)
_, max_dist = bfs(a)
print(max_dist)