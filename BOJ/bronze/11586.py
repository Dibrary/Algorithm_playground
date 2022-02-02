
n = int(input())

mirrors = []
for _ in range(n):
    mirrors.append(input())

k = int(input())
if k == 1:
    for j in range(len(mirrors)):
        print(mirrors[j])
elif k == 2:
    for s in range(len(mirrors)):
        print(mirrors[s][::-1])
else:
    for k in range(len(mirrors)-1,-1,-1):
        print(mirrors[k])

