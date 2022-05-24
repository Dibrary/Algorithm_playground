# import sys
#
# input = sys.stdin.readline
#
# n = input()
# n = n[::-1]
#
# result = ""
# for idx, i in enumerate(n):
#     value = bin(int(i))[2:]
#
#     if len(value) == 1 and idx != len(n) - 1:
#         value = "00" + value
#     elif len(value) == 2 and idx != len(n) - 1:
#         value = "0" + value
#
#     result = value + result
# print(result)

# 런타임 에러

# import sys
#
# input = sys.stdin.readline
#
# n = input()
# n = n[::-1]
# n = n.replace("\n","")
#
# result = ""
# for idx, i in enumerate(n):
#     value = bin(int(i))[2:]
#
#     if len(value) == 1 and idx != len(n) - 1:
#         value = "00" + value
#     elif len(value) == 2 and idx != len(n) - 1:
#         value = "0" + value
#
#     result = value + result
# print(result)

# 위 코드도 시간초과 걸린다.
#import sys
#input = sys.stdin.readline

# table = {"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
#
# n = input()
# n = n[::-1]
# n = n.replace("\n","")
#
# result = ""
# for i in n:
#     result = table[i] + result
# if result[:2] == "00":
#     print(result[2:])
# elif result[:2] == "01":
#     print(result[1:])

# 5% 갔다가 시간초과 걸림.


# 헐 input 에서 진법으로 받는 방법이 있다. 2, 8, 16진수만 된다.
n = int(input(),8)
print(bin(n)[2:])

