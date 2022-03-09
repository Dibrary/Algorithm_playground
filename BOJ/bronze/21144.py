s = [x for x in range(1, 101)]

n = int(input())
arr = input()

flag = 0
for i in range(0, 100):
    if i < 10:
        if s[i] == arr[i]:
            continue
        else:
            print(s[i])
            flag = 1
            break
    elif 10 <= i < 100:
        # 이렇게 하면 안 된다. 2자리씩 띄어야 한다;;
        pass


