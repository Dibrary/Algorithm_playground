while True:
    string = input()
    if string == "#":
        break

    flag = 0
    for i in string:
        if i == "b" or i == "d":
            continue
        elif i in "iovwx":
            continue
        else:
            print("INVALID")
            flag = 1
            break

    if flag == 0:
        result = ""
        for k in range(len(string) - 1, -1, -1):
            if string[k] == "d":
                result += "b"
            elif string[k] == "b":
                result += "d"
            else:
                result += string[k]
        print(result)

# 틀렸다고 나온다.