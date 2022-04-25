
# n = int(input())

# for _ in range(n):
#     print("@@@@@")
#
# for s in range(3):
#     for _ in range(n):
#         print("@",end='')
#     for k in range(n):
#         for m in range(3):
#             if m == 2:
#                 print(" ")
#             else:
#                 print(" ",end='')
#         if s == 2:
#             for _ in range(n):
#                 print("@")
#         else:
#             for _ in range(n):
#                 print("@",end='')
#
# for _ in range(n):
#     print("@@@@@")


# 위에껀 코드 너무 복잡.

n = int(input())

for _ in range(n):
    print("@@@@@"*n)

for _ in range(n):
    print("@"*n + " " * 3 * n + "@"*n)
    print("@"*n + " " * 3 * n + "@"*n)
    print("@"*n + " " * 3 * n + "@"*n)

for _ in range(n):
    print("@@@@@"*n)











