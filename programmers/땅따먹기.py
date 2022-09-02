
# def solution(land):
#     result = max(land[0])
#     idx = land[0].index(result)
#
#     for i in range(1, len(land)):
#         if land[i].index(max(land[i])) == idx:
#             tmp = sorted(land[i], reverse=True)
#             result += tmp[1]
#             idx = land[i].index(tmp[1])
#         else:
#             result += max(land[i])
#             idx = land[i].index(max(land[i]))
#     return result
#
# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# 위 코드는 예제만 통과하지 모조리 실패함.



# def solution(land):
#     result = max(land[0])
#     idx = land[0].index(result)
#     for x in range(1, len(land)):
#         while land[x].index(max(land[x])) == idx:
#             land[x][idx] = 0
#         result += max(land[x])
#         idx = land[x].index(max(land[x]))
#     return result

# 위 코드도 모조리 실패함.
# 반드시 첫 번째에서 max값으로 시작하는 게 답은 아닌듯?


# def solution(land):
#     result = []
#     for k in range(4): # 열의 갯수는 무조건 4개라고 함.
#         temp = land[0][k]
#         idx = land[0].index(temp)
#
#         for x in range(1, len(land)):
#             while land[x].index(max(land[x])) == idx:
#                 land[x][idx] = 0
#             temp += max(land[x])
#             idx = land[x].index(max(land[x]))
#         result.append(temp)
#     return max(result)

# 위 코드도 모조리 실패.
'''
선택할 수 있는 것 중에 최대값만 선택하는 게 답이 아닌가?
맞는데, 그 최대값이 중간에 튀어나오면 그걸 선택하는 것으로 바뀌어야 함.
'''


def solution(land):
    temp = [0 for _ in range(len(land[0]))]

    for index in range(1, len(land)):
        result = [0 for _ in range(len(land[0]))]
        if index == 1:
            for idx, value in enumerate(land[index]):
                result[idx] = (value + max(land[index - 1][:idx] + land[index - 1][idx + 1:]))
        else:
            for idx, value in enumerate(land[index]):
                result[idx] = (value + max(temp[:idx] + temp[idx + 1:]))
        temp = result
    return max(temp)




## 다른 사람 코드 ##

def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])










import copy

def hopscotch(board, size):
    result = 0
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    for i in range(1,size):
        for j in range(4):
            temp = copy.deepcopy(board[i-1])
            temp[j] = 0
            board[i][j]+=max(temp)
    result = max(board[-1])
    return result











def solution(land):
    n = len(land)

    # dp[i][j] = i행 j열에서 점수의 최대값
    dp = [[0,0,0,0]] + land
    for i in range(1, n+1):
        dp[i][0] += max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] += max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] += max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        dp[i][3] += max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    return max(dp[n])











def hopscotch(board, size):
    for i in range(size):
        if i == size - 1:
            return max(board[i])
        for j in range(4):
            # print j, board[i][:j] + board[i][j + 1:]
            board[i + 1][j] += max(board[i][:j] + board[i][j + 1:])