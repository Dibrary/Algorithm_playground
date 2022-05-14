
n = input()

joi_cnt = 0
ioi_cnt = 0

for i in range(len(n)):
    if n[i:i+3] == 'JOI':
        joi_cnt += 1
    elif n[i:i+3] == 'IOI':
        ioi_cnt += 1
print(joi_cnt)
print(ioi_cnt)



