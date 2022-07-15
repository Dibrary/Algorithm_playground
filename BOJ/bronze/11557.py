
n = int(input())

for _ in range(n):
    s = int(input())
    name = None
    soju = 0
    for _ in range(s):
        a, b = input().split()
        if int(b) >= soju:
            name = a
            soju = int(b)
    print(name)


## 다른 사람 코드 ##
N = int(input())
for _ in range(N):
    S = int(input())
    D = {}
    for i in range(S):
        a, b = input().split()
        D[a] = int(b)
    ans = max(D, key = D.get)
    print(ans)