# string = input()
# n = int(input())
# result = 0
# for _ in range(n):
#     ring = input()
#     for i in range(0, len(ring)):
#         if ring[i] == string[0]:
#             if ring[i:i+len(string)] == string:
#                 result += 1
#                 break
# print("%d"%(result))

# 실패

string = input()
n = int(input())

cnt = 0
for _ in range(n):
    ring = input()
    for i in range(len(ring)):
        if i+len(string) > len(ring):
            tmp = ring[i:i+len(string)]+ring[:(i+len(string))-len(ring)] # 여기 인덱스 중요
            if tmp == string:
                cnt += 1
                break
        else:
            if ring[i:i+len(string)] == string:
                cnt += 1
                break
print(cnt)

