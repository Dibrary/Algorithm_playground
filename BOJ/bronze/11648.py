
n = input()
if len(n) == 1:
    print(0)
else:
    cnt = 1
    while len(n) > 1:
        tmp = 1
        for i in n:
            tmp *= int(i)

        n = str(tmp)
        if len(n) != 1:
            cnt += 1
        elif len(n) == 1:
            print(cnt)
            break


