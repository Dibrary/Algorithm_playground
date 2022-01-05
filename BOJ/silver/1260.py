'''

받은 데이터를 어떻게 처리할 것인가가 문제.
'''
n, m, start = list(map(int, input().split()))

graph = []
graph.append([])
for i in range(m):
    graph.append(list(map(int, input().split())))

print(graph)

visited = [0]*(n+1)
dfs_result = ""
def dfs(graph, start, visited):
    global dfs_result
    visited[start] = 1
    dfs_result += str(start)+" "
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, start, visited)
print(dfs_result)



