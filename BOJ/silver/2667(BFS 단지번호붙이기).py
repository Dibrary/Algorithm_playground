# from collections import deque
#
# n = int(input())
#
# danzi = []
# for _ in range(n):
#     danzi.append(list(map(int, input())))
#
# visited = [[False for _ in range(len(danzi[0]))] for _ in range(len(danzi))]  # 방문여부
#
#
# def bfs(i, j):
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#
#     q = deque([[i, j]])
#     visited[i][j] = True
#
#     count = 1
#     while q:
#         y, x = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if -1 < nx < len(danzi[0]) and -1 < ny < len(danzi) and visited[ny][nx] == False and danzi[ny][nx] == 1:
#                 q.append([ny, nx])
#                 count += 1
#             print(visited)
#     return count
#
#
# cnt = 0
# results = []
# for i in range(len(danzi)):  # y
#     for j in range(len(danzi[0])):  # x
#         if visited[i][j] == False and danzi[i][j] == 1:
#             value = bfs(i, j)
#             results.append(value)
#             cnt += 1
#
# print(cnt)
# results.sort()
# for k in results:
#     print(k)

# 위 코드가 내가 짠 초안이고, 무한루프가 끝나지 않음 =_=

from collections import deque

n = int(input())

danzi = []
for _ in range(n):
    danzi.append(list(map(int, input())))

visited = [[False for _ in range(len(danzi[0]))] for _ in range(len(danzi))]  # 방문여부


def bfs(i, j):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([[i, j]])
    visited[i][j] = True

    count = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < len(danzi[0]) and -1 < ny < len(danzi) and visited[ny][nx] == False and danzi[ny][nx] == 1:
                q.append([ny, nx])
                visited[ny][nx] = True # 여기서 방문 처리를 하지 않아서 무한루프가 끝나지 않는 것
                # 반복은 while문 안에서 돌기 때문에 방문 처리 코드가 반드시 필요하다.
                count += 1 # 한 번 들어온 구간에서 실제 방문한 갯수만 세진다.
    return count


cnt = 0
results = []
for i in range(len(danzi)):  # y
    for j in range(len(danzi[0])):  # x
        if visited[i][j] == False and danzi[i][j] == 1:
            value = bfs(i, j)
            results.append(value)
            cnt += 1 # 몇 번 bfs로 들어갔는지를 센다.

print(cnt)
results.sort()
for k in results:
    print(k)

