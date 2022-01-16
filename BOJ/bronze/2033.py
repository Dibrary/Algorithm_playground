
n = input()
n = n[::-1]

result = ""
tmp = 0
for idx, i in enumerate(n):
    tmporary = (int(i) + tmp)
    if idx != len(n)-1:
        if tmporary < 5:
            result += str(tmporary)
            tmp = 0
        else: # 5 보다 큰 경우
            tmp = 1
            result += "0"
    else:
        if tmporary >= 10:
            result += str(tmporary)[1]
            result += str(tmporary)[0]
        else:
            result += str(tmporary)
print(result[::-1])
# 위 코드 틀림


