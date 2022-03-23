
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

min_value = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    if u <= min_value:
        min_value = u

visited = [] # 방문여부 확인 리스트 어케 만들지

def bfs(start):
    # start 지점의 방문여부 어케 알지 
    
    q = []
    q.append(start)
    while q:
        node = pop(q[0])
        visited[node] = True
        for k in graph[node]:
            if visited[k] == False:
                q.append(k)

print(graph)


