
my_str = input().strip()
tmp = [0 for x in range(26)]
for i in my_str:
    tmp[ord(i)-97] += 1

table = [x for x in 'abcdefghijklmnopqrstuvwxyz']

result = []
max_value = max(tmp)
for idx, k in enumerate(tmp):
    if k == max_value:
        result.append(table[idx])
result.sort()
print(''.join(map(str, result)))
# 통과. 근데 보기가;;;

from collections import Counter

my_str = input().strip()
tmp = Counter(my_str).most_common()
result = []
for x in tmp:
    if x[1] == tmp[0][1]:
        result.append(x[0])
result.sort()

print("".join(map(str, result)))



