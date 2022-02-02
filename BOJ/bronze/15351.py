
t = int(input())

for _ in range(t):
    string = input()

    value = 0
    for j in string:
        if j != " ":
            value += ord(j)-ord("A")+1
    if value == 100:
        print("PERFECT LIFE")
    else:
        print(value)

