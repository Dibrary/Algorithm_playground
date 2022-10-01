
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

def solution(A):
    table = [x for x in A if x != None]
    temp = dict()
    for x in table:
        if x not in temp:
            temp[x] = 1
        else:
            temp[x] += 1
    for k in temp.keys():
        if temp[k]%2 == 1: # 홀수 개인 것만 걸러낸다.
            return k

print(solution([9,3,9,3,9,7,9]))
print(solution([1,4,None,1,4]))
