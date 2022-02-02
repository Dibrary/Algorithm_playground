
while True:
    string = input()
    if string == "#":
        break
    alphabet = string[0]
    print(alphabet)
    print("%s %d"%(alphabet, (string[1:].lower()).count(alphabet)))



