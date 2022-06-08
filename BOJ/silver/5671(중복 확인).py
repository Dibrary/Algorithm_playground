
while True:
    try:
        n, m = map(int, input().split())
        arr = [x for x in range(n, m+1)]

        cnt = 0
        for i in arr:

            flag = 0
            value = str(i)
            for i in value:
                if value.count(i) > 1:
                    flag = 1
                    break
            if flag != 1:
                cnt += 1
        print(cnt)
    except:
        break
