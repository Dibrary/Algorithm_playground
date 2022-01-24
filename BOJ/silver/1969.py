
n, m = map(int, input().split())
table = [[] for _ in range(m)]

for _ in range(n):
    dna = input()
    for idx, k in enumerate(dna):
        table[idx].append(k)

result = [0 for _ in range(m)]
cnt = 0
for idx, j in enumerate(table):
    if len(j) == len(set(j)):
        j.sort()
        result[idx] = j[0]
    else:
        for i in "TAGC":
            if i in j:
                tmp = j.count(i)
                if tmp >= cnt:
                    cnt = tmp
                    result[idx] = i
        cnt = 0

hamming_dist = 0
for idn, f in enumerate(table):
    for s in f:
        if s != result[idn]:
            hamming_dist += 1

print("".join(map(str, result)))
print(hamming_dist)

# index Error가 난다.