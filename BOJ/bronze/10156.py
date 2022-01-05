
k, n, m = list(map(int, input().split()))
total = k*n
if total-m < 0:
    print("0")
else:
    print("%d"%(total-m))

