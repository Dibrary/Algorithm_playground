
n = int(input())
for _ in range(n):
    m = int(input())
    password = input()

    lower_idx, upper_idx, digit_idx, symbol_idx, length_idx = 0, 0, 0, 0, 0

    if m >= 12:
        length_idx = 1

    for k in password:
        if k.islower():
            lower_idx = 1
        if k.isupper():
            upper_idx = 1
        if k.isdigit():
            digit_idx = 1
        if k in "+_)(*&^%$#@!./,;{}":
            symbol_idx = 1

    if (lower_idx * upper_idx * digit_idx * length_idx * symbol_idx) == 1:
        print("valid")
    else:
        print("invalid")