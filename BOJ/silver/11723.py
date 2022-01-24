import sys
input = sys.stdin.readline

# m = int(input())
#
# table = set()
#
# for _ in range(m):
#     string = input().split()
#     if len(string) == 2:
#         operator, value = string
#         value = int(value)
#
#     if operator == "add":
#         table.add(value)
#     elif operator == "check":
#         if value in table:print(1)
#         else:             print(0)
#
#     elif operator == "remove":
#         if value in table:
#             table.remove(value)
#     elif operator == "toggle":
#         if value not in table:
#             table.add(value)
#         else:
#             table.remove(value)
#     elif operator == "all":
#         table = {x for x in range(1, 21)}
#     elif operator == "empty":
#         table = set()

# 위 코드 처럼 하면 에러남. 왜냐하면 all과 empty는 operator로 안 들어 가서.

m = int(input())

table = set()

for _ in range(m):
    string = input().split()
    if len(string) == 2:
        operator, value = string
        value = int(value)
        if operator == "add":
            table.add(value)
        elif operator == "check":
            if value in table:
                print(1)
            else:
                print(0)
        elif operator == "remove":
            if value in table:
                table.remove(value)
        elif operator == "toggle":
            if value not in table:
                table.add(value)
            else:
                table.remove(value)
    else:
        if string[0] == "all":
            table = {x for x in range(1, 21)}
        elif string[0] == "empty":
            table = set()