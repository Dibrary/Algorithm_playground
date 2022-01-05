
n = int(input())

arr = []
for i in range(0, n):
    arr.append((input()))

idx = 0
result = []
for i in range(0, len(arr[0])):
    tmp = set()
    for j in range(0, len(arr)):
        tmp.add(arr[j][i])
    if len(tmp) == 1:
        result.append(arr[0][i])
    else:
        result.append("?")

string = ""
for i in result:
    string += i
print(string)
