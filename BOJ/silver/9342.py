
def gem_seperate(gem_string):
    if gem_string[0] not in ["A","B","C","D","E","F"]:
        return "Good"
    if "A" not in gem_string:
        return "Good"
    if "C" not in gem_string:
        return "Good"
    if "F" not in gem_string:
        return "Good"
    return "Infected!"


# 마지막 규칙 "그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다." 이것의 의미를 모르겠음.

n = int(input())

for _ in range(n):
    gem_string = input()

    result = gem_seperate(gem_string)
    print(result)




