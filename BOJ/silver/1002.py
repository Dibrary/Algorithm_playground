
import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2 :
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접
        print(1)
    elif abs(r1-r2) < distance < (r1+r2):  # 두 점에서만 교차하는 것
        print(2)
    else:
        print(0)  # 나머지


# 주화입마에 걸릴뻔 =_=
# x, y가 다른경우, 원이 내부에 속한경우, 밖에 있는 경우 죄다 조건문으로 뽑아다가 처리할 뻔;;
# 핵심은 중심간의 거리와 반지름만으로 원이 내접하는지, 외접하는지, 내부에 있는지, 외부에 있는지를 판단하는 것이다.