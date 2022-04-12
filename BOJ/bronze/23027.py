

string = input()

if "A" in string:
    string = string.replace("B", "A")
    string = string.replace("C", "A")
    string = string.replace("D", "A")
    string = string.replace("F", "A")
elif ("A" not in string) and ("B" in string):
    string = string.replace("C", "B")
    string = string.replace("D", "B")
    string = string.replace("F", "B")
elif ("A" not in string) and ("B" not in string) and ("C" in string):
    string = string.replace("D", "C")
    string = string.replace("F", "C")
else:
    string = "A"*len(string)

print(string)

# 좀 더 깔끔한 방법이 없을까?


