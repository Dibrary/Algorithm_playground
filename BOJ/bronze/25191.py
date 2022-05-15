
n = int(input())
a, b = map(int, input().split())

tmp = a//2 + b

if tmp > n:
    print(n)
else:
    print(tmp)



