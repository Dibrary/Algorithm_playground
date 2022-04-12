
table = {"B":"v","E":"ye","H":"n","P":"r","C":"s","y":"u","X":"h"}

string = input()
result = ''
for i in string:
    s = i.upper()
    if s in table:
        result += table[i]
    else:
        result += i.lower()

print(result)

# 왜 계속 틀리지.


