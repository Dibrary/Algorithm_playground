
arr = [0]*26

string = input()

for i in string:
    tmp = ord(i) - ord('a')
    arr[tmp] += 1
result = ""
for k in arr:
    result += str(k)+" "
print(result[:-1])

