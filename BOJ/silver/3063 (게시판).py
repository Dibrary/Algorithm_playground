
'''
문제에서 구하고자 하는 것은 처음 붙인 것의 '보이는 넓이'다.
단순히 점의 갯수로 세기엔 문제가 있다.

'''

# from collections import defaultdict
#
# t = int(input())
#
# for _ in range(t):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split()) # 왼쪽아래, 오른쪽 위 이렇게 값이 주어진다.
#
#     first = set()
#     for x in range(x1, x2+1):
#         for y in range(y1, y2+1):
#             first.add((x, y))
#
#     second = set()
#     for x in range(x3, x4+1):
#         for y in range(y3, y4+1):
#             second.add((x, y))
#
#     points = first - first.intersection(second)
#
#     table = defaultdict(list)
#     for m in points:
#         table[m[0]].append(m[1])
#
#     result = 0
#     for k in table.keys():
#         result += len(table[k])-1
#     print(result)

# 위 코드는 에러 있다. 왜냐하면, 차집합에서 뺀 것이 곧 넓이를 의미하지 않음 =_=;;

# t = int(input())
#
# for _ in range(t):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split()) # 왼쪽아래, 오른쪽 위 이렇게 값이 주어진다.
#
#     first = set()
#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             first.add((x, y, x+1 ,y+1)) # 점의 갯수를 세는게 아니라, 면적(왼쪽아래, 오른쪽 위 점)을 add함.
#
#     second = set()
#     for x in range(x3, x4):
#         for y in range(y3, y4):
#             second.add((x, y, x+1, y+1))
#
#     print(len(first- second))

# 위 코드는 12%에서 메모리 초과로 나옴.

# t = int(input())
#
# for _ in range(t):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split()) # 왼쪽아래, 오른쪽 위 이렇게 값이 주어진다.
#
#     first = set()
#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             first.add((x, y, x+1 ,y+1)) # 점의 갯수를 세는게 아니라, 면적(왼쪽아래, 오른쪽 위 점)을 add함.
#
#     for x in range(x3, x4):
#         for y in range(y3, y4):
#             if (x, y, x+1, y+1) in first:
#                 first.remove((x, y, x+1, y+1))
#
#     print(len(first))

# 위 코드도 메모리초과로 나온다. 임시로 값을 1~10000 범주로 넣어보면, 실행에 시간이 매우 오래걸림.

# from collections import deque
# import sys
# input = sys.stdin.readline
#
# t = int(input())
# for _ in range(t):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
#
#     arr = deque()
#     for a in range(x3, x4):
#         for b in range(y3, y4):
#             arr.append((a, b, a+1, b+1))
#
#     cnt = 0
#     for k in range(x1, x2):
#         for j in range(y1, y2):
#             if (k, j, k+1, j+1) in arr:
#                 continue
#             else:
#                 cnt += 1
#     print(cnt)
# 위 코드는 시간초과 나옴.

# import sys
# input = sys.stdin.readline
#
# t = int(input())
# for _ in range(t):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
#
#     cnt = 0
#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             if x3 <= x <= x4 and x3 <= x + 1 <= x4 and y3 <= y <= y4 and y3 <= y + 1 <= y4:
#                 continue
#             else:
#                 cnt += 1
#     print(cnt)

# 위 코드도 12%에서 시간초과 걸린다.
# 입력이 최대 10000*10000일 수 있으므로, 1억, 2천만개당 1초라고 가정하면 5초가 된다;;


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    cnt = 0
    for x in range(x1, x2):
        if x3 <= x <= x4 and x3 <= x + 1 <= x4:
            for y in range(y1, y2):
                if y3 <= y <= y4 and y3 <= y + 1 <= y4:
                    continue
                else:
                    cnt += 1
        else:
            cnt += y2-y1
    print(cnt)

# pypy로 해야 통과됨;;


## 다른 사람 코드 ##
import sys
input = sys.stdin.readline
def f(a,b,c,d):
    return max(min(b,d)-max(a,c), 0)
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    a = f(x1,x2,x3,x4)
    b = f(y1,y2,y3,y4)
    print((x2-x1) * (y2-y1) - a*b)










import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    # 영화 동아리 포스터 크기
    sang = (x2 - x1) * (y2 - y1)

    # 영화 포스터가 완전히 덮힐 때
    if x1 >= x3 and y1 >= y3 and x2 <= x4 and y2 <= y4:
        print(0)
    # 하나도 겹치지 않는 경우
    elif x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:
        print(sang)
    # 일부만 덮는 경우, 덮히는 부분 계산
    # 일부만 덮힌다면, 곂치는 선분은 2개
    else:
        if x1 < x3 < x2:
            x_left = x3
        else:
            x_left = x1
        if x1 < x4 < x2:
            x_right = x4
        else:
            x_right = x2

        if y1 < y3 < y2:
            y_down = y3
        else:
            y_down = y1
        if y1 < y4 < y2:
            y_up = y4
        else:
            y_up = y2

        sang -= (x_right - x_left) * (y_up - y_down)
        print(sang)








import sys

def ans():
    # x1, y1, x2, y2, x3, y3, x4, y4
    arr = list(map(int, sys.stdin.readline().split(" ")))
    poster = (arr[2] - arr[0]) * (arr[3] - arr[1])
    hor = 0 if arr[2] <= arr[4] or arr[6] <= arr[0] else min(arr[2], arr[6]) - max(arr[0], arr[4])
    ver = 0 if arr[1] >= arr[7] or arr[5] >= arr[3] else min(arr[3], arr[7]) - max(arr[1], arr[5])
    return poster - hor * ver


for _ in range(int(sys.stdin.readline())):
    print(ans())


