
ipv6 = input()

if "::" in ipv6:
    tmp = ipv6.split(":")
    cnt = 0
    result = ""

    if ipv6[:2] == "::":
        tmp = tmp[1:]
        for k in tmp:
            if k != "":
                cnt += 1
        count = 8-cnt
        value = ("0000:"*count)

        for i in tmp:
            if i == "":
                result += value
            else:
                if len(i) != 4:
                    result += "0" * (4 - len(i)) + i + ":"
                else:
                    result += i + ":"
        print(result[:-1])


    elif ipv6[-2:] == "::":
        tmp = tmp[:-1]
        for k in tmp:
            if k != "":
                cnt += 1
        count = 8-cnt
        value = ("0000:" * count)[:-1]

        for i in tmp:
            if i == "":
                result += value
            else:
                if len(i) != 4:
                    result += "0" * (4 - len(i)) + i + ":"
                else:
                    result += i + ":"
        print(result)


    else: # ::가 중간에 있는 경우
        for k in tmp:
            if k != "":
                cnt += 1
        count = 8-cnt
        value = ("0000:"*count)

        for i in tmp:
            if i == "":
                result += value
            else:
                if len(i) != 4:
                    result += "0" * (4 - len(i)) + i + ":"
                else:
                    result += i + ":"
        print(result[:-1])

else:
    tmp = ipv6.split(":") # ::이 없는 경우
    result = ""
    for i in tmp:
        if len(i) != 4:
            result += "0" * (4 - len(i)) + i + ":"
        else:
            result += i + ":"
    print(result[:-1])

# 조건은 다 맞췄으나 너무 복잡함. 함수를 통해 공통부분을 뽑아내야 한다.

