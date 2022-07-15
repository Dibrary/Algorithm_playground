
'''
먼저 시간이 지남에 따라 치즈 변화하는 코드를 작성하고,

cnt를 어떻게 셀 지,
cnt -1 일 때, 몇 개인지 어떻게 셀 지를 정하자.
'''

from collections import deque
from copy import deepcopy

y, x = map(int, input().split())

cheese = []
for i in range(y):
    cheese.append(list(map(int, input().split())))


tmp = deepcopy(cheese) # 이렇게 비교 안하면, 바뀐 값에 대해서 적용하므로 확인이 어렵다.

# 4방향으로 치즈 녹는 것 만들기

dx = [0,0,-1,1]
dy = [-1,1,0,0]

cnt = 1
for b in range(1500):
    for i in range(y):
        for j in range(x):
            temp = []
            for k in range(4):
                nx = dx[k]+j
                ny = dy[k]+i
                if nx < 0 or ny < 0 or nx >= x or ny >= y: # 치즈 내부의 구멍 0에 의해서는 치즈가 녹지 않는다 ;;
                    continue
                else:
                    temp.append(tmp[ny][nx])
            if (0 in temp) and (cheese[i][j] == 1): # 사방에 0이 하나라도 있으면 해당 cheese는 0으로 변경시켜버린다.
                cheese[i][j] = 0
    print(tmp, cheese, cnt)
    check = set()
    for d in cheese:
        d = list(set(d))
        for e in d:
            check.add(e)
    if check == {0}:
        print(cnt)
        break
    else:
        tmp = deepcopy(cheese)
        cnt += 1

count = 0
for e in tmp:
    count += e.count(1)
print("1회 전에 남아있는 치즈 값", count)


