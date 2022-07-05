'''
1. 전체 섬에 대해 0의 갯수만큼 - 해주는 기능 필요
2. -적용이 이뤄진 후에 BFS로 섬을 순회한다. 섬이 2개가 되면 그 때의 cnt값 출력.
'''


from copy import deepcopy

n, m = map(int, input().split())

# 초기값 만들기
ice = []

for idx in range(n):
    values = list(map(int, input().split()))
    ice.append(values)

tmp = deepcopy(ice) # 이렇게 비교 안하면, 바뀐 값에 대해서 적용하므로 확인이 어렵다.

# 4방향으로 ice 녹는 것 만들기

dx = [0,0,-1,1]
dy = [-1,1,0,0]

print(ice, "초기 값")

for b in range(2):
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(4):
                nx = dx[k]+j
                ny = dy[k]+i
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                else:
                    if tmp[ny][nx] == 0:
                        cnt += 1
            value = ice[i][j] - cnt
            if value < 0 :
                ice[i][j] = 0
            else:
                ice[i][j] = value
    tmp = deepcopy(ice)
    print(ice, f"{b+1}차 적용")

# 이제 여기서 BFS로 섬의 갯수를 매 번 확인해야 한다.




#
# tmp = deepcopy(ice)
#
# for i in range(n):
#     for j in range(m):
#         cnt = 0
#         for k in range(4):
#             nx = dx[k]+j
#             ny = dy[k]+i
#             if nx < 0 or ny < 0 or nx >= m or ny >= n:
#                 continue
#             else:
#                 if tmp[ny][nx] == 0:
#                     cnt += 1
#         value = ice[i][j] - cnt
#         if value <= 0 :
#             ice[i][j] = 0
#         else:
#             ice[i][j] = value
# print(ice, "2차 적용")



