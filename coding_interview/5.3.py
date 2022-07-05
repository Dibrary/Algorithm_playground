
def check_max_length(table):
    max_length = 0
    for k in range(len(table) - 1):
        if len(table[k] + table[k + 1] + "1") >= max_length:
            max_length = len(table[k] + table[k + 1] + "1")
    return max_length


value = bin(1775)[2:]
print(value)

table = value.split("0")
print(table)
print(check_max_length(table))





value = bin(75942)[2:]
print(value)

table = value.split("0")
print(table)
print(check_max_length(table))
