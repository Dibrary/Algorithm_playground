
def changer_lower(s):
    result = ""
    for i in s:
        if i.isalpha():
            result += i.lower()
        else:
            result += i
    return result

def replace_string(s):
    result = ""

    for k in s:
        if k.isdigit() or k.isalpha() or k == "_" or k == "-" or k == ".":
            result += k
    return result

def replace_dot(s):
    # table = ["."*n for n in range(1, len(s)) ]
    # result = ""
    # for i in table:
    #     result = s.replace(i,".") # 이 코드의 문제는 1번만 적용된다는 것.
    # return result

    pass



n = input()
n = changer_lower(n)
n = replace_string(n)
n = replace_dot(n)
print(n)

