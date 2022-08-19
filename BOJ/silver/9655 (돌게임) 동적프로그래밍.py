n = int(input())
if n % 2 == 0:
    print('CY')
else:
    print('SK')

'''
이는 점화식으로 풀 수 있다. 1개 혹은 3개만 가져갈 수 있으므로 상대방의 선택지는 n-1 혹은 n-3이 될 것이다.

따라서 자신이 가져갈 수 있는 다음 경우의 수는 n-2, n-4, n-6 총 3가지가 될 것이다.

이렇게 쭉 내려가다 보면 결국 SK는 n이 홀 수 일 때 이길 수 있고, 짝수 일 때는 방법이 없이 CY가 우승을 차지하게 된다.
'''

## 다른 사람 코드 ##

import sys

N = int(sys.stdin.readline().rstrip())
turn_cnt = 0
dp = [-1] * (N + 1)
result = ''

for i in range(1, 4):
    if N >= i:
        dp[i] = i % 2

for i in range(4, N + 1):
    if dp[i - 3] == 1:
        dp[i] = 2
    else:
        dp[i] = 1

if dp[N] == 1:
    result = 'SK'
else:
    result = 'CY'

print(result)








import sys

n = int(sys.stdin.readline())
dp = [False for _ in range(n)]
dp[0] = True
for i in range(1, n):
    if not dp[i - 1] or (i >= 4 and dp[i - 4]):
        dp[i] = True
print("SK") if dp[n - 1] else print("CY")








def who_win(iter: int) -> str:
    if iter % 2 == 0:
        return "SK"
    else:
        return "CY"
def stone_game(N: int) -> str:
    #상근이 먼저 시작
    iter = 1
    while True:
        if N == 0:
            return who_win(iter)
        elif N < 3:
            N -= 1
        else:
            N -= 3
        iter += 1


N = int(input())
print(stone_game(N))









import sys
input = sys.stdin.readline

dp = [""] * 10001

dp[1] = "CY"
dp[2] = "SK"
dp[3] = "CY"
dp[4] = "SK"
dp[5] = "CY"

for i in range(6, 1001):
    if dp[i - 1] == "CY" or dp[i - 3] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"

n = int(input())
if dp[n] == "SK":
    print("CY")
else:
    print("SK")