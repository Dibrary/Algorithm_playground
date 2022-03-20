
n = int(input())

names = dict()
for _ in range(n):
    string = input()
    name, f_name = string.split()
    if (name, f_name) not in names:
        names[(name, f_name)] = string

result = []
for i in names:
    result.append(i)

result.sort(key=lambda x:(x[0],x[1]))

for s in result:
    print(names[s])

# 위 코드는 틀림.





