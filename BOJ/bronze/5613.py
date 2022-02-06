result = None
op = None

while True:
    value = input()
    if value == "=":
        break
    if value.isdigit():
        if result == None:
            result = int(value)
        elif result != None and op != None:
            if op == "*":
                result *= int(value)
    else:
        op = value

