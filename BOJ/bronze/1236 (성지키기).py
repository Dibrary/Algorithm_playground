
# n, m = map(int, input().split())  # 세로, 가로
#
# castle = []
# for _ in range(n):
#     castle.append(list(input()))
#
# castle_vertical = []
# for x in range(m):
#     tmp = []
#     for y in range(n):
#         tmp.append(castle[y][x])
#     castle_vertical.append(tmp)
#
# cnt = 0
# for y in range(n):
#     for x in range(m):
#         if set(castle[y]) == {'.'} and set(castle_vertical[x]) == {'.'}:
#             castle[y][x] = "X"
#             cnt += 1
# print(cnt)

# 2%에서 틀림

# n, m = map(int, input().split())  # 세로, 가로
#
# castle = []
# for _ in range(n):
#     castle.append(list(input()))
#
# castle_vertical = []
# for x in range(m):
#     tmp = []
#     for y in range(n):
#         tmp.append(castle[y][x])
#     castle_vertical.append(tmp)
#
# cnt = 0
# for y in range(n):
#     for x in range(m):
#         if set(castle[y]) == {'.'} and set(castle_vertical[x]) == {'.'}:
#             castle[y][x] = "X"
#             castle_vertical[y][x] = "X" # vertical 체크를 안 해줬었음.
#             cnt += 1
# print(cnt)

# 위 코드도 2%에서 틀림.

'''
핵심은 대각선으로 한 번만 가면서 확인하면 될듯?
안된다. 대각선은 n*n 배열만 됨.. n*m이면?
'''

# from collections import deque

# def bfs(y, x):
#     cnt = 0
#
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     q = deque()
#     q.append((y, x))
#
#     while q:
#         y, x = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= m or ny >= n:
#                 continue
#             if visited[ny][nx] == False:
#                 visited[ny][nx] = True
#
#                 tmp = set()
#                 for a in range(n):
#                     tmp.add(maps[a][nx])
#                 if tmp == {'.'} or set(maps[ny]) == {'.'}:
#                     maps[ny][nx] = 'X'
#                     cnt += 1
#                 q.append((ny, nx))
#     return cnt
#
# n, m = map(int, input().split())
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# maps = []
# for _ in range(n):
#     maps.append(list(input()))
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if visited[i][j] == False:
#             result += bfs(i, j)
#
# print(result)

# 위 방식 대로 하면 '최솟값'이 안 나온다.

'''
먼저 x, y 축 모두가 .으로 구성된 곳에 X를 한 후에
순회 해야 할까?
'''

n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(input()))

result = 0

for y in range(n):
    for x in range(m):
        tmp = set()
        for s in range(n):
            tmp.add(maps[s][x])
        if tmp == {'.'} and set(maps[y]) == {'.'}:
            maps[y][x] = 'X'
            result += 1

for y in range(n):
    for x in range(m):
        tmp = set()
        for s in range(n):
            tmp.add(maps[s][x])
        if tmp == {'.'} or set(maps[y]) == {'.'}:
            maps[y][x] = 'X'
            result += 1
print(result)


n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(input()))

result = 0

def both(tmp, value):
    return tmp == {'.'} and set(maps[y]) == {'.'}
def single(tmp, value):
    return tmp == {'.'} or set(maps[y]) == {'.'}

f = [both, single]

for i in range(2):
    for y in range(n):
        for x in range(m):
            tmp = set()
            for s in range(n):
                tmp.add(maps[s][x])
            if f[i](tmp, set(maps[y])):
                maps[y][x] = 'X'
                result += 1
print(result)



## 다른 사람 코드 ##

import sys
n, m = map(int,sys.stdin.readline().split())
map_l = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(n)]
row = set()
col = set()

for i in range(n):
  for j in range(m):
    if map_l[i][j] == 'X':
      row.add(i)
      col.add(j)

print(max(n - len(row),m - len(col)))











N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph_line = list(input())
    graph.append(graph_line)

h, v = 0, 0

for i in range(N):
    check = True
    for j in range(M):
        if graph[i][j] != '.':
            check = False
    if check:
        h += 1

for i in range(M):
    check = True
    for j in range(N):
        if graph[j][i] != '.':
            check = False
    if check:
        v += 1

print(max(h, v))
