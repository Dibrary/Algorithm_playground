
# n = int(input())
#
# for idx, s in enumerate(range(n)):
#     string = "".join(map(str,sorted(str(s),reverse=True)))
#     print(s, string, idx)
#     '''
#     여기에서 숫자가 같은게 없는지 체크 함수 필요
#
#     '''
#
#     if str(s) == string:
#         print(s, idx, "해당됨")


# n = int(input())
# if n == 0:
#     print(0)
# n += 1
#
# for i in range(1800**3):
#     value = str(i)[::-1]
#     flag = 0
#     for k in range(len(value)-1):
#         if value[k] < value[k+1]:
#             continue
#         else:
#             flag = 1
#             break
#     if flag == 0:
#         n -= 1
#     else:
#         continue
#     if n == 0:
#         print(value[::-1])
#         break

# 근데 일케 하면 시간이 오래 걸릴게 뻔하다. 1%에서 진행이 안 된다.
# 반복문 말고, 5XV라는 값이라면 X는 4,3,2,1이 가능하고 4면 V는 3,2,1,0이 가능, 3이면 2,1,0가능, 2이면 1,0 가능 1이면 0만 가능하다.





