
table = {"A":11,"K":4,"Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}
non_table = {"A":11,"K":4,"Q":3,"J":2,"T":10, "9":0, "8":0, "7":0}

n, suit = input().split()
n = int(n)

result = 0
for _ in range(n*4):
    value = input()
    if value[1] == suit:
        result += table[value[0]]
    elif value[1] != suit:
        result += non_table[value[0]]

print(result)



