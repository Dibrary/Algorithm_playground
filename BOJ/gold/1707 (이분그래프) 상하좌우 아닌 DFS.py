
'''
기존 탐색 메커니즘에서 탐색한 노드에 다시 접근하게 됐을 때 현재 노드의 집합과 같으면 이분 그래프가 불가능하다.
사이클이 발생하면 이분 그래프가 불가능하다.

'''

# import sys
# sys.setrecursionlimit(10**6)
#
# def dfs(node, graph, visited):
#     if visited[node] == True:
#         return False
#     visited[node] = True
#
#     for k in graph[node]:
#         dfs(k, graph, visited)
#     return True
#
#
# k = int(input())
# for _ in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v+1)]
#
#     for _ in range(e):
#         n, e = map(int, input().split())
#         graph[n].append(e)
#
#     visited = [False] * (v+1)
#
#     for i in range(1, v+1):
#         if visited[i] == False: # 방문 안한 경우만 들어가는데,
#             if dfs(i, graph, visited) == False:
#                 print("NO")
#                 break # 더 진행 못하게 막음.
#             else:
#                 print("YES")

# 위 코드 좀 이상함.. 예제에서 2번째가 YES로 빠진다. (True 반환함.)


# from collections import deque
#
# def dfs(start, graph, visited):
#     q = deque()
#     q.append(start)
#
#     while q:
#         node = q.popleft()
#         if visited[node] == True:
#             return False
#         visited[node] = True
#         for i in graph[node]:
#             q.append(i)
#     return True
#
#
# k = int(input())
#
# for _ in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v+1)]
#
#     for _ in range(e):
#         n, e = map(int, input().split())
#         graph[n].append(e)
#
#     visited = [False] * (v+1)
#
#     for i in range(1, v+1):
#         if visited[i] == False: # 방문 안한 경우만 들어가는데,
#             if dfs(i, graph, visited) == False:
#                 print("NO")
#                 break # 더 진행 못하게 막음.
#             else:
#                 print("YES")
#                 break

# 위 코드 틀림

from collections import deque

def dfs(start, graph, visited):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        if visited[node] == True:
            return False
        visited[node] = True
        for i in graph[node]:
            q.append(i)
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        n, e = map(int, input().split())
        graph[n].append(e)

    visited = [False] * (v+1)

    result = []
    for i in range(1, v+1):
        if visited[i] == False: # 방문 안한 경우만 들어가는데,
            result.append(dfs(i, graph, visited))
    if False in result:
        print("NO")
    else:
        print("YES")

# 그냥 단순히 방문 여부만 따질 게 아니라, "이분이 가능한지"를 판별해야 함. 이게 중요.



## 다른 사람 코드 ##

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

K = int(input())
RED, BLUE = 1, -1

def dfs(vertex, color):
    global flag
    colors[vertex] = color  # 시작 정점 color 색으로 칠함.

    # 인접한 정점들 중에서
    for graph in graphs[vertex]:
        # 인접한 정점의 색상이 같으면 이분 그래프 X 이므로 종료
        if colors[graph] == color:
            flag = False
            return
        # 정점을 칠한적이 없으면 재귀 함수 호출
        if colors[graph] == 0:
            dfs(graph, -color)

for i in range(K):
    V, E = map(int, input().split())

    graphs = [[] for _ in range(V + 1)]  # 연결리스트 그래프
    colors = [0] * (V + 1)  # 색상 저장
    flag = True
    for _ in range(E):
        x, y = map(int, input().split())
        graphs[x].append(y)
        graphs[y].append(x)

    for v in range(1, V + 1):
        if not flag:
            break
        if colors[v] == 0:
            dfs(v, RED)  # 처음에 빨간색으로 칠함. (파란색으로 먼저 칠해도 상관 X)

    print('YES' if flag else "NO")

# 위 코드는 pypy로 하면 메모리 초과 나오고, python으로 해야 통과 됨.








import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfsf(start,group):
    global error
    if error :
        return
    visited[start]=group
    for i in D[start]:
        if visited[i]== 0 :
            dfsf(i,-group)
        elif visited[start] == visited[i]:
            error=True
            return #재귀리턴

k = int(input())
for _ in range(k): #test case 시작
    v,e = map(int, input().split())
    D = [[]for i in range(v+1)]
    visited = [0] * (v + 1)
    error = False
    for _ in range(e):
        u, v = map(int, input().split())
        D[u].append(v)
        D[v].append(u)

    for i in range(1,v+1):
        if visited[i] == 0 :
            dfsf(i,1)
            if error==True :
                break #for문나옴
    if error  :
        print("NO")
    else :
        print("YES")












import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def bfs(m, color, start_node):
    queue = deque()
    queue.append(start_node)
    color[start_node] = 1
    while queue:
        now = queue.popleft()
        for node in m[now]:
            if color[node] == 0:
                queue.append(node)
                color[node] = -1 * color[now]
            else:
                if color[node] == color[now]:
                    return False
    if 0 in color:
        return bfs(m, color, color.index(0))
    return True


K = int(input())
for _ in range(K):
    V, E = list(map(int, input().split()))
    m = [[] for _ in range(V + 1)]
    color = [0] * (V + 1)
    color[0] = [-1]
    for _ in range(E):
        u, v = list(map(int, input().split()))
        m[u].append(v)
        m[v].append(u)

    print("YES" if bfs(m, color, 1) else "NO")


