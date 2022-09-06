
'''
모양은 무조건 4가지 뿐이다.
'''
from collections import Counter

# n = int(input())
#
# lines = []
# directs = []
#
# area = 0
# for _ in range(6):
#     direct, length = map(int, input().split())
#     directs.append(direct)
#     lines.append((direct, length))
#
# if directs == [1,4,1,4,2,3]:
#     print(lines[0][1]*lines[5][1]*n + lines[2][1]*lines[3][1]*n)
# elif directs == [1,4,2,4,2,3]:
#     print(lines[1][1]*lines[2][1]*n + lines[4][1]*lines[5][1]*n)
# elif directs == [1,4,2,3,2,3]:
#     print(lines[1][1]*lines[2][1]*n + lines[4][1]*lines[5][1]*n)
# elif directs == [2,3,1,3,1,4]:
#     print(lines[1][1] * lines[2][1] * n + lines[4][1] * lines[5][1] * n)
# elif directs == [2,3,1,4,1,4]:
#     print(lines[1][1] * lines[2][1] * n + lines[4][1] * lines[5][1] * n)
# elif directs == [2,3,1,3,1,4]:
#     print(lines[1][1] * lines[2][1] * n + lines[4][1] * lines[5][1] * n)
#
# elif directs == [3,2,4,1,4,1]:
#     print(lines[2][1] * lines[3][1] * n + lines[0][1] * lines[5][1] * n)
# elif directs == [3,2,4,2,4,1]:
#     print(lines[3][1] * lines[4][1] * n + lines[0][1] * lines[1][1] * n)
# elif directs == [3,2,4,1,3,1]:
#     print(lines[3][1] * lines[4][1] * n + lines[0][1] * lines[1][1] * n)
# elif directs == [3,1,4,2,4,2]:
#     print(lines[2][1] * lines[3][1] * n + lines[0][1] * lines[5][1] * n)
# elif directs == [3,1,4,1,4,2]:
#     print(lines[3][1] * lines[4][1] * n + lines[0][1] * lines[1][1] * n)
# elif directs == [3,1,4,2,3,2]:
#     print(lines[2][1] * lines[3][1] * n + lines[0][1] * lines[5][1] * n)
# 이런 개노가다 형태는 =_=;; 아닐 것이다.

# 규칙성이 계단형태가 반드시 있으므로, 계단 꼴을 알면 된다.
# 전체 넓이에서 작은 넓이를 빼면 어떨까?

from collections import Counter
n = int(input())

lines = dict()
arr = []

area = 0
for _ in range(6):
    direct, length = map(int, input().split())
    arr.append((direct, length))
    if direct not in lines:
        lines[direct]= [length]
    else:
        lines[direct].append(length)

arr = arr+arr[:3] # 반복되는 구간이 시작위치를 포함할 수 있어서 넣음.
first_idx, second_idx = 0, 0
for i in range(len(arr)-4):
    if arr[i][0] == arr[i+2][0] and arr[i+1][0] == arr[i+3][0]:
        first_idx = i+1
        second_idx = i+2
        break

tmp = sorted(Counter(lines).most_common(), key=lambda x: (len(x[1]),x[0])) # 길이가 1 방향인 것만.

total_area = tmp[0][1][0] * tmp[1][1][0] # 전체 넓이
minus_area = arr[first_idx][1] * arr[second_idx][1]

print((total_area - minus_area)*n)

# 14%에서 틀림






























