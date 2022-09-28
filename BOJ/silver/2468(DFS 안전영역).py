
# 먼저 든 생각은 들어있는 값을 하나씩 만 저장한 별개의 객체를 두고
# 해당 객체일 때 최대 값을 구한다.
# import sys
# limit_number = 15000
# sys.setrecursionlimit(limit_number)
#
# n = int(input())
#
# ground = []
# for _ in range(n):
#     ground.append(list(map(int, input().split())))
#
# tmp = set()
# for k in ground:
#     for j in k:
#         tmp.add(j)
#
# def dfs(y, x, target):
#     if y<0 or x<0 or (y>=len(ground)) or (x>=len(ground[0])) or (visited[y][x] == 1) or (ground[y][x] < target):
#         return False
#     visited[y][x] = 1
#     dfs(y-1, x, target)
#     dfs(y, x-1, target)
#     dfs(y+1, x, target)
#     dfs(y, x+1, target)
#     return True
#
# max_value = 0
#
# for k in tmp:
#     visited = [[0 for _ in range(len(ground[0]))] for _ in range(len(ground))]
#     cnt = 0
#     for i in range(len(ground)):
#         for j in range(len(ground[0])):
#             if visited[i][j] == 0 and ground[i][j] == k:
#                 if dfs(i, j, k):
#                     cnt += 1
#     if cnt >= max_value:
#         max_value = cnt
#
# print(max_value)

# 5%에서 틀림, 2번째 예제 답이 제대로 나오지 않음.


# n = int(input())
#
# ground = []
# for _ in range(n):
#     ground.append(list(map(int, input().split())))
#
# tmp = set()
# for k in ground:
#     for j in k:
#         tmp.add(j)
#
# def dfs(y, x, target):
#     if y<0 or x<0 or (y>=len(ground)) or (x>=len(ground[0])) or (visited[y][x] == 1) or (ground[y][x] <= target): # 같은 경우도 침수된다고 해야 함.
#         return False
#     visited[y][x] = 1
#     dfs(y-1, x, target)
#     dfs(y, x-1, target)
#     dfs(y+1, x, target)
#     dfs(y, x+1, target)
#     return True
#
# max_value = 0
#
# for k in tmp:
#     visited = [[0 for _ in range(len(ground[0]))] for _ in range(len(ground))]
#     cnt = 0
#     for i in range(len(ground)):
#         for j in range(len(ground[0])):
#             if visited[i][j] == 0 and ground[i][j] != k: # k랑 다를 때 진입해야 한다.
#                 if dfs(i, j, k):
#                     cnt += 1
#     if cnt >= max_value:
#         max_value = cnt
#
# print(max_value)

# 88%에서 틀림

import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

n = int(input())

ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))

tmp = set()
for k in ground:
    for j in k:
        tmp.add(j)

def dfs(y, x, target):
    if y<0 or x<0 or (y>=n) or (x>=n) or (visited[y][x] == 1) or (ground[y][x] <= target):
        return False
    if visited[y][x] == 0 and ground[y][x] > target: # 주어진 높이 '이하'까지가 잠기는 것이므로 >
        visited[y][x] = 1
        dfs(y-1, x, target)
        dfs(y, x-1, target)
        dfs(y+1, x, target)
        dfs(y, x+1, target)
        return True
    return False

max_value = [1] # 이게 문제였다. 아예 안 잠길 경우 섬 전체가 한덩어리 이므로 1을 반환해야함.

for k in tmp:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(len(ground)):
        for j in range(len(ground[0])):
            if visited[i][j] == 0 and ground[i][j] > k: # k보다 클 때 섬이다.
                dfs(i, j, k)
                cnt += 1

    max_value.append(cnt)
print(max(max_value))








## 다른 사람 코드 ##

from collections import deque

n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(maxNum):
    visited = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)













from sys import setrecursionlimit
setrecursionlimit(10000)
n = int(input())

grid = []
cnt = 0
visited = [[False for i in range(n)] for i in range(n)]
for _ in range(n):
    grid.append(list(map(int, input().split())))



def is_valid(x,y):
    if x >= 0 and x < n and y < n and y >= 0:
        return True
    return False

def dfs(x,y):
    if not is_valid(x,y):
        return False
    if visited[x][y] == False and grid[x][y] != 0:
        visited[x][y] = True
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False


def rain(depth):
    global visited
    visited = [[False for i in range(n)] for i in range(n)]
    for x in range(n):
        for y in range(n):
            if grid[x][y] <= depth:
                grid[x][y] = 0

min_depth = min(min(grid))
max_depth = max(max(grid))
depth = min_depth
answers = [1]

while(depth <= max_depth):
    rain(depth)
    cnt = 0
    for x in range(n):
        for y in range(n):
            if dfs(x,y):
                cnt += 1

    answers.append(cnt)
    depth += 1
print(max(answers))