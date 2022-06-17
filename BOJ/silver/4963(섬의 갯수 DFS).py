
# import sys
# sys.setrecursionlimit(10**6)
# 
# while True:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
# 
#     world = []
#     for _ in range(h):
#         world.append(list(map(int, input().split())))
# 
#     visited = [[0 for _ in range(w)] for _ in range(h)]
# 
#     dx = [-1,0,1,1,1,0,-1,-1]
#     dy = [1,1,1,0,-1,-1,-1,0] # 대각선도 고려해야 하므로 총 8개
#     def dfs(x, y):
#         if x < 0 or y < 0 or x >=w or y >= h or visited[y][x] == 1:
#             return False
#         if world[y][x] and visited[y][x] == 0: # 땅은 1이므로 True
#             visited[y][x] = 1
#             for i in range(8): # 방향이 총 8개 이므로 이렇게 수정해야 함.
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 dfs(nx, ny)
#             return True
#         return False
# 
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             # print(f'i값 {i} j값{j}')
#             if dfs(i, j):
#                 cnt += 1
#     print(cnt)

# 위 코드는 틀린 코드.#################################################

# w, h = map(int, input().split())
#
# graph = []
# for _ in range(h):
#     graph.append(list(map(int, input().split())))
#
# visited = [[0 for _ in range(w)] for _ in range(h)]
#
# def dfs(y, x):
#     if y < 0 or x < 0 or y >= h or x >= w or graph[y][x] == 0 or visited[y][x] == 1:
#         return False
#     visited[y][x] = 1 # 방문 처리
#     dfs(y-1, x)
#     dfs(y, x-1)
#     dfs(y+1, x)
#     dfs(y, x+1)
#     return True
# print(visited)
#
# cnt = 0
# for i in range(h):
#     for j in range(w):
#         if visited[i][j] == 0:
#             answer = dfs(i, j)
#             if answer:
#                 cnt += 1
# print(visited)
#
# print(cnt)

# 위 코드까지만 하면 상하, 좌우만 이동이 가능한 것이 된다.
# 문제는 대각선도 걸어갈 수 있다고 함.

import sys
sys.setrecursionlimit(10**6)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    visited = [[0 for _ in range(w)] for _ in range(h)]

    def dfs(y, x):
        if y < 0 or x < 0 or y >= h or x >= w or graph[y][x] == 0 or visited[y][x] == 1:
            return False
        visited[y][x] = 1 # 방문 처리
        dfs(y-1, x)
        dfs(y, x-1)
        dfs(y+1, x)
        dfs(y, x+1)
        dfs(y-1,x-1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        dfs(y-1,x+1)
        return True

    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0:
                answer = dfs(i, j)
                if answer:
                    cnt += 1
    print(cnt)

### 다른 사람 코드 ####

from collections import deque
from sys import stdin

def bfs():
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]


while True:
    w, h = map(int, stdin.readline().split())
    graph = []
    queue = deque([])
    ans = []
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append(list(map(int, stdin.readline().split())))
    for a in range (h):
        for b in range(w):
            if graph[a][b] == 1:
                queue.append([b, a])
                ans.append(bfs())
    print(len(ans))


#### 다른 사람 코드 #####

"""
백준 4963번

1. 아이디어
- DFS로 돌면서 섬의 개수를 구한다

2. 시간복잡도
- O(V+E) = wh + 8wh = 9wh = 9*2500

3. 자료구조
- 지도 mab = int[][]
- 방문 chk = bool[][]
- 섬의 개수 count = int
"""

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline



while(True):

    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    mab = [list(map(int, input().split())) for _ in range(h)]
    chk = [[False]*w for _ in range(h)]
    count = 0

    dy = [1, 0, -1, 0, 1, -1, -1, 1]
    dx = [0, 1, 0 ,-1, 1, 1, -1, -1]
    def dfs(y, x):
        for i in range(8):
            py = y + dy[i]
            px = x + dx[i]

            if 0<=py<h and 0<=px<w:
                if chk[py][px] == False and mab[py][px] == 1:
                    chk[py][px] = True
                    dfs(py, px)

    for j in range(h):
        for i in range(w):
            if chk[j][i] == False and mab[j][i] == 1:
                chk[j][i] = True
                dfs(j, i)
                count += 1

    print(count)