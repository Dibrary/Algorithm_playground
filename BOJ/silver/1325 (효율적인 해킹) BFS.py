
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

table = [0 for _ in range(n+1)]

def bfs(start):
    global table
    visited = [False]*(n+1)

    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        table[node] += 1
        for k in graph[node]:
            if visited[k] == False:
                visited[k] = True
                q.append(k)

for i in range(1, n+1):
    bfs(i)

result = []
max_value = max(table)

for node, x in enumerate(table):
    if x == max_value:
        result.append(node)

result.sort()
print(" ".join(map(str, result)))

# 그냥 python으로 하면 2% 에서 시간초과로 멈춘다.




## 다른 사람 코드 ##
import sys
from collections import defaultdict, deque

inp = lambda: sys.stdin.readline()


def DFS(node):
    visited = [False] * (N + 1)
    cnt = 1
    visited[node] = True
    q = deque([node])
    while q:
        src = q.popleft()
        for tgt in trust[src]:
            if not visited[tgt]:
                q.append(tgt)
                visited[tgt] = True
                cnt += 1

    return cnt


N, M = map(int, inp().split())

trust = defaultdict(set)
for _ in range(M):
    src, tgt = map(int, inp().split())
    trust[tgt].add(src)

counts = []
max_cnt = 0
for node in range(1, N + 1):
    cnt = DFS(node)
    max_cnt = max(cnt, max_cnt)
    counts.append([node, cnt])

for i, cnt in counts:
    if cnt == max_cnt:
        print(i, end=' ')










import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

def bfs(start):
	cnt = 1
	queue = deque()
	queue.append(start)
	visit = [False for _ in range(n+1)]
	visit[start] = True

	while queue:
		cur = queue.popleft()

		for nx in graph[cur]:
			if not visit[nx]:
				visit[nx] = True
				cnt += 1
				queue.append(nx)

	return cnt

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a,b = map(int,input().split())
	graph[b].append(a)

maxCnt = 1
ans = []

for i in range(1,n+1):
	cnt = bfs(i)
	if cnt > maxCnt:
		maxCnt = cnt
		ans.clear()
		ans.append(i)
	elif cnt == maxCnt:
		ans.append(i)

print(*ans)










from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)


def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
    return count


result = []
max_value = -1
for i in range(1, n + 1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

for e in result:
    print(e, end=" ")