
k = int(input())
for _ in range(k):
    n = int(input())

    def sol(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            return sol(n-1)+sol(n-2)+sol(n-3)

    print(sol(n))


### 다른 사람 풀이 ###

dp = [0 for _ in range(12)]
dp[1] = 1
dp[2] = 2 #2, 1+1
dp[3] = 4 #1+1+1, 2+1, 1+2, 3

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(int(input())):
    x = int(input())
    print(dp[x])