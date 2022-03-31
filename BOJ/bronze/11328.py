# n = int(input())
# for _ in range(n):
#     a, b = map(str, input().split())
#     a = list(a)
#     b = list(b)
#
#     flag = 0
#     for k in a:
#         if k in b:
#             b.remove(k)
#     print(b)
#     if b == []:
#         print("Possible")
#     else:
#         print("Impossible")

# 25%에서 틀렸다고 나옴.

n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    a = list(a)
    b = list(b)

    a.sort()
    b.sort()

    if a == b:
        print("Possible")
    else:
        print("Impossible")