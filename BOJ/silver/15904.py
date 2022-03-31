# import sys
# s = sys.stdin.readline()
#
# tmp = ""
# for i in s:
#     if i.isupper() and i in ["U","C","P","C"]:
#         tmp += i
#
# if "UCPC" in tmp:
#     print("I love UCPC")
# else:
#     print("I hate UCPC")

# 위 코드 틀림.

# string = list(input().split())
#
# tmp = ""
# for i in string:
#     if i[0].isupper():
#     tmp += i[0]
#
# if "UCPC" in tmp:
#     print("I love UCPC")
# else:
#     print("I hate UCPC")

# 이것도 1%에서 틀림.


# string = list(input().split())
#
# tmp = ""
# for i in string:
#     for s in i:
#         if s.isupper():
#             tmp += s
# print(tmp)
#
# if "UCPC" in tmp:
#     print("I love UCPC")
# else:
#     print("I hate UCPC")

# 이건 진행도 안 하고 아예 틀림.
# 반례로 UCPPC가 있다. P를 하나 지우면 UCPC가 될 수 있는데, hate로 나옴.

string = list(input().split())

tmp = ""
for i in string:
    for idx, s in enumerate(i):
        if s.isupper():
            if idx == 0:
                tmp += s
            else:
                if tmp[-1] == s:
                    continue
                else:
                    tmp += s
if "UCPC" in tmp:
    print("I love UCPC")
else:
    print("I hate UCPC")
# 관건은 뽑아낸 대문자 중에 중복이 있으면 안 된다.
# 이것도 틀림.










