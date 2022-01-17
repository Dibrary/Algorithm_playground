
s = input()
value = []
start = 0
for i in range(0, len(s)):
    if s[i].isdigit() == False:
        value.append(s[start:i])
        start = i
    elif i == len(s)-1:
        value.append(s[start:])
print(value)