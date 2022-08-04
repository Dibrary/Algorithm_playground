
n = int(input())
A = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

for i in M:
    print(1 if i in A else 0)

## 다른 사람 코드 ##
import sys
sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

for i in arr_m:
    if i in a:
        print(1)
    else:
        print(0)