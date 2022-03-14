
a, b, g = list(map(int, input().split()))

a_team = input().split()
b_team = input().split()

a_count, b_count = 0, 0
goals = input().split()

for i in goals:
    if i in a_team:
        a_count += 1
    elif i in b_team:
        b_count += 1

if a_count > b_count:
    print("A")
elif a_count < b_count:
    print("B")
else:
    print("TIE")



