
n = int(input())

for _ in range(n):
    value = input()

    if len(value)%2 == 0:
        result = ""
        for i in range(0, len(value),2):
            result += value[i]
        print(result)

        result = ""
        for i in range(1, len(value),2):
            result += value[i]
        print(result)

    else:
        result = ""
        for i in range(0, len(value),2):
            result += value[i]
        for i in range(1, len(value),2):
            result += value[i]
        print(result)

        result = ""
        for i in range(1, len(value),2):
            result += value[i]
        for i in range(0, len(value),2):
            result += value[i]
        print(result)

# 다른 사람 코드

t = int(input())

for i in range(t):
    s = input()

    if len(s) % 2 == 0:
        print(s[::2])
        print(s[1::2])

    elif len(s) == 1:
        print(s)
        print(s)

    else:
        print(s[::2] + s[1::2])
        print(s[1::2] + s[::2])

# 다른 사람 코드

for _ in range(int(input())) :
    s = input()
    if len(s) % 2 == 1 :
        for i in range(0, len(s), 2) :
            print(s[i], end = '')
        for i in range(1, len(s), 2) :
            print(s[i], end = '')
        print()
        for i in range(1, len(s), 2) :
            print(s[i], end = '')
        for i in range(0, len(s), 2) :
            print(s[i], end = '')
        print()
    else :
        for i in range(0, len(s), 2) :
            print(s[i], end = '')
        print()
        for i in range(1, len(s), 2) :
            print(s[i], end = '')
        print()