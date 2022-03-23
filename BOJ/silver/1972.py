
while True:
    string = input()
    if string == "*":
        break

    tmp = []

    cnt = 0
    for i in range(1, len(string)):
        for m in range(0, len(string)):
            if m + i >= len(string):
                break
            else:
                tmp.append(string[m] + string[m + i])

        if len(tmp) == len(set(tmp)):
            cnt += 1
            tmp = []
    if len(string) - 1 == cnt:
        print(f'{string} is surprising.')
    else:
        print(f'{string} is NOT surprising.')


# 핵심은 1칸씩 띄어서 찾는 알고리즘.