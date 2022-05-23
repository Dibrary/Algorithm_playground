# import sys
#
# table = {"]": "[", ")": "(", "}": "{"}
#
# while True:
#     s = input()
#     if s == ".":
#         break
#     tmp = []
#     flag = 0
#     for i in s:
#         if i in "[({":
#             tmp.append(i)
#             flag = 1
#         elif i in table:
#             if len(tmp) == 0:
#                 tmp.append(0)
#                 flag = 1
#                 break
#             else:
#                 if table[i] == tmp[-1]:
#                     if len(tmp) == 0:
#                         flag = 1
#                         break
#                     else:
#                         tmp.pop()
#                         flag = 1
#
#     if tmp == [] or flag == 0:
#         print("yes")
#     else:
#         print("no")

# 이 코드 실패함
table = {"]": "[", ")": "(", "}": "{"}

while True:
    n = input()
    if n == ".":
        break
    tmp = []
    for i in n:
        if i in ["[","("]:
            tmp.append(i)
        if i in table and len(tmp)>=1:
            if tmp[-1] == table[i]:
                tmp.pop()
    if len(tmp) == 0:
        print("yes")
    else:
        print("no")

# 20%에서 틀림. 문자열이 균형을 맞는다는게 뭔말이지?

