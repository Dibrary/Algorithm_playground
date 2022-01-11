
cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    days = 0
    while True:
        if v >= p:
            v -= p
            days += l
        else:
            if v <= l:
                days += v
                break
            elif v > l:
                days += l
                break
    print("Case %d: %d"%(cnt, days))
    cnt += 1