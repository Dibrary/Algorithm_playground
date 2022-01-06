
import sys

n, m = list(map(int, sys.stdin.readline().split()))
a = list(set(map(int, sys.stdin.readline().split())))
b = list(set(map(int, sys.stdin.readline().split())))
tmp = a+b
tmp.sort()

result = ""
for i in tmp:
    result += str(i) + " "
print("%s"%(result[:-1]))
