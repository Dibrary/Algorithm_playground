
'''
기존에 알던 y와 x가 바뀌어있음 주의.
'''

# n, m = map(int, input().split())
#
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
#
# for _ in range(m):
#     total = 0
#     x1, y1, x2, y2 = map(int, input().split())
#
#     for x in range(x1-1, x2):
#         total += sum(arr[x][y1-1:y2])
#     print(total)

# 시간초과 걸림. pypy로 해도 시간초과 걸림


'''
책 풀이에서는 일일이 더하면 안 되고,
해당 좌표가 주어지면 전체 구간합을 구한 뒤, 해당되지 않는 부분을 빼야 한다고 함.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (n+1)]

for _ in range(1, n+1):
    arr.append([0]+list(map(int, input().split()))) # 처음에 0이 들어가게 해서 만들었으므로 ( 그래야 시작부분 계산이 편함 )

d = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):   # 시작 인덱스를 1부터 n+1로 할 수 있다.
    for j in range(1, n+1):
        d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + arr[i][j]

# 가로 세로 첫 줄은 0이 나와야 한다.

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
    print(total)

# 위 코드로 바꿔도 pypy로 해야 통과된다.




## 다른 사람 코드 ##
from sys import stdin
n, m = map(int, stdin.readline().split())

numbers = [[0] * (n + 1)]

for _ in range(n):
    nums = [0] + [int(x) for x in stdin.readline().split()]
    numbers.append(nums)

# prefix sum 행렬 만들기

# 1. 행 별로 더하기
for i in range(1, n + 1):
    for j in range(1, n):
        numbers[i][j + 1] += numbers[i][j]

# 2. 열 별로 더하기
for j in range(1, n + 1):
    for i in range(1, n):
        numbers[i + 1][j] += numbers[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    # (x1, y1)에서 (x2, y2)까지의 합
    # p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])












import sys

N, M = map(int, sys.stdin.readline().split())
matrix = []

matrix.append([0]*(N+1))

for _ in range(N):
    line = [0] + list(map(int, sys.stdin.readline().split()))

    for j in range(1, N+1):
        line[j] += line[j-1]
    matrix.append(line)

for i in range(1, N+1):
    for j in range(1, N+1):
        matrix[j][i] += matrix[j-1][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(matrix[x2][y2] - matrix[x2][y1-1] - matrix[x1-1][y2] + matrix[x1-1][y1-1])