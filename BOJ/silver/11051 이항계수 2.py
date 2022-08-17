
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = i
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(n+1):
    for j in range(i): # 여기 범주 i까지인 것에 유의
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1] # 이 공식을 잘 기억해 두자.

print(dp[n][k]%10007)


## 다른 사람 코드 ##
n, k = map(int, input().split())
s = 1

for i in range(n-k+1, n+1):
    s *= i
if k != 0:
    for i in range(1, k):
        k *= i
else:
    k = 1

print(s//k%10007)







import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1

divisor = 1
for i in range(2, K+1):
    divisor *= i

print((result // divisor) % 10007)