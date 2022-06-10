
# n = int(input())
#
# cnt = 0
# while n != 1:
#     if n%3 == 0:
#         print("3")
#         n = n//3
#         cnt += 1
#         continue
#     if n%2 == 0:
#         print("2")
#         n = n//2
#         cnt += 1
#         continue
#
#     n -= 1
#     cnt += 1 # 이게 먼저 위치해야 할 듯. 
#
# print(cnt)



# 위 코드는 예제 답이 안 나온다.

n = int(input())

d = [0]*(n+1)

for i in range(2, n+1):
    d[i] = d[i-1] +1

    if i%2 == 0:
        d[i] = min(d[i] ,d[i // 2] + 1)
    if i%3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
# print(d)
print(d[n])






