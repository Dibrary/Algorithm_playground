
import sys
input = sys.stdin.readline # 이거 안 넣으면 시간초과 됨

n = int(input())

arr = []
for _ in range(n):
    arr.append(float(input()))

arr.sort()

for i in range(7):
    print('{:.3f}'.format(arr[i]))

