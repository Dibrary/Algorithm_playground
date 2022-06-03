#
# n = int(input())
# arr = list(map(int, input().split()))
#
# result = 0
# for i in range(1, n):
#     result += abs(arr[0]-arr[i])
# print(result*(n-1))

# 틀림

n = int(input())
arr = list(map(int, input().split()))
total = 0
for i in range(len(arr)-1):
    for j in range(i, len(arr)):
        total += abs(arr[i]-arr[j])
print(total*2)

# 시간이 너무 오래 걸린다. 8%에서 시간초과 걸림

