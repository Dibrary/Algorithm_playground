# # import sys
# # input = sys.stdin.readline
#
# n = int(input())
#
# img = []
# for _ in range(n):
#     img.append([x for x in input()]) # 입력 받고 해당 글자를 하나씩 list에 쪼개서 넣는다.
#
# def dfs(i, j, target): # 처음에 들어오는 것을 target으로 해야 함.
#     global visited
#
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#
#     que = [[i,j]]
#     visited[i][j] = 1
#
#     while que:
#         i, j = que.pop()
#         for k in range(4):
#             nx = dx[k]+j
#             ny = dy[k]+i
#             if -1 < nx < len(img[0]) and -1 < ny < len(img):
#                 if visited[nx][ny] == 0 and img[nx][ny] == target:
#                     visited[nx][ny] = 1
#                     que.append([ny,nx]) # 여기 nx, ny 방향 주의
#
# visited = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
#
# normal = dict()
#
# for i in range(len(img)):
#     for j in range(len(img[0])):
#         if visited[i][j] == 0:
#             dfs(i, j, img[i][j])
#             if img[i][j] not in normal:
#                 normal[img[i][j]] = 1
#             else:
#                 normal[img[i][j]] += 1
#
# visited = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
#
# abnormal = dict()
#
# def dfs_abnormal(i, j, target): # 처음에 들어오는 것을 target으로 해야 함.
#     global visited
#
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#
#     que = [[i,j]]
#     visited[i][j] = 1
#
#     while que:
#         i, j = que.pop()
#         for k in range(4):
#             nx = dx[k]+j
#             ny = dy[k]+i
#             if -1 < nx < len(img[0]) and -1 < ny < len(img):
#                 if visited[nx][ny] == 0:
#                     if target in ["R","G"]:
#                         if img[nx][ny] == "R" or img[nx][ny] == "G":
#                             visited[nx][ny] = 1
#                             que.append([ny,nx]) # 여기 nx, ny 방향 주의
#                     else:
#                         if img[nx][ny] == target:
#                             visited[nx][ny] = 1
#                             que.append([ny, nx])  # 여기 nx, ny 방향 주의
#
# for i in range(len(img)):
#     for j in range(len(img[0])):
#         if visited[i][j] == 0:
#             dfs_abnormal(i, j, img[i][j])
#             if img[i][j] not in abnormal:
#                 abnormal[img[i][j]] = 1
#             else:
#                 abnormal[img[i][j]] += 1
#
# print(f"{sum([v[1] for v in normal.items()])} {sum([v[1] for v in abnormal.items()])}")

# 런타임 에러가 난다.

# sys.stdin.readline을 지우면 9%에서 틀린다.

'''
반례
5
BGGBB
GGBBB
BBBRR
BBRRR
RRRRR

4 4 나와야 하는데 5 5 나온다.
'''

# 재귀 안쓰고 플려했는데 어려워서 안 되겠음.
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

import copy

n = int(input())

img = []
for _ in range(n):
    img.append([x for x in input()])
img2 = copy.deepcopy(img)

def dfs(x, y, target):
    if x <= -1 or x >= len(img) or y <= -1 or y >= len(img[0]) or img[x][y] == 1 :
        return False
    if img[x][y] != 1 and img[x][y] == target:
        img[x][y] = 1
        dfs(x-1, y, target)
        dfs(x, y-1, target)
        dfs(x+1, y, target)
        dfs(x, y+1, target)
        return True
    return False

normal_cnt = 0

for i in range(len(img)):
    for j in range(len(img[0])):
        if dfs(i, j, img[i][j]) == True:
            normal_cnt += 1

def dfs_abnormal(x, y, target):
    if x <= -1 or x >= len(img2) or y <= -1 or y >= len(img2[0]) or img2[x][y] == 1:
        return False
    else:
        if target in ["G","R"]:
            if img2[x][y] != 1 and (img2[x][y] == "G" or img2[x][y] == "R"):
                img2[x][y] = 1
                dfs_abnormal(x - 1, y, target)
                dfs_abnormal(x, y - 1, target)
                dfs_abnormal(x + 1, y, target)
                dfs_abnormal(x, y + 1, target)
                return True
        elif img2[x][y] != 1 and img2[x][y] == target:
            img2[x][y] = 1
            dfs_abnormal(x-1, y, target)
            dfs_abnormal(x, y-1, target)
            dfs_abnormal(x+1, y, target)
            dfs_abnormal(x, y+1, target)
            return True
        return False

abnormal_cnt = 0

for i in range(len(img2)):
    for j in range(len(img2[0])):
        if dfs_abnormal(i, j, img2[i][j]) == True:
            abnormal_cnt += 1

print(f"{normal_cnt} {abnormal_cnt}")

# 위 코드는 9%에서 재귀에러(깊이문제)가 나옴.
