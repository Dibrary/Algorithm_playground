
a = bin(29)
b = bin(15)
# bin을 적용한 값(문자열)에서는 ^ & | 적용 불가능.

print(29^15, bin(29^15))


cnt = 0
for i in bin(29^15)[2:]:
    if i == "1":
        cnt += 1

print(cnt)


