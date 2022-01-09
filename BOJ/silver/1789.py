
s = int(input())
total = 0
for i in range(1, s):
    total += i
    if total > s:
        print(i-1)
        break
