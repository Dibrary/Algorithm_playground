
t = int(input())

for _ in range(t):
    p, m = map(int, input().split())

    arr = [0 for _ in range(m)]
    cnt = 0
    for i in range(p):
        seat = int(input())
        if i <= len(arr)-1:
            if seat not in arr and arr[i] == 0:
                arr.append(seat)
            else:
                cnt += 1
        else:
            cnt += 1
    print(cnt)

# 틀림


