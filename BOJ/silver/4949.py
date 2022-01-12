import sys

table = {"]": "[", ")": "(", "}": "{"}

while True:
    s = input()
    if s == ".":
        break
    tmp = []
    flag = 0
    for i in s:
        if i in "[({":
            tmp.append(i)
            flag = 1
        elif i in table:
            if len(tmp) == 0:
                tmp.append(0)
                flag = 1
                break
            else:
                if table[i] == tmp[-1]:
                    if len(tmp) == 0:
                        flag = 1
                        break
                    else:
                        tmp.pop()
                        flag = 1

    if tmp == [] or flag == 0:
        print("yes")
    else:
        print("no")

# 이 코드 실패함

