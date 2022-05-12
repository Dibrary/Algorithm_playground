import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    i -= 1;    j -= 1; # 리스트 인덱스 시작이 0부터라서.

    total = 0
    for m in range(i,x):
        for n in range(j,y):
            total += arr[m][n]
    print(total)

# 위 코드는 예제는 통과. 그러나 시간초과 발생.
# pypy로 하면 통과 됨. 아무래도 for문을 3겹 중첩해서 그런 듯.

# 다른 사람 코드 (Python으로 통과된 것)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = []
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    num_list.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = num_list[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

k = int(input())
sum = [0 for _ in range(k)]

for a in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])

