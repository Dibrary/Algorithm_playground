

# m, n = map(int,input().split())
#
# snail = [[0 for _ in range(n)]for _ in range(m)]
#
# nx = 0
# ny = 0
#
# snail[ny][nx] = 1
#
# cnt = 0
# for c in range(1, n):
#     for k in range(n-c):
#         nx += 1
#         if snail[ny][nx] == 0:
#             snail[ny][nx] = 1
#         else:
#             break
#     cnt += 1
#     for j in range(m-c):
#         ny += 1
#         if snail[ny][nx] == 0:
#             snail[ny][nx] = 1
#         else:
#             break
#     cnt += 1
#     for s in range(n-c):
#         nx -= 1
#         if snail[ny][nx] == 0:
#             snail[ny][nx] = 1
#         else:
#             break
#     cnt += 1
#     for a in range(m-c):
#         ny -= 1
#         if snail[ny][nx] == 0:
#             snail[ny][nx] = 1
#         else:
#             break
#     cnt += 1
#
# print(snail)
# print(cnt)

# 우선 위 코드까지만 하면 차례대로 달팽이를 다 채운다.
# ㄴㄴ 예제에 대해서만 다 채운다. 6 4를 하면 안됨

'''
좌우로 이동할 때는, 오른쪽 갔다 왼쪽 간 이후에 -1이 되고
상하로 이동할 때는, 아래로 갈때가 n이면 위로 올라갈 때는 n-1 다시 아래로 갈 때는 n-2

'''

# m, n = map(int,input().split())
#
# snail = [[0 for _ in range(n)]for _ in range(m)]

# nx = 0
# ny = 0
#
# snail[ny][nx] = 1
#
# for a in range(n-1):
#     nx += 1
#     if snail[ny][nx] == 0:
#         snail[ny][nx] = 1
# for b in range(m-1):
#     ny += 1
#     if snail[ny][nx] == 0:
#         snail[ny][nx] = 1
#
# dy = 1
# dx = 1
# for c in range(n-dx):
#     nx -= 1
#     if snail[ny][nx] == 0:
#         snail[ny][nx] = 1
# for d in range(m-dy):
#     ny -= 1
#     if snail[ny][nx] == 0:
#         snail[ny][nx] = 1
#     dy += 1
# print(snail)

# 이렇게 접근하면 안 될 듯.

# from collections import deque
#
# m, n = map(int,input().split())
#
# snail = [[0 for _ in range(n)]for _ in range(m)]
#
# dd = [1,1,-1,-1] # 오른쪽, 아래쪽, 왼쪽, 위쪽
#
# nx = 0
# ny = 0
#
# snail[ny][nx] = 1
#
# idx = 0  # dd값을 위한 index
# cnt = 0
#
# q = deque([[ny,nx]])
#
# while q:
#     y, x = q.popleft()
#     if cnt >= 5 and snail[y + 1][x] == 1 and snail[y][x + 1] == 1 and snail[y - 1][x] == 1 and snail[y][x - 1] == 1:
#         break # 이 종료조건이 문제다.
#
#     if idx == 0:
#         nx = x + dd[idx]
#         ny = y
#         if nx >= n or snail[ny][nx] == 1:
#             idx += 1
#             q.append([ny, x])
#             cnt += 1
#         else:
#             snail[ny][nx] = 1
#             q.append([ny, nx])
#
#     elif idx == 1:
#         ny = y + dd[idx]
#         nx = x
#         if ny >= m or snail[ny][nx] == 1:
#             idx += 1
#             q.append([y, nx])
#             cnt += 1
#         else:
#             snail[ny][nx] = 1
#             q.append([ny, nx])
#
#     elif idx == 2:
#         nx = x + dd[idx]
#         ny = y
#         if nx < 0 or snail[ny][nx] == 1:
#             idx += 1
#             q.append([ny, x])
#             cnt += 1
#         else:
#             snail[ny][nx] = 1
#             q.append([ny, nx])
#
#     elif idx == 3:
#         ny = y + dd[idx]
#         nx = x
#         if ny < 0 or snail[ny][nx] == 1:
#             idx = 0
#             q.append([y, nx])
#             cnt += 1
#         else:
#             snail[ny][nx] = 1
#             q.append([ny, nx])
# 위 코드처럼 하면 5 3 부터 그보다 큰 숫자들에 대해 cnt 구할 수 있음.

### 다른 사람 코드

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

board = [[1]*(n+2)]+[[1]+[0]*n+[1] for _ in range(m)]+[[1]*(n+2)]
# 실제 돌아야 하는 map 가장자리에 1로 된 벽을 추가로 세워서 만듦.

dy = [0,1,0,-1]
dx = [1,0,-1,0]

y = 1
x = 1
dir = 0
ans = 0

t = m*n

while True:
    if not board[y][x]:
        board[y][x] = 1
        t -= 1
        if t == 0:
            break
        y += dy[dir]
        x += dx[dir]
    else:
        y -= dy[dir]
        x -= dx[dir]
        dir = (dir+1)%4
        ans += 1
        y += dy[dir]
        x += dx[dir]
print(ans)


## 다른 사람 코드
r,c = map(int,input().split())

def sol(r,c):
    if r == 1:
        return 0
    return sol(c,r-1) + 1 # 재귀
print(sol(r,c))

## 다른 사람 코드
n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

check = [[False]*m for _ in range(n)]
x, y = 0, 0
dir = 0
turn = 0
while True:
    check[x][y] = True
    nx, ny = x + dx[dir], y + dy[dir]
    if not (0 <= nx < n and 0 <= ny < m) or check[nx][ny]:
        dir = (dir+1)%4
        nx, ny = x + dx[dir], y + dy[dir]
        if not (0 <= nx < n and 0 <= ny < m) or check[nx][ny]:
            break
        turn += 1
    x, y = nx, ny

print(turn)
