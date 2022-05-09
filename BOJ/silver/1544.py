#
# n = int(input())
#
# table = []
#
# result = 0
# for s in range(n):
#     if s == 1:
#         string = input()
#         temp = set()
#         for i in range(len(string)):
#             temp.add(string[i:]+string[:i])
#         table.append(temp)
#         result += 1
#     else:
#         string = input()
#         flag = 0
#         for m in table:
#             if string in m:
#                 flag = 1
#                 continue
#         if flag == 0:
#             temp = set()
#             for i in range(len(string)):
#                 temp.add(string[i:]+string[:i])
#             table.append(temp)
#             result += 1
# print(result)

# 장황하게 할 필요가 없네?

n = int(input())
table = []

for s in range(n):
    string = input()
    temp = set()
    for i in range(len(string)):
        temp.add(string[i:] + string[:i])
    if temp in table:
        continue
    else:
        table.append(temp) # 앗 set 안에 set은 안된다.
print(len(table))

# 위에서 해결한 핵심 개념은 [set은 안에 순서가 달라도 구성원소가 같으면 같은 것으로 친다.]
