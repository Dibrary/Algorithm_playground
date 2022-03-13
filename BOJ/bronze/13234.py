first, op, second = input().split()

if op == "AND":
    if first == "true" and second == "true":
        print("true")
    else:
        print("false")

else:
    if first == "false" and second == "false":
        print("false")
    else:
        print("true")