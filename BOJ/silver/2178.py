
from collections import deque

n, m = map(int, input().split())

miro = []
for i in range(n):
    miro.append([int(x) for x in input()])

visited = [[0 for _ in range(0, len(miro[0]))] for _ in range(0, len(miro))]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue
            if visited[ny][nx] != 0:
                continue
            if visited[ny][nx] == 0 and miro[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))
            print(visited, miro, "중간단계") # 중간단계 이해하자.
    print(visited, miro)
    return visited[n-1][m-1]

print(bfs(0,0)+1)
