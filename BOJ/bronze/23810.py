def five(n):
    for j in range(n):
        for i in range(n):
            if i == n - 1:
                print("@@@@@")
            else:
                print("@@@@@", end='')

def one(n):
    for j in range(n):
        for i in range(n):
            if i == n - 1:
                print("@")
            else:
                print("@", end='')

n = int(input())

five(n)
one(n)
five(n)
one(n)
one(n)