
# 바이러스 확산 코드는 BFS로 구현 가능.
# from collections import deque
#
# n, m = map(int, input().split())
#
# lab = []
# for _ in range(n):
#     lab.append(list(map(int, input().split())))
#
# queue = deque()
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs():
#     for idx, i in enumerate(lab):
#         for jdx, j in enumerate(i):
#             if j == 2:
#                 queue.append((idx, jdx))
#
#     while queue:
#         x, y = queue.popleft()
#         for s in range(4):
#             nx = x + dx[s]
#             ny = y + dy[s]
#
#             if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
#                 lab[nx][ny] = 1
#                 queue.append((nx, ny))
#
# dfs()
#
# print(lab)



### 다른 사람 코드 ###
from collections import deque
import copy

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1) # 백트래킹 방식
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
makeWall(0)
print(answer)

'''
어디서 최대값이 나올 지 모르므로 모든 경우의 수에 대해 수행해야 한다.
3개를 순서대로 선택해서 벽을 세우고, BFS를 하고 벽을 지우고 다음에 대해 벽을 세우고 BFS를 하고 벽을 지우고... 반복

백트래킹 방식을 이용했다.
'''


### 다른 사람 코드 ###

import sys, copy, collections

n, m = map(int, sys.stdin.readline().split())
max_num = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2

# 입력
g = [[0] * m for _ in range(n)]

for y in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]

    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == EMPTY:
            empty_list.append([y, x])
        if g[y][x] == VIRUS:
            virus_list.append([y, x])


# bfs 탐색
def bfs(ng):
    q = collections.deque([])
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    global max_num

    for virus in virus_list:
        q.append(virus)

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if ng[ny][nx] == EMPTY and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = VIRUS
                visited[ny][nx] = True

    for i in range(n):
        cnt += ng[i].count(EMPTY)

    if max_num < cnt:
        max_num = cnt


# 벽 세우기
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            g[y1][x1] = WALL
            g[y2][x2] = WALL
            g[y3][x3] = WALL

            ng = copy.deepcopy(g)
            bfs(ng)

            g[y1][x1] = EMPTY
            g[y2][x2] = EMPTY
            g[y3][x3] = EMPTY

print(max_num)

'''
먼저 벽을 세우고 bfs를 진행한다. 
벽은 for문 3개를 통해서 '모든 경우의 수'를 다 고려한다. (n, m이 8로 작게 주어졌으므로)
바이러스 퍼뜨린 후에 벽을 허문다.
'''