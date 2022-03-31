
def double_func(string):
    tmp = ""
    for s in string:
        tmp += s
        tmp += s

    return tmp


n, m = map(int, input().split())
first_value = [[] for _ in range(n)]

for i in range(n):
    values = double_func(input())
    first_value[i].append(values)

compare_value = [[] for _ in range(n)]
for i in range(n):
    compare_value[i].append(input())

if first_value == compare_value:
    print("Eyfa")
else:
    print("Not Eyfa")

