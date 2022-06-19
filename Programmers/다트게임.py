'''
kakao 2018 blind
'''

# def solution(dartResult):
#     tmp_idx = 0
#
#     result = []
#     dartResult += "0" # 숫자 앞을 기준으로 자르기 때문에, 맨 마지막 값이 안 들어감, 처리를 위해 임시로 계산 (끝에 주어진 값이 숫자라 하더라도, 괜찮다)
#     for idx, i in enumerate(dartResult):
#         if idx != 0 and i.isdigit():
#             result.append(dartResult[tmp_idx:idx])
#             tmp_idx = idx
#     print(result) # 분리하는 데 까지는 성공.
#
#
#
#
# if __name__=="__main__":
#     solution("1S*2T*3S9")
#
# # 제일 먼저 든 생각은 숫자 앞을 기준으로, 띄워놔야 한다는 생각


# def solution(dartResult):
#     tmp = []
#     idx = 0
#     for i in range(len(dartResult)):
#         if dartResult[i].isalpha():
#             tmp.append(dartResult[idx:i+1])
#             idx = i+1
#         if dartResult[i] in ["*","#"]:
#             tmp.append(dartResult[idx:i+1])
#             idx = i+1
#     # 여기까지 하면 분리가 완료된다.
#     print(tmp)
#
#     now = 0
#     result = 0
#     bbefore = 0
#     before = 0
#     for idx, j in enumerate(tmp):
#         if len(j) == 2:
#             no = j[0]
#             rg = j[1]
#             if j[1] == "S":
#                 now =  int(no)
#             elif j[1] == "D":
#                 now =  int(no)**2
#             elif j[1] == "T":
#                 now =  int(no)**3
#             result += now
#
#             if idx == 0:
#                 bbefore = now
#             elif idx == 1:
#                 before = now
#             elif idx >= 2:
#                 bbefore = before
#                 before = now
#
#         else: # 특수문자의 경우
#             if idx > 2 and j == "*":
#                 result += bbefore*2
#                 result += before*2
#             elif idx == 1 and j == "*":
#                 result += bbefore*2
#             elif idx > 2 and j == "#":
#                 result += before*(-1)
#                 bbefore = before*(-1)
#             elif idx == 1 and j == "#":
#                 result += bbefore*(-1)
#     print(result)






def solution(dartResult):
    tmp = []
    idx = 0
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            tmp.append(dartResult[idx:i+1])
            idx = i+1
        if dartResult[i] in ["*","#"]:
            tmp.append(dartResult[idx:i+1])
            idx = i+1
    # 여기까지 하면 분리가 완료된다.

    values = [] # 3개가 들어간다.
    idxs = [] # 값이 있던 index만 넣음.

    for idx, i in enumerate(tmp):
        if len(i) >= 2: # == 2 로 하면 안 됨.
            number = int(i[:-1])
            order = i[-1]
            if order == "S":
                values.append(number)
            elif order == "D":
                values.append(number**2)
            elif order == "T":
                values.append(number**3)
            idxs.append(idx)

    for idx, k in enumerate(tmp):
        if k in ["*","#"]:
            temp = [ x for x in idxs if x < idx] # 해당 특수기호보다 적은 것만 뽑아 놓음.
            if k == "*":
                for m in temp[-2:]:
                    values[idxs.index(m)] = values[idxs.index(m)]*2
            elif k == "#":
                values[temp[-1:][0]] =values[temp[-1:][0]]*(-1)
    return sum(values)


print(solution("1S2D*3T")) # 37
print(solution("1D2S#10S")) # 9

print(solution("1D2S0T")) # 3
print(solution("1S*2T*3S")) # 23
print(solution("1D#2S*3S")) # 5

# 예제는 통과하는데 32개 중 6개가 실패

