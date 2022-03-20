
n = int(input())

# cnt = 0
# for _ in range(n):
#     string = input()
#     if "A" in string:
#         cnt += string.count("A")
#     if "B" in string:
#         cnt += string.count("B")
#     if "D" in string:
#         cnt += string.count("D")
#     if "O" in string:
#         cnt += string.count("O")
#     if "P" in string:
#         cnt += string.count("P")
#     if "Q" in string:
#         cnt += string.count("Q")
#     if "R" in string:
#         cnt += string.count("R")
#     print(cnt)

# 근데 위 처럼 하면 반복 코드가 너무 많다.

table = ["A","B","D","O","P","Q","R"]
for _ in range(n):
    cnt = 0
    string = input()
    for k in table:
        if k in string:
            if k != "B":
                cnt += string.count(k)
            else:
                cnt += string.count(k)*2
    print(cnt)

# 통과 안됨 ;; B는 2개로 쳐야됨.