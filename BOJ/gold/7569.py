
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j]) # 처음에 시작점을 모조리 넣어두고 시작하는 것이 중요하다.

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs() # 여기서 실제 bfs 코드가 실행된다.

for i in matrix: # 여기서 도는 matrix는 bfs작업이 끝나서 초기 입력값과 다르다.
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)