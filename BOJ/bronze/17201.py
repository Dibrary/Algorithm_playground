
n = int(input())
magnet = input()

flag = 0
for i in range(0, len(magnet)-1):
    if magnet[i] != magnet[i+1]:
        continue
    else:
        flag = 1
        break

if flag == 0: print("Yes")
else:         print("No")


