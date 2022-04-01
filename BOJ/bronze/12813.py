
def reverse_func(a, b):
    a_reverse = ""
    b_reverse = ""

    for i in a:
        if i == "0":  a_reverse += "1"
        else:         a_reverse += "0"

    for j in b:
        if j == "0":  b_reverse += "1"
        else:         b_reverse += "0"

    return a_reverse[::-1], b_reverse[::-1] # 원본으로 반환

def and_func(a, b): # 3개 함수 구현을 해야됨.
    return None

def or_func(a, b):
    return None

def xor_func(a, b):
    return None

a = input()[::-1]
b = input()[::-1]

result = []
result.append(and_func(a, b))
result.append(or_func(a, b))
result.append(xor_func(a, b))
a_reverse, b_reverse = reverse_func(a, b)
result.append(a_reverse)
result.append(b_reverse)

for k in result:
    print(k)

