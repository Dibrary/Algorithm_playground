
n = int(input())

arr = []
for _ in range(n):
    age, name = list(input().split())
    arr.append((int(age), name))

arr.sort(key=lambda x:x[0])

for i in arr:
    print("%d %s"%(i[0],i[1]))
    