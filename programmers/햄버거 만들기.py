'''
스택 문제인거 같은데
'''

# def solution(ingredient):
#     stack = []
#     cnt = 0
#     for n in ingredient:
#         if n == 1 and len(stack) >= 4: # 1일 때만 꺼내보고 아니면 다시 넣어보자
#             value = stack[-3:]
#             if value == [1,2,3]:
#                 stack.pop()
#                 stack.pop()
#                 stack.pop()
#                 cnt += 1
#             else:
#                 stack.append(n)
#         else:
#             stack.append(n)
#     return cnt

# 위 코드는 2개 틀림 (88.2점)

def solution(ingredient):
    stack = []
    cnt = 0
    pass

    return cnt





print(solution([2,1,1,2,3,1,2,3,1]))
print(solution([1,3,2,1,2,1,3,1,2]))





