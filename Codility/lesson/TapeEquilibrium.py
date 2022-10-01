
'''
해당 길이의 합을 두 구간으로 나눴을 때 가장 차이가 작게 해 주는 그 '차이'를 찾으라는 것 같다.

'''

# from collections import deque
#
# def solution(A):
#     add_arr = deque()
#     add_arr.append(A[0])
#     for x in range(1, len(A)):
#         add_arr.append(add_arr[-1]+A[x])
#
#     reverse_add_arr = deque()
#     reverse_add_arr.append(A[-1])
#     for k in range(len(A)-2, -1, -1):
#         reverse_add_arr.insert(0, reverse_add_arr[0]+A[k])
#
#     min_value = 10e9
#     for x in range(1, len(reverse_add_arr)):
#         value = abs(reverse_add_arr[x]-add_arr[x-1])
#         if value < min_value:
#             min_value = value
#     return min_value


# 위 코드는 76% 통과. 굉장히 큰 수의 경우 timeout이 걸림.




print(solution([3,1,2,4,3]))






