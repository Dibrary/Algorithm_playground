
'''
가장 기본적인 배낭문제
'''

n, k = map(int, input().split())

A = [[0 for x in range(k+1)] for x in range(n+1)]

val = []
wt = []

for _ in range(n):
    w, v = map(int ,input().split())
    wt.append(w)
    val.append(v)

for i in range(1, n+1):
    for w in range(1, k+1):
        if wt[i-1] > w:
            A[i][w] = A[i-1][w]
        else:
            valwith =  val[i-1] + A[i-1][w-wt[i-1]]
            valwithout = A[i-1][w]
            A[i][w] = max(valwith, valwithout)
print(A[n][w])



## 다른 사람 코드 ##

n, k = map(int, input().split())
items = [(0, 0)]
for _ in range(n):
    items.append(tuple(map(int, input().split())))

knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # value x weight (4, 7)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight, value = items[i][0], items[i][1]
        if j < weight:  # 현재 가방 허용 용량이 weight보다 작을 때
            knapsack[i][j] = knapsack[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다.
        else:  # 가방 허용 용량이 weight를 받아들일 수 있을 때 (weight 전까지의 값 + 해당 배낭의 값 vs 넣지 않음)
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
print(max(map(max, knapsack)))







n, k = map(int, input().split())
item = [[0, 0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())
    item.append([w, v])

for i in range(1, n+1):
    for j in range(1, k+1):
        if item[i][0] <= j:
            dp[i][j] = max(item[i][1] + dp[i-1][j-item[i][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])