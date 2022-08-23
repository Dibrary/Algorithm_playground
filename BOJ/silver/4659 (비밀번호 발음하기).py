# while True:
#     string = input()
#     if string == "end":
#         break
#
#     vowel_count = 0
#     flag = 0
#     for m in 'aeiou': # 모음이 반드시 하나는 있는지 거르는 코드.
#         vowel_count += string.count(m)
#     if vowel_count == 0:
#         print(f"{string} is not acceptable.")
#         flag = 1
#         continue
#
#     if flag == 0:
#         for idx, s in enumerate(string):
#             if len(string[idx:idx + 3]) >= 3 and len(set(string[idx:idx + 3])) == 1:
#                 print(f"{string} is not acceptable.")
#                 flag = 1
#                 break
#
#     if flag == 0 and len(string) != 1:
#         for k in range(len(string) - 1):
#             if string[k] == string[k + 1] and string[k] != 'e' and string[k] != 'o':
#                 print(f"{string} is not acceptable.")
#                 flag = 1
#                 break
#
#     if flag == 0:
#         print(f"{string} is acceptable.")

# 틀림
# 2번 규칙에서 '모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.'에서 모음이나 자음이 항상 같을 이유가 없다.


while True:
    string = input()
    if string == "end":
        break

    vowel_count = 0
    flag = 0
    for m in 'aeiou': # 모음이 반드시 하나는 있는지 거르는 코드.
        vowel_count += string.count(m)
    if vowel_count == 0:
        print(f"{string} is not acceptable.")
        flag = 1
        continue

    if flag == 0:
        for idx, s in enumerate(string):
            if len(string[idx:idx + 3]) >= 3:
                vowel_count = 0
                tmp = string[idx:idx+3]
                for m in 'aeiou':  # 모음이 반드시 하나는 있는지 거르는 코드.
                    vowel_count += tmp.count(m)
                notvowel_count = 0
                for n in 'bcdfghjklmnpqrstvwxyz':
                    notvowel_count += tmp.count(n)

                if vowel_count == 3 or notvowel_count == 3:
                    print(f"{string} is not acceptable.")
                    flag = 1
                    break

    if flag == 0 and len(string) != 1:
        for k in range(len(string) - 1):
            if string[k] == string[k + 1] and string[k] != 'e' and string[k] != 'o':
                print(f"{string} is not acceptable.")
                flag = 1
                break

    if flag == 0:
        print(f"{string} is acceptable.")

# 틀림. 근데 코드가 너무 지저분하다.













