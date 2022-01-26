import copy

n = int(input())

names = []
for _ in range(n):
    names.append(input())
tmp = copy.deepcopy(names)
tmp.sort()

if names == tmp:
    print("INCREASING")
else:
    tmp.sort(reverse=True)
    if names == tmp:
        print("DECREASING")
    else:
        print("NEITHER")