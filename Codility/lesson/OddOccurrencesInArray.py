
# def solution(A):
#     table = [x for x in A if x != None]
#     temp = dict()
#     for x in table:
#         if x not in temp:
#             temp[x] = 1
#         else:
#             temp[x] += 1
#     for k in temp.keys():
#         if temp[k] == 1:
#             return k

# 위 코드는 66% 받은 코드.



print(solution([1,4,None,1,4]))
print(type(None))
