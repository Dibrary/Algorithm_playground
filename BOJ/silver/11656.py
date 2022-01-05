
string = input()
arr = []
for i in range(0, len(string)):
    arr.append(string[i:])
arr.sort()
for k in arr:
    print("%s"%(k))