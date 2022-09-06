
# string = input()
# odd = []  # 홀수개
# even = []  # 짝수개
#
# for x in set(string):
#     if string.count(x) % 2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)
#
# if len(odd) % 2 == 0 and odd != []:  # 홀수인 것이 홀수개라면 팰린드롬이 안 됨.
#     print("I'm Sorry Hansoo")
# else:
#     even.sort(reverse=True)
#     result = ""
#     if odd != []:
#         result = odd[0] * string.count(odd[0])  # 처음에 홀수 개를 중앙에 위치시킴
#     for x in even:
#         cnt = string.count(x) // 2
#         result = (x * cnt) + result + (x * cnt)
#     print(result)

# 위 코드로는 AAABB를 ABABA로 만들 수 없음. BAAAB로 만들어진다.











