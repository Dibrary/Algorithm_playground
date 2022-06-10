from collections import deque

m, n, h = map(int, input().split())

tomato = [[] for _ in range(h)] # 맨 앞에 있는게 가장 아래층이라 가정.
for k in range(h):
    for _ in range(n):
        tomato[k].append(list(map(int, input().split())))

que = deque([])
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                que.append([k, i, j])

# print(que) # 여기까진 들어옴

dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dh = [0,0,0,0,1,-1] # h는 위 아래밖에 이동 못함. # 이게 문제다.(for문 횟수)
# 일케 변경하면 6방향으로 이동하는 게 된다.

def bfs():
    while que:
        hh, x, y = que.popleft()
        for i in range(6):
            nx = dx[i]+x
            ny = dy[i]+y
            nhh = dh[i]+hh
            if 0 <= nx < n and 0 <= ny < m and 0 <= nhh <h and tomato[nhh][nx][ny] == 0:
                tomato[nhh][nx][ny] = tomato[hh][x][y] + 1 # 여기 코드가 틀렸다. [nhh][nx][ny]에서 +1 을 하면 0+1이 되버리므로 안됨.
                que.append([nhh, nx, ny])
        # print(tomato)

bfs() # 이 코드로 하면 토마토가 모두 변형이 된다.

res = 0
for k in tomato:
    for i in k:
        for j in i:
            if j == 0: # 하나라도 안 익은게 나오면 -1
                print(-1)
                exit(0)
        res = max(res, max(i))
print(res -1)