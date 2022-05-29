
n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(1, n):
    result += abs(arr[0]-arr[i])
print(result*(n-1))

# 틀림



