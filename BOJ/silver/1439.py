s = input()
zero_cnt = 0
one_cnt = 0
for i in range(0, len(s)-1):
    print(s[i], s[i+1], "값")
    if s[i] != s[i+1] and s[i] == 1:
        one_cnt += 1
    elif s[i] != s[i+1] and s[i] == 0:
        zero_cnt += 1
print(zero_cnt, one_cnt)


