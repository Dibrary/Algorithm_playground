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





