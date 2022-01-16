
def func(title):
    arr = title.split(" ")

    result = ""
    for i in arr:
        for idx, j in enumerate(i):
            if idx == 0:
                result += j.upper()
            else:
                result += j.lower()
        result += " "
    return result[:-1]

print(func("capiTalIze tHe titLe"))
