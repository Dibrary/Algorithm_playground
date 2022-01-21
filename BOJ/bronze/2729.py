
a = "1000111"
b = "1010110"
a = a[::-1]
b = b[::-1]

result = ""
tmp = 0
if len(a)>= len(b):
    for i in range(len(b)):
        if (int(a[i])+int(b[i]))+tmp == 2:
            result += "0"
            tmp = 1
        elif (int(a[i])+int(b[i]))+tmp == 1:
            result += "1"
            tmp = 0
        elif (int(a[i])+int(b[i]))+tmp == 3:
            result += "1"
            tmp = 1
        elif (int(a[i])+int(b[i]))+tmp == 0:
            result += "0"
    print(result[::-1], tmp)
    for j in range(len(b), len(a)):
        print(j, a[j], tmp)
        if int(a[j])+tmp == 2 and j != len(a)-1:
            result += "0"
            tmp = 1
        elif int(a[j])+tmp == 1:
            result += "1"
            tmp = 0
        elif int(a[j])+tmp == 0 and j != len(a)-1:
            result += "0"
            tmp = 0
print(result[::-1])



