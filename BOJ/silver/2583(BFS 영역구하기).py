
'''

dfs를 써서 0인 곳만 돌면서 갯수 + 크기를 구하면 된다.
갯수는 구하기 쉬운데, 크기는 어떻게 구하지?
사각형 좌표로 해당 위치에 값을 0이 아닌 걸로 바꿔줘야 한다.

'''

import sys
from collections import deque
# limit_number = 15000
# sys.setrecursionlimit(limit_number)

m, n, k = map(int, input().split()) # 세로, 가로, 사각형 갯수

grid = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            grid[j][k] = 1 # 영역이 역순으로 채워지는데;;?

visited = [[0 for _ in range(n+1)] for _ in range(m+1)]

# def dfs(y, x): # 갯수 세려면 반복문 꼴로 바꿔야 함.
#     if y<0 or x<0 or y>=len(grid) or x>=len(grid[0]) or visited[y][x] == 0 or :
#         return False
#     visited[y][x] = 1

def bfs(y, x):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([[y, x]])
    visited[y][x] = 1
    grid[y][x] = 1

    count = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (-1 < nx < len(grid[0])) and (-1 < ny < len(grid)) and (visited[ny][nx] == 0) and (grid[ny][nx] == 0):
                q.append([ny, nx])
                visited[ny][nx] = 1
                count += 1
    return count


total = 0
results = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visited[i][j] == 0 and grid[i][j] == 0:
            value = bfs(i, j)
            if value:
                total += 1
                results.append(value)
print(total)
results.sort()
print(" ".join(map(str, results)))


# 퍼지면서 방문처리 + 갯수 세려면 BFS 써야 한다.

