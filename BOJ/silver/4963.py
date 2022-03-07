import sys
sys.setrecursionlimit(10**6)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    world = []
    for _ in range(h):
        world.append(list(map(int, input().split())))

    visited = [[0 for _ in range(w)] for _ in range(h)]

    dx = [-1,0,1,1,1,0,-1,-1]
    dy = [1,1,1,0,-1,-1,-1,0] # 대각선도 고려해야 하므로 총 8개
    def dfs(x, y):
        if x < 0 or y < 0 or x >=w or y >= h or visited[y][x] == 1:
            return False
        if world[y][x] and visited[y][x] == 0: # 땅은 1이므로 True
            visited[y][x] = 1
            for i in range(8): # 방향이 총 8개 이므로 이렇게 수정해야 함.
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
        return False

    cnt = 0
    for i in range(h):
        for j in range(w):
            # print(f'i값 {i} j값{j}')
            if dfs(i, j):
                cnt += 1
    print(cnt)

# 위 코드는 틀린 코드.






