
def canbewords(text, brokenLetters):
    table = text.split(" ")
    length = len(table)
    cnt = 0
    for i in table:
        for k in i:
            if k in brokenLetters:
                cnt += 1
                break
    return length - cnt

print(canbewords("leet code", "e"))
print(canbewords("leet code", "lt"))