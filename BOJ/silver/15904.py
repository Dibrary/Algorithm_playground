import sys
s = sys.stdin.readline()

tmp = ""
for i in s:
    if i.isupper() and i in ["U","C","P","C"]:
        tmp += i

if "UCPC" in tmp:
    print("I love UCPC")
else:
    print("I hate UCPC")

