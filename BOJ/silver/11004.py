
import sys
n, k = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
print("%d"%(arr[k-1]))


#  이렇게 하면 시간초과 걸린다.
for i in range(1, k+1):
    if i == k:
        print("%d"%(min(arr)))
    else:
        arr.pop(arr.index(min(arr)))