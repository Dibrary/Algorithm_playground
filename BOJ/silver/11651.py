
n = int(input())

arr = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    arr.append((a, b))

arr.sort(key=lambda x:(int(x[1]), int(x[0])))

for i in arr:
    print("%d %d"%(i[0], i[1]))
