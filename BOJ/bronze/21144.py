# s = [x for x in range(1, 101)]
#
# n = int(input())
# arr = input()
#
# flag = 0
# for i in range(0, 100):
#     if i < 10:
#         if s[i] == arr[i]:
#             continue
#         else:
#             print(s[i])
#             flag = 1
#             break
#     elif 10 <= i < 100:
#         # 이렇게 하면 안 된다. 2자리씩 띄어야 한다;;
#         pass

# idx = dict()
# idx[1] = 1
# values = "1"
# for i in range(2, 101):
#     idx[i] = idx[i-1]+len(str(i))
#     values += str(i)
#
# n = int(input())
# index = idx[n]
# compare_value = values[:index]
# value = input()

# result = ""
# for i in a:
#     if i in b:
#         continue
#     else:
#         result += i
# 이 방식은 불가능.


# 생각을 바꾸니 간단하다. 그냥 순서대로 index로 찾되, 길이가 2개인 경우와 1개인 경우만 다르게 해서 비교함.

n = int(input())
value = input()
start_idx = 0
for i in range(1, 101):
    if value[start_idx:start_idx+len(str(i))] != str(i):
        print(i)
        break
    else:
        start_idx += len(str(i))

