
# n = int(input())
#
# arr = [(0,0)]
#
# for i in range(1, n+1):
#     t, p = map(int, input().split())
#     arr.append((t, p))
#
# result = []
# for i in range(1, len(arr)):
#     idx = i
#     sum = 0
#
#     while idx < n+1:
#         if idx + arr[idx][0]-1 >= n+1:
#             break
#         else:
#             sum = arr[idx][1] + sum
#             idx = arr[idx][0] + idx
#     result.append(sum)
# print(max(result))

# 위 코드는 예제 3번까지는 잘 됨. # 1일 경우에가 문제다. 그리고 일은 '당일'을 포함해야됨.

n = int(input())

arr = [(0,0)]

for i in range(1, n+1):
    t, p = map(int, input().split())
    arr.append((t, p))
result = []
for i in range(1, len(arr)):
    idx = i
    sum = 0
    while idx < n+1:
        change_idx = arr[idx][0] + idx
        if change_idx >= n+1:
            break
        else:
            sum += arr[idx][1]
        idx = change_idx
    if idx == len(arr)-1 and arr[idx][0] == 1:
        sum += arr[idx][1]
    result.append(sum)
print(result) # 예제 4번이 안 된다.












## 다른 사람 코드 ##

n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])












n = int(input())

t_list = []
p_list = []
answer = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(n - 1, -1, -1):
    if t_list[i] + i > n:
        answer[i] = answer[i + 1]
    else:
        answer[i] = max(p_list[i] + answer[i + t_list[i]], answer[i + 1])

print(answer[0])









N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i + li[i][0], N+1): # 앞에서부터
        if dp[j] < dp[i] + li[i][1]:
            dp[j] = dp[i] + li[i][1]

print(dp[-1])


N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1): # 뒤에서부터
    if i + li[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], li[i][1] + dp[i + li[i][0]])

print(dp[0])


