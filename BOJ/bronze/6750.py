
string = input()

cnt = 0
for i in string:
    if i not in ["I","O","S","H","Z","X","N"]:
        cnt += 1
        break

if cnt != 0:
    print("NO")
else:
    print("YES")
