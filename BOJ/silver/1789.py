
s = int(input())
total = 0
for i in range(1, s):
    total += i
    if total > s:
        print(i-1) # 이렇게 하니 곧바로 틀림.
        break

for i in range(1, 1000000):
    value = ((i*(i+1))/2)
    if value >= s:
        print(i-1)
        break # 이렇게 하니 막판에 가서 틀림.

for i in range(1, 1000000):
    value = ((i * (i + 1)) / 2)
    if value > s:
        print(i - 1)
        break
    elif value == s:
        print(i)
        break



