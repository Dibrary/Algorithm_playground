# def solution(X, A):
#     tmp = set()
#
#     for idx, k in enumerate(A):
#         if k == X:
#             table = list(tmp)
#             flag = True
#             table.sort()
#             for index, m in enumerate(table):
#                 if index != 0:
#                     if m - table[index - 1] == 1:
#                         continue
#                     else:
#                         flag = False
#                         break
#             if flag == True:
#                 return idx
#         else:
#             tmp.add(k)

# 위 코드는 예제만 통과한 코드다. 0%;;;;

def solution(X, A):
    cnt = 0
    check = [True]+[False for _ in range(X)]
    for x in A:
        if check[x] == False:
            check[x] = True
            cnt += 1
        else:
            cnt += 1
        if x == X and set(check) == {True}:
            return cnt-1
    return -1

# 위 코드는 27% 받은 코드다. performance test 전부 실패

print(solution(5, [1,3,1,4,2,3,5,4]))


