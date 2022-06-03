
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


## 다른 사람 코드

split_IPv6 = list(map(lambda x : x.split(':'), input().split('::')))
IPv6 = split_IPv6[0][:]

if len(split_IPv6) == 2:
    for i in range(8-len(IPv6)-len(split_IPv6[1])):
        IPv6.append('0000')
    for i in split_IPv6[1]:
        IPv6.append(i)

print(":".join(map(lambda x : x.zfill(4), IPv6)))

# 다른 사람 코드
import sys


IPv6 = list(map(str, sys.stdin.readline().strip("\n").split(":")))
idx = []
for i in range(len(IPv6)):

    if len(IPv6[i]) == 0:
        idx.append(i)
        continue

    if len(IPv6[i]) < 4:
        IPv6[i] = "0" * (4 - len(IPv6[i])) + IPv6[i]


if idx:
    for _ in idx:
        del IPv6[idx[0]]
    while len(IPv6) != 8:
        IPv6.insert(idx[0], "0000")


print(":".join(IPv6))
