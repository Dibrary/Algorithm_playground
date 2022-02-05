

while True:
    string = input()
    string = string.lower()
    print(string)
    if string == "eoi":
        break
    if "nemo" in string:
        print("Found")
    else:
        print("Missing")