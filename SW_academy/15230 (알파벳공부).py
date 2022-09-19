
n = int(input())
for i in range(1, n+1):
    string = input()
    if string[0] != "a":
        print(f"#{i} {0}")
    else:
        index = 1
        for idx in range(1, len(string)):
            if ord(string[idx]) - ord(string[idx-1]) == 1:
                index += 1
            else:
                break
        print(f"#{i} {index}")





