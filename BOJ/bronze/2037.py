

p, w = map(int, input().split())
table = {"A":p, "B":p+w, "C":p+w*2, "D":p, "E":p+w, "F":p+w*2,
         "G":p, "H":p+w, "I":p+w*2, "J":p, "K":p+w, "L":p+w*2,
         "M":p, "N":p+w, "O":p+w*2,"P":p, "Q":p+w, "R":p+w*2,"S":p+w*3,
         "T":p, "U":p+w, "V":p+w*2,"W":p, "X":p+w, "Y":p+w*2,"Z":p+w*3,
         " ":p}

string = input()
result = 0
for s in string:
    result += table[s]
print(result)

# 문제 이해가 잘 안됨;
