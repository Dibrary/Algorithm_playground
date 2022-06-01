
import sys
input = sys.stdin.readline

n = int(input())

for m in range(n):
    k = int(input())
    arr = []
    for i in range(k):
        arr.append(int(input())+1)
    print(f"Case {m+1}:")
    for s in arr:
        if s > 6:
            continue
        else:
            print(s)

