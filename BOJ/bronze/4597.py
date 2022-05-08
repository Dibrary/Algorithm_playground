
while True:
    n = input()
    if n == "#":
        break
    else:
        result = ""
        if n[-1] == "e":
            result = n[:-1]+'0'
        else:
            result = n[:-1]+'1'
        print(result)


# 위 코드 잘못됨. 우선 e라고 해서 무조건 0이 아니다.
