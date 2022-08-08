
# def solution(n, lost, reserve):
#
#     result = n-len(lost)
#     tmp = dict()
#
#     for i in reserve:
#         if i+1 in lost and i+1 not in tmp:
#             result += 1
#             tmp[i+1] = 1
#             continue
#         elif i-1 in lost and i-1 not in tmp:
#             result += 1
#             tmp[i-1] = 1
#             continue
#     return result

# 위 코드는 20개 중 6개를 통과하지 못한다.

'''
n이 주어지고, 
lost에 없는 숫자는 가지고 있는 사람이다.
'''


# def solution(n, lost, reserve):
#     result = n - len(lost)  # 가지고 온 학생 수
#
#     tmp = dict()
#     for k in reserve:
#         tmp[k] = 1
#
#     for i in lost:
#         if i - 1 in tmp and tmp[i - 1] == 1:
#             tmp[i - 1] = 0
#             result += 1
#         elif i + 1 in tmp and tmp[i + 1] == 1:
#             tmp[i + 1] = 0
#             result += 1
#     return result

# 위 코드로 바꾸니 20개 중 5개를 통과하지 못하게 바뀜.

'''
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

이게 내가 고려하지 못한 내용인듯?
'''

# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#
#     result = n - len(lost)  # 가지고 온 학생 수
#
#     tmp = dict()
#     for k in reserve:
#         tmp[k] = 1
#
#     for i in lost:
#         if i - 1 in tmp and tmp[i - 1] == 1:
#             tmp[i - 1] = 0
#             result += 1
#         elif i + 1 in tmp and tmp[i + 1] == 1:
#             tmp[i + 1] = 0
#             result += 1
#     return result
#
# # sort 코드 추가하니 4개만 실패라고 바뀜. (3,5,7,12 실패)
# # 12번은 아래 코드 실행하면 통과로 나옴. (lost랑 reserve에 중복으로 있는 것 문제)
#
# def solution(n, lost, reserve):
#     x = [m for m in reserve if m not in lost]  # reserve지만, 도난당했다면 1개뿐이라 빌려줄 수 없음.
#
#     result = n - len(lost)  # 가지고 온 학생 수
#
#     tmp = dict()
#     for k in x:
#         tmp[k] = 1
#
#     for i in lost:
#         if i - 1 in tmp and tmp[i - 1] == 1:
#             tmp[i - 1] = 0
#             result += 1
#         elif i + 1 in tmp and tmp[i + 1] == 1:
#             tmp[i + 1] = 0
#             result += 1
#     return result










## 다른 사람 코드 ##

def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve) # 파이썬은 차집합이 된다. (중복 없다고 할 때 쓰기 유용)
    new_reserve = set(reserve) - set(lost)
    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i + 1) # 빌려줄 수 있는 학생을 제거
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1) # 빌려줄 수 있는 학생을 제거
        else:
            n -= 1
    return n
    # 위 코드는 마지막 4개를 통과하지 못한다.


def solution(n, lost, reserve):
    reserve_student = set(reserve) - set(lost)
    lost_student = set(lost) - set(reserve)

    for student in reserve_student:
        if (student - 1) in lost_student: # -1번을 빌려줄 수 있으면
            lost_student.remove(student - 1) # 빌려준 학생을 lost_student에서 제외
        elif (student + 1) in lost_student: # +1번을 빌려줄 수 있으면
            lost_student.remove(student + 1) # 빌려준 학생을 lost_student에서 제외

    return n - len(lost_student) # 전체 인원 수에서 lost_student 수 만큼만 제외








def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN.sort()
    for l in lostN:
        for x in range(l-1, l+2):
            if x in reserveN:
                reserveN.remove(x)
                reserved += 1
                break
    return n - len(lostN) + reserved





def solution(n, lost, reserve):
    reserve = set(reserve)

    for size in [0, 1, -2]:
        lost = set(map(lambda x : x+size, lost))
        reserve, lost = reserve - lost, lost - reserve

    return n - len(lost)