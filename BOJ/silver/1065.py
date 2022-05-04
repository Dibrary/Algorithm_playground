
n = int(input())

result = 0

for s in range(1, n+1):
    temp = list(str(s))

    od = 0
    cnt = 0
    for k in range(1, len(temp)):
        ods = int(temp[k]) - int(temp[k-1])
        if k == 1:
            od = ods
            cnt += 1
        else:
            if od != ods:
                continue
            else:
                cnt += 1
    if cnt == len(temp)-1:
        result += 1

print(result)




