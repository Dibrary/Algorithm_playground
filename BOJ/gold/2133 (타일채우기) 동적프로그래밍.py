
'''
문제를 보면, 타일로 딱 떨어지지 않는 경우는 출력을 0으로 해야 하는 건지 모르겠다.
소수점... 으로는 안 내보낼 듯.
'''

n = int(input())

# 초기 2와 4의 갯수는 직접 구할 수 있었으나 6은 못 구함.
# 갯수를 추정하는 '방법'을 알아야 한다.



## 다른 사람 코드 ##

n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3

for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]

    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]

    dp[i] += 2

print(dp[n])







n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else :
        dp[i] = 0
print(dp[n])
