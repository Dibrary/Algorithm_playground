def fn(n):
    return n*sum([k for k in range(1, n+2)])

t = int(input())

for _ in range(t):
    n = int(input())
    print(sum([fn(s) for s in range(1, n+1)]))

