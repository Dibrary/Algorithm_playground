sk = input()

tmp = []

start_idx = 0
end_idx = 0
for i in range(0, len(sk)):
    if sk[i] == sk[i].upper() and i == 0:
        tmp.append(sk[i])
        start_idx += 1
        end_idx += 1
    elif sk[i] == sk[i].upper() and i != 0:
        value = sk[start_idx:end_idx]
        tmp.append(value)
        tmp.append(sk[i])
        start_idx += (len(value)+1)
        end_idx += 1
    else:
        end_idx += 1
cnt = 0

for i in tmp:
    if i.isupper() == False:
        cnt += 3-len(i)
print(cnt)


# 예제랑 똑같이 동작하지만, 틀렸다.



