def test():
    n = input()
    if n == "0": return 1
    if len(n) == 1:
        n = "0" + n
    first = n
    cnt = 0

    tmp = 0
    while first != tmp:
        tmp = int(n[0]) + int(n[1])
        if tmp >= 10:
            tmp -= 10
            tmp += int(n[1]) * 10
        else:
            tmp += int(n[1]) * 10
        tmp = str(tmp)
        n = tmp
        if len(tmp) != 2:
            n = "0" + n
        print(n, tmp)
        cnt += 1
    print(cnt)

if __name__=="__main__":
    test()
    # 예시 중에 26, 55, 71, 0은 처리할 수 있으나, 1에서 안 멈춘다..