
n, m = list(map(int, input().split()))

x, y, d = list(map(int, input().split()))

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

dx = [-1,0,1,0] # 좌,하,우,상
dy = [0,1,0,-1]

def direction():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
visited[x][y] = 1

turn_time = 0
while True:
    direction()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and maps[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        visited[nx][ny] = 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print("%d"%(count))







