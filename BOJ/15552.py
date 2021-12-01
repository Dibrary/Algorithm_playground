import sys

n = int(input())

while n > 0:
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))
    n -= 1

for i in range(0, n):
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))
