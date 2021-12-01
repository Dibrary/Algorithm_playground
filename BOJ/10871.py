import sys

a, b = map(int, input().split())
values = list(map(int, sys.stdin.readline().split()))

print(values)

result = ""
for i in values:
    if b > i:
        result += str(i)+" "
print(result[:-1])


