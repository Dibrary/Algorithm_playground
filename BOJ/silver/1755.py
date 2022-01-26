table = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
table2 = {"zero":"0", "one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

m, n = map(int, input().split())
temp = []

for i in range(m, n+1):
    tmp = []
    for j in str(i):
        tmp.append(table[j])
    temp.append(tmp)
temp.sort()

result = []
for k in temp:
    value = ""
    for s in k:
        value += table2[s]
    result.append(value)
for i in range(0, len(result), 10):
    print(" ".join(map(str, result[i:i+10])))