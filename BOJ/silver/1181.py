import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().split())
arr = list(set(arr))
arr.sort(key=lambda x:(len(x), x))
for i in arr:
    print("%s"%(i))