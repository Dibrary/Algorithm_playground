

# import sys
# input = sys.stdin.readline
#
# tb = [1, 2] # 미리 공간을 만들어두지 않음.
#
# n = int(input())
# if n == 1:
#     print(tb[0])
# elif n == 2:
#     print(tb[1])
# else:
#     for i in range(1, n):
#         tb.append(tb[i]+tb[i-1]) # 그때그때 append를 함으로써 추가 공간 할당이 2배로 이뤄짐 (약 1.12배)
#     print(tb[n-1]%15746)


# 위 코드는 메모리 초과에 걸린다.



first = 1
second = 2

n = int(input())
if n == 1:
    print(first)
elif n == 2:
    print(second)
else:
    for i in range(1, n-1):
        third = (first+second)
        first = second
        second = third
    print(second%15746)

# 위 코드는 시간초과 걸린다.



### 다른 사람 코드 ###

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001 # 위에 메모리 초과와 다른 점은 미리 만들어놓고 채워나간다는 것.
dp[1] = 1
dp[2] = 2

for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])


