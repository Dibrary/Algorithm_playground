
n, successor = input().split()
n = int(n)

table = dict()

target_value = ""
target_idx = 0

for i in range(n):
    user, answer = input().split()
    if user == successor:
        target_value = answer
        target_idx = i
    table[user] = [answer,i]

cnt = 0
for k in table:
    if table[k][0] == target_value and table[k][1] <target_idx:
        cnt += 1

print(cnt)


