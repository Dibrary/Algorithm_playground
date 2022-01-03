import sys

n, m = list(map(int,sys.stdin.readline().split()))
a, b = set(), set()

for _ in range(n):
    a.add(sys.stdin.readline())
for _ in range(m):
    b.add(sys.stdin.readline())

result = a&b
print(len(result))
result = list(result)
result.sort()
for s in result:
    print(s)