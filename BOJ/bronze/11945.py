
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input())

for k in arr:
    print(k[::-1])


