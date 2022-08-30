
# def solution(n):
#     table = [x for x in range(1,n+1)]
#
#     cnt = 0
#     for i in range(1, int(n//2)):
#         for j in range(0, len(table)-i+1):
#             if j == 0 and (sum(table[j:j+i]) > n):
#                 break
#             if sum(table[j:j+i]) == n:
#                 cnt += 1
#     return cnt
#
# print(solution(15))

# 위 코드는 18개 중 3개 실패. 효율성 테스트는 단 하나도 통과 못함.
# 중간에 break부분 코드 제거 해도 3개는 실패.


# def solution(n):
#     cnt = 1
#
#     start_idx = 0
#     end_idx = 1
#
#     total_value = 0
#     while start_idx < end_idx:
#         if total_value < n:
#             total_value += end_idx
#             end_idx += 1
#         elif total_value > n:
#             start_idx += 1
#             total_value -= start_idx
#         elif total_value == n:
#             cnt += 1
#             end_idx += 1
#             total_value += end_idx
#     return cnt
#
# print(solution(15))
# 위 코드는 무한정 커진다. total_value < n , total_value > n 부분에서 n보다 커지면 total_value == n으로 못 감.

def solution(n):
    arr = [x for x in range(1, n + 1)]

    start_idx = 0
    end_idx = 0

    total_value = [arr[0]] # 처음 값을 넣어둠. 
    cnt = 0

    while start_idx <= end_idx:
        if start_idx < n:
            if sum(total_value) < n:
                end_idx += 1
                total_value.append(arr[end_idx])
            elif sum(total_value) > n:
                total_value.pop(0)
                start_idx += 1
            elif sum(total_value) == n:
                cnt += 1
                if end_idx < n - 1:
                    end_idx += 1
                    total_value.append(arr[end_idx])
                else:
                    break
        else:
            break
    return cnt

# 통과






## 다른 사람 코드 ##
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])









def expressions(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1


    return answer










def expressions(num):
    answer = 0

    for i in range(1, num+1):
        sum_val = 0
        for j in range(i, num+1):
            sum_val += j
            if sum_val == num:
                answer += 1
                break
            elif sum_val > num:
                break

    return answer