
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




