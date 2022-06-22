# from collections import deque
#
# y, x = map(int, input().split())
#
# treasure = []
# for _ in range(y):
#     treasure.append([m for m in input()])
#
# visited = [[0 for _ in range(len(treasure[0]))] for _ in range(len(treasure))]
#
# def bfs(x, y):
#     que = deque()
#     que.append((x, y))
#
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#
#     cnt = 0
#
#     while que:
#         x, y = que.popleft()
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#
#             if nx < 0 or ny < 0 or nx >=len(treasure) or ny >= len(treasure[0]):
#                 continue
#             if treasure[nx][ny] == "L" and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 que.append((nx, ny))
#                 cnt += 1
#     return cnt
#
# result = []
# for i in range(len(treasure)):
#     for j in range(len(treasure[0])):
#         if visited[i][j] == 0:
#             result.append(bfs(i, j))
#
# print(result) # 일케 하면 그룹의 묶인 '갯수'가 나온다...

from collections import deque

l, w = map(int, input().split())

arr = []
for _ in range(l):
    arr.append(list(input()))

visited = [[0 for _ in range(w+1)] for _ in range(l+1)]

def bfs(y, x):
    q = deque([[y, x]])
    visited[y][x] = 1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    cnt = 1

    while q:
        y, x = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if -1<ny<l and -1<nx< w and arr[ny][nx] == "W" and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x]+1
                q.append([ny, nx])
                cnt += 1
    print(visited, cnt)
    '''
    예제 대로 하면 visited가 이렇게 바뀜
    [[2, 1, 1, 2, 3, 4, 1, 0], [1, 1, 1, 3, 1, 1, 1, 0], [1, 2, 1, 4, 1, 2, 3, 0], [1, 3, 1, 5, 1, 1, 1, 0], [2, 1, 1, 6, 1, 2, 3, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    return cnt

result = []

for i in range(l):
    for j in range(w):
        if visited[i][j] == 0 and arr[i][j] == "L":
            print(i, j, "i, j 값")
            result.append(bfs(i, j))

print(result)

'''
갯수만을 세면 최단 거리인지 알 수 없는 듯.


'''

