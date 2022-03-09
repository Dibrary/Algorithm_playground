
cnt = 1
while True:
    string1 = [x for x in input()]
    string2 = [y for y in input()]
    if string1 == [n for n in "END"] and string2 == [n for n in "END"]:
        break

    flag = 0
    if len(string1) != len(string2):
        flag = 1
    else:
        for i in range(0, len(string1)):
            if string1[i] in string2:
                string2.remove(string1[i])
            else:
                flag = 1
                break

    if flag == 0:
        print(f'Case {cnt}: same')
    elif flag == 1:
        print(f'Case {cnt}: different')

    cnt += 1

